"""
Created on Tue Mar 21 2023
@author: Ching Yue Ip
"""

#Import necessary libraries
import pandas as pd

#Load the three dataframes
dfMLP = pd.read_csv("FinalResultMLP.csv")
dfDT = pd.read_csv("FinalResultDT.csv")
dfRF = pd.read_csv("FinalResultRF.csv")

#Concatenate the dataframes along axis=1 to combine them horizontally
dfMerged = pd.concat([dfMLP, dfDT['Predicted_DT'], dfRF['Predicted_RF']], axis=1)

#Compute the average predicted column and add it to dfMerged
dfMerged['Avg predicted'] = dfMerged[['Predicted_MLP','Predicted_DT','Predicted_RF']].mean(axis=1)

#Save the updated dataframe to a new CSV file
dfMerged.to_csv("FinalResultAll.csv", index=False)

print("The average predicted test result of three models are calculated in FinalResultAll.csv")
