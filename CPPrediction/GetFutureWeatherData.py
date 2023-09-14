import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

def get_weather(city):
# Make a GET request to the webpage
    url = f"https://www.timeanddate.com/weather/canada/{city}/ext"
    response = requests.get(url)

# Create a BeautifulSoup object to parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

# Find the script tag containing the weather data
    script = soup("script", {"type":"text/javascript"})[0]

# Extract the weather data from the script tag
    data = script.string.partition('var data=')[-1]
    data = data[:-2]

    data = json.loads(data)

    df = pd.json_normalize(data, 'detail')

# Drop the useless columns
    useLess = ['hl','hls','date','ts','icon','desc','cf','hum','wd','pc']
    df = df.drop(useLess, axis=1)


# Rename the columns
    if 'snow' in df.columns:
        df.columns = ['Date', 'Max Temp', 'Min Temp', 'Spd of Max Gust (km/h)','Total Rain (mm)','Total Snow (cm)']
    else:
        df.columns = ['Date', 'Max Temp', 'Min Temp', 'Spd of Max Gust (km/h)','Total Rain (mm)']
        df['Total Snow (cm)'] = 0

    df['Total Snow (cm)'].fillna(0, inplace=True)
    df['Total Rain (mm)'].fillna(0, inplace=True)
    df['Mean Temp'] = (df['Max Temp'] + df['Min Temp'] )/2
    df['Total Precip (mm)'] = df['Total Rain (mm)'] + df['Total Snow (cm)']
    df['Heat Deg Days'] = df['Mean Temp'].apply(lambda x: 18-x if x<18 else 0)
    df['Cool Deg Days'] = df['Mean Temp'].apply(lambda x: x - 18 if x > 18 else 0)
    df['DAY_OF_WEEK'] = pd.to_datetime(df['Date'], format='%a, %b %d').dt.dayofweek + 1
    df['MONTH_NO'] = pd.to_datetime(df['Date'], format='%a, %b %d').dt.month
    df['DAY_OF_MONTH'] = pd.to_datetime(df['Date'], format='%a, %b %d').dt.day
    if city == 'MISSISSAUGA':
        df['CITY_MISSISSAUGA'] = 1
        df['CITY_RED DEER'] = 0
        df['CITY_VICTORIA'] = 0
    elif city == 'Reddeer':
        df['CITY_MISSISSAUGA'] = 0
        df['CITY_RED DEER'] = 1
        df['CITY_VICTORIA'] = 0
    elif city == 'VICTORIA':
        df['CITY_MISSISSAUGA'] = 0
        df['CITY_RED DEER'] = 0
        df['CITY_VICTORIA'] = 1
    else:
        df['CITY_MISSISSAUGA'] = 0
        df['CITY_RED DEER'] = 0
        df['CITY_VICTORIA'] = 0

    df = df.drop("Date", axis=1)
    return(df)


#Call the get_weather function for each city
dfs=[]
cityList = ['MISSISSAUGA','Reddeer','VICTORIA','montreal']
for city in cityList:
    df = get_weather(city)
    dfs.append(df)
combined_df = pd.concat(dfs)



combined_df = combined_df.assign(NATIONAL_HOLIDAY_IND=0, PROVINCIAL_HOLIDAY_IND=0, IMPACT_DAY_FLG=0, PEAK=0)




# output a csv file for prediction
combined_df.to_csv('Predict_ww.csv',index=False)



Drop_list = ['Max Temp', 'Min Temp', 'Spd of Max Gust (km/h)','Total Rain (mm)','Total Snow (cm)','Mean Temp','Total Precip (mm)','Heat Deg Days','Cool Deg Days']
Predict_no = combined_df.drop(Drop_list, axis=1)

# output a csv file for prediction without weather
Predict_no.to_csv('Predict_no.csv',index=False)

print('The next 14 days Weather data is in Predict_ww.csv!')

