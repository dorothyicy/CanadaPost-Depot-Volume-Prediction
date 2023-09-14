#import required libaray
import pandas as pd

#import data from excel
dfDeport = pd.read_excel('depot.xlsx')
dfWeather = pd.read_excel('weather.xlsx')

#join two dataframe on center Id and dat
dfMerge = pd.merge(dfDeport, dfWeather,left_on=['COST_CENTRE_ID','CALENDAR_DATE']\
                   , right_on=['COST_CENTRE_ID','Date/Time'])


print(dfMerge.info())
desc = dfMerge.describe()
desc.to_csv("C:\CPPrediction\Model_Building\describe.csv")
