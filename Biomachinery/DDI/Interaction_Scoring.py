#!/usr/bin/env python
# coding: utf-8

# In[5]:


from Setup_Module import transformer, tokenizer
import torch
import keras.models
from sklearn.metrics import classification_report
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import joblib


# In[8]:


def get_interaction_score(smiles_1, smiles_2):
    
    # Example of SMILES strings
    #smiles_1 = 'COC1=CC2=C(C=C1)C(C)=C(N2)CCN(CC)CC'
    #smiles_2 = 'CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)Cl)C3=CC=CC=C3'

    # Encode the SMILES strings using the tokenizer
    encoding_1 = tokenizer(smiles_1, return_tensors='pt', padding=True, truncation=True)
    encoding_2 = tokenizer(smiles_2, return_tensors='pt', padding=True, truncation=True)

    # Concatenate the input IDs and attention masks into a single tensor for each SMILES string
    input_ids = torch.cat((encoding_1['input_ids'], encoding_2['input_ids']), dim=1)
    attention_mask = torch.cat((encoding_1['attention_mask'], encoding_2['attention_mask']), dim=1)

    # Make the prediction
    with torch.no_grad():
        
        logits = transformer(input_ids=input_ids, attention_mask=attention_mask)[0]
        logits_avg = torch.mean(logits)
        interaction_score = torch.sigmoid(logits_avg).item()
        
    #print('The interaction score between the two drugs is:', interaction_score)
        
    return round(interaction_score,2)


# In[9]:


#print(get_interaction_score('COC1=CC2=C(C=C1)C(C)=C(N2)CCN(CC)CC','CC1=C(C=C(C=C1)NC(=O)C2=CC=C(C=C2)Cl)C3=CC=CC=C3'))


# In[ ]:




