"""
Created on Tue Mar 14 2023
@author: Haowen Shi
"""

#import required libaray
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.utils import shuffle



def MLPPredict(weatherflag):
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

#scale the data
    scaler = StandardScaler()
    X_train = scaler.fit_transform(x_train)
    X_test = scaler.fit_transform(x_test)

    X_train, y_train = shuffle(X_train, y_train)
#instantiate the model
    modelMLP = MLPRegressor(hidden_layer_sizes=[100,100], max_iter=2000)

#fit the model on the train set
    modelMLP.fit(X_train, y_train)

#-----perform prediction on X_test-----
    predictedMLP = modelMLP.predict(X_test)

#-----control the min predicted volume is 0-----
    predictedMLP = np.clip(predictedMLP, a_min=0, a_max=None)


    result = pd.DataFrame({f'MLP_{weatherflag}': predictedMLP}).astype('int')
    combined = pd.concat([x_test,result], axis=1)

#-----export result DataFrame to CSV file-----
    combined.to_csv(f'MLP_{weatherflag}.csv', index=False)






MLPPredict('no')
MLPPredict('ww')

print('MLP Prediction End!')


