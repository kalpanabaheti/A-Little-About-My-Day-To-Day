#!/usr/bin/env python
# coding: utf-8

# In[1]:


import deepchem as dc
from rdkit import Chem
from rdkit.Chem import AllChem, rdPartialCharges
from rdkit.Chem.EState import EStateIndices
import pubchempy as pcp

import Interaction_Scoring
import SideEffect_Prediction

from collections import Counter

import copy
from itertools import combinations
import random
import numpy as np
import pandas as pd
import csv
import json
import os

error_message = ''


# In[2]:

def driver(drugs):
    df = pd.read_csv('test_charges.csv')
    column_names = list(df.columns)
    column_names.remove('Y')

    def get_atom_symbol(column_name):

        symbol = ''
        for char in column_name:
            if char.isalpha():
                symbol+=char
            else:
                break

        return symbol

    keys = []
    for column_name in column_names:

        name = get_atom_symbol(column_name)
        if name not in keys:

            keys.append(name)

    filename = "max_atoms.json"

    # Read the contents of the JSON file
    with open(filename, "r") as f:
        data = json.load(f)

    with open('smiles_name.json', "r") as f1:
        smiles_name = json.load(f1)

    with open('name_smiles.json', "r") as f2:
        name_smiles = json.load(f2)

    with open('side_effect_dict.json', "r") as f3:
        side_effect_dict = json.load(f3)


    # In[3]:


    def get_partial_charges(smiles_molecule):

        # Create an RDKit molecule object from the SMILES string
        mol = Chem.MolFromSmiles(smiles_molecule)

        # Add hydrogens to the molecule
        mol = Chem.AddHs(mol)

        # Generate a conformer for the molecule
        AllChem.EmbedMolecule(mol)

        # Create a PyMMFFMolProperties object for the molecule
        props = AllChem.MMFFGetMoleculeProperties(mol)

        # Calculate the partial charges using the MMFF94 force field
        ff = AllChem.MMFFGetMoleculeForceField(mol, props)
        ff.Initialize()
        rdPartialCharges.ComputeGasteigerCharges(mol)
        charges = [float(atom.GetProp("_GasteigerCharge")) for atom in mol.GetAtoms()]

        # Print the partial charges for each atom
        charge_dict = dict()
        for i, atom in enumerate(mol.GetAtoms()):

            atom_symbol = atom.GetSymbol()
            if atom_symbol not in charge_dict.keys():
                charge_dict[atom.GetSymbol()]=[charges[i]]
            else:
                charge_dict[atom.GetSymbol()].append(charges[i])

        for key, value in charge_dict.items():
            value.sort()

        return charge_dict

    def get_attributes(molecule):

        features = get_partial_charges(molecule)
        ordered_vector = []
        for key in keys:

            total_count = data[key]
            if key in features.keys():

                values = features[key]
                num_zeros = [0.0]*(total_count-len(values))
                values.extend(num_zeros)

            else:
                values = [0.0]*total_count

            ordered_vector.extend(values)

        return ordered_vector

    def transform(df, column_names):

        global error_message

        transformed_smiles = []
        transformed_data = []

        for index, row in df.iterrows():

            row_list = row.tolist()

            try:

                molecule1 = row_list[0]
                molecule2 = row_list[1]

                feature_vec1 = get_attributes(molecule1)
                feature_vec2 = get_attributes(molecule2)

                feature_vec1.extend(feature_vec2)
                transformed_row = feature_vec1

                transformed_data.append(transformed_row)
                transformed_smiles.append(row_list)

            except:

                error_message = '\n'+'Record discarded due to parsing error!'

        new_df = np.array(transformed_data)
        old_df = np.array(transformed_smiles)

        return old_df, new_df

    def get_data(textfile):

        with open(textfile, 'r') as file:
            lines = file.readlines()

        drug_list = []

        if lines!=[]:

            input_data = list(map(eval, lines[0].strip().split()))
            drug_list = list(input_data[0])

        return drug_list



    def put_data(textfile, data): #requires import json

        result = []
        for record in data:
            entry = dict()
            entry['Drug 1'] = str(record[0]) #str
            entry['Drug 2'] = str(record[1]) #str
            entry['Side Effect'] = str(record[2]) #str
            entry['Confidence'] = float(record[3]) #float
            result.append(entry)

        with open(textfile, "w") as outfile:
            json.dump(result, outfile)


    # In[4]:


    input_set_of_drugs = set(drugs)


    # In[5]:


    def convert_drug_to_smiles(drug_name):

        compound = pcp.get_compounds(drug_name, 'name')
        if len(compound)>0:

            smiles = compound[0].isomeric_smiles
            return smiles

        return False


    # In[6]:


    def get_smiles_info(input_set_of_drugs):

        smiles_to_drug_dict = dict()
        drug_set = set()
        for drug in input_set_of_drugs:

            global error_message

            try:

                if drug in name_smiles.keys():
                    smiles = name_smiles[drug]

                else:
                    smiles = convert_drug_to_smiles(drug)

            except:
                error_message = '\n'+drug+'cannot be parsed!'
                continue

            smiles_to_drug_dict[smiles]=drug
            drug_set.add(smiles)

        return smiles_to_drug_dict, drug_set


    # In[7]:


    smiles_to_drug_dict, drug_set = get_smiles_info(input_set_of_drugs)
    subsets = []
    for drug1 in drug_set:
        for drug2 in drug_set:
            pair1, pair2 = [drug1, drug2], [drug2,drug1]
            if drug1!=drug2 and pair1 not in subsets and pair2 not in subsets:
                subsets.append(pair1)

    drug_pairs = np.array(list(subsets))
    df = pd.DataFrame(drug_pairs, columns=['drug1', 'drug2'])


    # In[8]:


    old_df, new_df = transform(df, column_names)


    # In[9]:


    records = []
    effects = []

    for r in range(old_df.shape[0]):

        smiles_1, smiles_2 = old_df[r,0], old_df[r,1]
        features = np.array([new_df[r]])

        score = Interaction_Scoring.get_interaction_score(smiles_1, smiles_2)
        side_effect = SideEffect_Prediction.get_side_effect_number(features)

        new_record = [smiles_to_drug_dict[smiles_1], smiles_to_drug_dict[smiles_2], side_effect_dict[str(side_effect)], score]
        records.append(new_record)
        effects.append(side_effect_dict[str(side_effect)])

    counts = Counter(effects)
    most_effects = []
    for k,v in counts.items():
        entry = dict()
        entry['effect'] = k
        entry['count'] = v
        most_effects.append(entry)
    with open('static/vis_file.json', "w") as outfile:
            json.dump(most_effects, outfile)


    # In[11]:


    put_data('static/output_file.json', records)


# In[ ]:




