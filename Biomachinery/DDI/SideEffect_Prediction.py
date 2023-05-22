#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Setup_Module import scaler, pca, model
from Setup_Module import transformer, tokenizer
import torch
import keras.models
from sklearn.metrics import classification_report
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import joblib
import json

with open('class_to_effect.json', "r") as f2:
    lookup = json.load(f2)


# In[3]:


def get_side_effect_number(instance):
    
    instance_scaled = scaler.transform(instance)
    instance_transformed = pca.transform(instance_scaled)
    
    y_pred = model.predict(instance_transformed)
    y_pred_class = np.argmax(y_pred, axis=1)
    
    fake_class = str(y_pred_class[0])
    actual_class = lookup[fake_class]
    
    return actual_class


# In[ ]:




