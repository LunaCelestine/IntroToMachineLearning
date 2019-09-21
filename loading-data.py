# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 12:41:13 2019

@author: Lunafreya Celestine
"""

import numpy as np
import pandas as pd

# Read the titanic_dataset.csv 
# file into a pandas.dataframe
df0 = pd.read_csv(r'data\train.csv')
print(len(df0))

# Drop any rows with a null
df1 = df0.dropna()
print(len(df1))

# Replace null values with column mean
df2 = df0.fillna(df0.mean())
print(len(df2))

# Replace null values with column maximum
df3 = df0.fillna(df0.max())
print(len(df3))

# Replace null values with column minimum
df4 = df0.fillna(df0.min())
print(len(df4))

# REplace null values with column median
df5 = df0.fillna(df0.median())
print(len(df5))















