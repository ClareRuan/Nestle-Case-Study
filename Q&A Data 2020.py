# -*- coding: utf-8 -*-
"""
Created on Tue Nov  8 11:57:00 2022

@author: cr_ru
"""
# =============================================================================
# Nestle - clean 'Q&A Data 2020.xlsx'
# =============================================================================
import pandas as pd
df=pd.read_excel('Q&A Data 2020.xlsx')
df.info()
df.shape
columns=list(df.columns)

df.head()
df.dtypes # no need to convert data types


# missing value proportion:
df.isnull().mean().sort_values(ascending=False) #no missing values

# what's unique value for them
df['Question Status'].unique()
df['Question Summary'].unique()
df['Product Brand'].unique()
# be able to join with 'Engage Date 2020.xlsx' on Product Brand