# DESCRIPTION - 

The package is a webapp-based system that takes in a list of drugs from a dropdown menu, and displays a table of drug pairs from input drugs, with most probable side-effect associated with the pair. It also returns an interaction (trust) score for each drug-pair and graphs that. 

What happens on the backend when a list of drugs is sent is that the drugs are first reduced to distinct pairs of drugs, and each drug-pair is sent to two models - the side-effect prediction model and the interaction scoring model. They return the most probable side-effect and trust score respectively. 

The interaction scoring model is based on the pre-trained ChemBERTa transformer that takes in two SMILES-formatted drugs, featurises them for interaction, runs them through a sigmoid function to get a score between 0 and 1. The higher the score, the more serious the interaction.

The side-effect prediction (restricted to 10 side-effects for PoC) is the major part of our research. It focuses on the sole contribution of structural similarity of drugs to competing for a binding spot on the human proteome, thus causing adverse effects - however this is only one contributor, but it is the center of our focus for this proof of concept and the aim to find the maximal possible inference extraction from a singular contributor. I decomposed drug-pairs from SMILES representation to residual atomic charges through logical deduction towards which feature-granularity will be adequate and within our compute power, and studied the relationship of the resultant feeature vectors of each drug-pair with the side-effects, via sequential neural networks after dimensionality reduction of features.I establish maximal inference from one contributor in this problem,usable for further in-depth research. 


# INSTALLATION - 

1. Download the package. 
2. To this package, download the test and train data - do not change their names. You can download the data from here - 

train_charges.csv: **https://drive.google.com/file/d/1DgsMVxOaS4Wkzjpw3M2lB2Fzp3EjCbxz/view?usp=sharing**

test_charges.csv: **https://drive.google.com/file/d/1caad2O8zIILPD72qtf4zu970Lms7riEw/view?usp=sharing**

3. Create a conda virtual environment in the package folder.
4. Install the following in the virtual environment. - 
  
  ```
  pip install scikit-learn
  pip install torch
  pip install deepchem
  pip install rdkit-pypi
  pip install PubChemPy
  pip install keras
  pip install joblib
  pip install transformers
  pip install python-csv
  pip install jsonlib
  pip install Flask
  ```


# EXECUTION - 

Open VSCode or Terminal, run main.py. A URL will be displayed, click on that URL to go to the webpage. Select diseases and drugs. Then click the 'Click to Run' button, then when the 'Display Data' button appears, click on that to view results. 


# DEMO VIDEO - **https://youtu.be/L93voZ2VOgU**
