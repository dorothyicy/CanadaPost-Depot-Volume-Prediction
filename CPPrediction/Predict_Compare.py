"""
Created on Tue Mar 21 2023
@author: Ching Yue Ip
"""

#Import necessary libraries
import pandas as pd


#Load the three dataframes
dfMLP_no = pd.read_csv("MLP_no.csv")
dfDT_no = pd.read_csv("DT_no.csv")
dfRF_no = pd.read_csv("RF_no.csv")
dfMLP_ww = pd.read_csv("MLP_ww.csv")
dfDT_ww = pd.read_csv("DT_ww.csv")
dfRF_ww = pd.read_csv("RF_ww.csv")

#Concatenate the dataframes along axis=1 to combine them horizontally
dfMerged = pd.concat([dfMLP_no, dfDT_no['DT_no'], dfRF_no['RF_no'],dfMLP_ww['MLP_ww'], dfDT_ww['DT_ww'], dfRF_ww['RF_ww']], axis=1)

#Compute the average predicted column and add it to dfMerged
dfMerged['AVE_no'] = dfMerged[['MLP_no','DT_no','RF_no']].mean(axis=1)
dfMerged['AVE_ww'] = dfMerged[['MLP_ww','DT_ww','RF_ww']].mean(axis=1)

if (dfMerged['CITY_MISSISSAUGA'] == 1).any():
    dfMerged.loc[dfMerged['CITY_MISSISSAUGA'] == 1, 'CITY'] = 'Mississauga'
    dfMerged.drop('CITY_MISSISSAUGA', axis=1,inplace=True)

if (dfMerged['CITY_RED DEER'] == 1).any():
    dfMerged.loc[dfMerged['CITY_RED DEER'] == 1, 'CITY'] = 'Red Deer'
    dfMerged.drop('CITY_RED DEER', axis=1,inplace=True)

if (dfMerged['CITY_VICTORIA'] == 1).any():
    dfMerged.loc[dfMerged['CITY_VICTORIA'] == 1, 'CITY'] = 'Victoria'
    dfMerged.drop('CITY_VICTORIA', axis=1,inplace=True)

dfMerged['CITY'].fillna('Brossard', inplace=True)


dfMerged.drop('NATIONAL_HOLIDAY_IND', axis=1,inplace=True)
dfMerged.drop('PROVINCIAL_HOLIDAY_IND', axis=1,inplace=True)
dfMerged.drop('IMPACT_DAY_FLG', axis=1,inplace=True)
dfMerged.drop('PEAK', axis=1,inplace=True)

dfMerged['date'] = pd.to_datetime('2023-' + dfMerged['MONTH_NO'].astype(str) + '-' + dfMerged['DAY_OF_MONTH'].astype(str))





#Save the updated dataframe to a new CSV file
dfMerged.to_csv("FinalResultAll.csv", index=False)


print('The average predicted volumn is calculated in FinalResultAll.csv!')






