# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:41:19 2022

@author: cr_ru
"""
# =============================================================================
# Nestle project - clean data source file 'Excel Data 2020.xlsx'
# =============================================================================

# import dataset and create dataframe
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Engage Data 2020.xlsx")   # create a dataframe, fill in with excel contents
pd.set_option('display.max_columns', None)  #show all columns

# EDA
# data shape
df.head() 
print(df.shape)
df.columns
columns=list(df.columns)
print(columns)
df.describe(include='all')

# ETL
# examine missing values
print("Missing values distribution:")
print(df.isnull().mean().sort_values(ascending=False))  # descending order by mean 
# missing value exists: True, 1.
# missing value doesn't exists: false, 0.
# 4 columns doesn't have missing values

# pattern
# plt.bar() # want bar chart, x=open date , y = Business



# proportion of missing data


# ETL
# df['Contact Qualification'].unique()


# convert string to datetime data type, format yyyy-mm-dd
df['Opened Date']=pd.to_datetime(df['Opened Date'], format='%d/%m/%Y')
df['Closed Date']=pd.to_datetime(df['Closed Date'], format='%d/%m/%Y')
# print(df.dtypes) 
df['Opened Date']=df['Opened Date'].dt.strftime('%Y-%m-%d')
# print(df['Opened Date'])
df['Closed Date']=df['Closed Date'].dt.strftime('%Y-%m-%d')
# print(df['Closed Date'])

df['Opened Date']=pd.to_datetime(df['Opened Date'], format='%Y-%m-%d')
df['Closed Date']=pd.to_datetime(df['Closed Date'], format='%Y-%m-%d')
# print(df.dtypes)
# print(df['Opened Date'])
# print(df['Closed Date'])

# Look at the proportion of missing data
# Check the data type of each column
# If you have columns of strings, check for trailing whitespaces
# Dealing with Missing Values (NaN Values)
# Extracting more information from your dataset to get more variables
# Check the unique values of columns

# df['Contact Qualification'].unique()
# need to remove record with cq=1856
# what does it mean by cq= update profile, unsubscribe, not received
df.to_excel('Engage Data 2020_p.xlsx', sheet_name='FINAL', index=False)








# some records have no Closed Date, want to create a categorical column, ticket status: open/closed

# different between open date and closed date-->waiting days

# how many unique values in column "contact 



















