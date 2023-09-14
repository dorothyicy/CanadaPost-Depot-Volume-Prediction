"""
Created on Sat Feb 25 2023
@author: Ching Yue Ip, Haowen Shi
"""

#import required libaray
import pandas as pd

#import data from excel
dfDeport = pd.read_excel('depot.xlsx')
dfWeather = pd.read_excel('weather.xlsx')

#join two dataframe on center Id and dat
dfMerge = pd.merge(dfDeport, dfWeather,left_on=['COST_CENTRE_ID','CALENDAR_DATE'], right_on=['COST_CENTRE_ID','Date/Time'])


#----------Data Cleaning----------
#-----drop wanted observation 
#remove irrelevant column from the dataframe
drop = ['Data Quality', 'Climate ID', 'Dir of Max Gust (10s deg)', 'Snow on Grnd (cm)']
dfMerge.drop(drop, axis=1, inplace=True)

#remove the flag column from the dataframe
for column in dfMerge.columns:
    if 'Flag' in column:
        dfMerge.drop([column], axis=1, inplace=True)

#remove the redundant location features from the dataframe
drop = ['Longitude (x)', 'Latitude (y)', 'SITE_PROVINCE_CODE', 'COST_CENTRE_ID', 'POSTAL_CODE', 'Station Name']
dfMerge.drop(drop, axis=1, inplace=True)

#remove the useless date features from the dataframe
drop = ['Date/Time', 'DAY_OF_MONTH', 'YEAR_NO', 'CALENDAR_DATE', 'Year', 'Month', 'Day', 'WEEK_OF_YEAR']
dfMerge.drop(drop, axis=1, inplace=True)


#-----handle missing value
#calculate the mean for each column
means = dfMerge.mean()

#fill null values in the columns with 0 or mean
dfMerge['Max Temp'].fillna(means['Max Temp'], inplace=True)
dfMerge['Min Temp'].fillna(means['Min Temp'], inplace=True)
dfMerge['Mean Temp'].fillna(means['Mean Temp'], inplace=True)
dfMerge['Heat Deg Days'].fillna(means['Heat Deg Days'], inplace=True)
dfMerge['Cool Deg Days'].fillna(means['Cool Deg Days'], inplace=True)
dfMerge['Total Rain (mm)'].fillna(0, inplace=True)
dfMerge['Total Snow (cm)'].fillna(0, inplace=True)
dfMerge['Total Precip (mm)'].fillna(0, inplace=True)
dfMerge['Spd of Max Gust (km/h)'].fillna(means['Spd of Max Gust (km/h)'], inplace=True)


#----------Feature Engineering----------
#create dummy variables for "City"
dfMerge =pd.get_dummies(dfMerge,columns=['CITY'],drop_first=True)

dfMerge.to_csv('Merge_temp.csv', index=False)
print("Data Cleaning and Feature Engineering End")