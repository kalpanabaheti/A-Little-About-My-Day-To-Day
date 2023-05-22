#!/usr/bin/env python
# coding: utf-8

# In[1]:


#for interaction scoring
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

#for side effect prediction
import keras.models
from sklearn.metrics import classification_report
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import joblib


# In[2]:


# Load the pre-trained ChemBERTa model and tokenizer
transformer = AutoModelForSequenceClassification.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")
tokenizer = AutoTokenizer.from_pretrained("seyonec/ChemBERTa-zinc-base-v1")


# In[3]:


scaler = joblib.load('scaler.pkl')
pca = joblib.load('pca_transform.pkl')
model = keras.models.load_model('max_accuracy_model')


# In[ ]:




