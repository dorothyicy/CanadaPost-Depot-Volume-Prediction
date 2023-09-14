"""
Created on Sat Feb 25 2023
@author: Ching Yue Ip, Haowen Shi
"""

#import required libaray
import pandas as pd

#import data from excel
dfDeport = pd.read_excel('depot.xlsx')
dfWeather = pd.read_excel('weather.xlsx')

#drop the wanted column from depot excel
dfDeport.drop(['WEEK_OF_YEAR'],axis=1, inplace=True)
dfDeport.drop(['YEAR_NO'],axis=1, inplace=True)
dfDeport.drop(['POSTAL_CODE'],axis=1, inplace=True)
dfDeport.drop(['SITE_PROVINCE_CODE'],axis=1, inplace=True)


#----------Feature Engineering----------
#create dummy variables for "City"
dfDeport =pd.get_dummies(dfDeport,columns=['CITY'],drop_first=True)


#join two dataframe on center Id and dat
dfMerge = pd.merge(dfDeport, dfWeather,left_on=['COST_CENTRE_ID','CALENDAR_DATE'], right_on=['COST_CENTRE_ID','Date/Time'])


#----------Data Cleaning----------
#-----drop wanted observation 
#remove irrelevant column from the dataframe
dfMerge.drop(['Data Quality'],axis=1, inplace=True)
dfMerge.drop(['Climate ID'],axis=1, inplace=True)
dfMerge.drop(['Dir of Max Gust (10s deg)'],axis=1, inplace=True)
dfMerge.drop(['Snow on Grnd (cm)'],axis=1, inplace=True)


#remoev the flag column from the dataframe
for column in dfMerge.columns:
    if 'Flag' in column:
        dfMerge.drop([column], axis=1, inplace=True)

#remove the redundant location features from the dataframe
dfMerge.drop(['Longitude (x)'],axis=1, inplace=True)
dfMerge.drop(['Latitude (y)'],axis=1, inplace=True)
dfMerge.drop(['COST_CENTRE_ID'],axis=1, inplace=True)
dfDeport.drop(['COST_CENTRE_ID'],axis=1, inplace=True)
dfMerge.drop(['Station Name'],axis=1, inplace=True)

#remove the date features from the dataframe
dfMerge.drop(['Date/Time'],axis=1, inplace=True)
dfMerge.drop(['CALENDAR_DATE'],axis=1, inplace=True)
dfDeport.drop(['CALENDAR_DATE'],axis=1, inplace=True)
dfMerge.drop(['Year'],axis=1, inplace=True)
dfMerge.drop(['Month'],axis=1, inplace=True)
dfMerge.drop(['Day'],axis=1, inplace=True)



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
dfMerge['Spd of Max Gust (km/h)'].fillna(0, inplace=True)




#export a csv without weather data & a csv with weather
dfDeport.to_csv('Train_no.csv', index=False)
dfMerge.to_csv('Train_ww.csv', index=False)
print("Data Cleaning and Feature Engineering End")