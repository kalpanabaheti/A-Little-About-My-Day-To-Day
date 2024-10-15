# DESCRIPTION - 

This package is a webapp-based system that takes in a list of drugs from a dropdown menu, and displays a table of drug pairs from input drugs, with the most probable side-effect associated with the pair. It also returns an interaction (trust) score for each drug-pair and graphs that. 

What happens on the backend when a list of drugs is sent is this - the drugs are first reduced to distinct pairs of drugs, and each drug-pair is sent to two models - the side-effect prediction model and the interaction scoring model. They return the most probable side-effect and trust score respectively. 

The interaction scoring model is based on the pre-trained ChemBERTa transformer that takes in two SMILES-formatted drugs, featurises them for interaction, runs them through a sigmoid function to get a score between 0 and 1. The higher the score, the more serious the interaction.

The side-effect prediction (restricted to 10 side-effects for this PoC) is the major part of my work. It focuses on the sole contribution of structural similarity of drugs that results in competing for a binding spot on the human proteome, thus causing adverse effects - this is only one contributor, however, owing to it's importance, it is the center of my focus for this proof of concept. The aim is to find the maximal possible inference extraction from this singular contributor. This approach decomposes drug-pairs from SMILES representation to spatially aware vectors of residual atomic charges - this method was arrived at through logical deduction by evaluating varied feature granularities and their performance. This approach is also constrained by limited available compute power. The work covers studying the relationship of the resultant feature vectors of each drug-pair with the side-effects, via sequential and graph neural networks after dimensionality reduction of features - to determine the most optimal model. We establish maximal inference from a single contributor in this problem, usable for further in-depth research. 


# INSTALLATION - 

1. Download the package. 
2. Download the test and train data, and save it within this package - do not change their names. You can download the data from here - 

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


# DEMO VIDEO - **https://drive.google.com/file/d/1QPVrstXvgNac7SgU6WyV5ieGnHbJ4OZF/view?usp=sharing**
