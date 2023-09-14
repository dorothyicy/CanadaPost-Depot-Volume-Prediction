"""
Created on Mon Mar 20 2023
@author: Ching Yue Ip
"""


# Import necessary libraries
import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.utils import shuffle


def DTPredict(weatherflag):
#import data from excel
    df = pd.read_csv(f'Train_{weatherflag}.csv')

    columnOrder = df.columns
    predict = pd.read_csv(f'Predict_{weatherflag}.csv')
    predict = predict.reindex(columns=columnOrder)
    predict.drop(['ACTUAL_VOLUME'], axis=1, inplace=True)

#select the features (x) and target (y) for model
    X_train = df.drop(["ACTUAL_VOLUME"], axis=1)
    y_train = df["ACTUAL_VOLUME"]
    X_test = predict

#split the dataset into train and test
    X_train, y_train = shuffle(X_train, y_train)
# Create a decision tree model
    modelDT = DecisionTreeRegressor(max_depth=7,max_features=23)

# Train the model on the training data
    modelDT.fit(X_train, y_train)

# Make predictions on the testing data
    predictedDT = modelDT.predict(X_test)


#-----create result DataFrame-----
    result = pd.DataFrame({f'DT_{weatherflag}': predictedDT}).astype('int')
    combined = pd.concat([X_test,result], axis=1)

#-----export result DataFrame to CSV file-----
    combined.to_csv(f'DT_{weatherflag}.csv', index=False)


DTPredict('no')
DTPredict('ww')

print('Decision Tree Prediction End!')