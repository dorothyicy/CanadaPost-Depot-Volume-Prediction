"""
Created on Mon Mar 20 2023
@author: Ching Yue Ip
"""
# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.utils import shuffle



def RFPredict(weatherflag):
#import data from excel
    df = pd.read_csv(f'Train_{weatherflag}.csv')
    
    columnOrder = df.columns
    predict = pd.read_csv(f'Predict_{weatherflag}.csv')
    predict = predict.reindex(columns=columnOrder)
    predict.drop(['ACTUAL_VOLUME'], axis=1, inplace=True)

#select the features (x) and target (y) for model
    x_train = df.drop(["ACTUAL_VOLUME"], axis=1)
    y_train = df["ACTUAL_VOLUME"]
    x_test = predict

    x_train, y_train = shuffle(x_train, y_train)
# Create a RandomForest model
    modelRF =  RandomForestRegressor(n_estimators=100,  random_state=42)

# Train the model on the training data
    modelRF.fit(x_train, y_train)

# Make predictions on the testing data
    predictedRF = modelRF.predict(x_test)


    result = pd.DataFrame({f'RF_{weatherflag}': predictedRF}).astype('int')
    combined = pd.concat([x_test,result], axis=1)

#-----export result DataFrame to CSV file-----
    combined.to_csv(f'RF_{weatherflag}.csv', index=False)


RFPredict('no')
RFPredict('ww')

print('Random Forest Prediction End!')