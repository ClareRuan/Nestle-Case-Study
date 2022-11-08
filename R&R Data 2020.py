# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 12:20:37 2022

@author: cr_ru
"""

# =============================================================================
# Nestle - clean 'R&R Data 2020.xlsx' - Review & Ranking
# =============================================================================
import pandas as pd
df=pd.read_excel('R&R Data 2020.xlsx')
df.info()
df.shape
columns=list(df.columns)

df.head()
df.describe(include='all') 
# avg ranking is 4.18
# most people mentioned Brand 2.2 

# missing value proportion:
df.isnull().mean().sort_values(ascending=False) # only 2 columns have missing values

# what's unique value for them
df['Moderation Status'].unique()
df['Review Title'].unique()
df['Review Text'].unique()

# be able to join with 'Engage Date 2020.xlsx' on Product Brand