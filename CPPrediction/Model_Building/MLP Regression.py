"""
Created on Tue Mar 14 2023
@author: Haowen Shi
"""

#import required libaray
import numpy as np
import pandas as pd
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


#import data from excel
df = pd.read_csv("Merge_temp.csv")

#select the features (x) and target (y) for model
x = df.drop(["ACTUAL_VOLUME"], axis=1)
y = df["ACTUAL_VOLUME"]

#split the dataset into train and test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=42)

#scale the data
scaler = StandardScaler()
X_train = scaler.fit_transform(x_train)
X_test = scaler.fit_transform(x_test)


#instantiate the model
modelMLP = MLPRegressor(hidden_layer_sizes=[100,100], max_iter=2000)

#fit the model on the train set
modelMLP.fit(X_train, y_train)

#-perform prediction on X_test
predictedMLP = modelMLP.predict(X_test)

#control the min predicted volume is 0
predictedMLP = np.clip(predictedMLP, a_min=0, a_max=None)

#Evaluate the model: R-square
score = modelMLP.score(X_test, y_test)
print(f'MLP R2: {score}')

#create result DataFrame
result = pd.DataFrame({'Actual': y_test, 'Predicted_MLP': predictedMLP}).astype('int')
combined = pd.concat([result,x_test], axis=1)

#export result DataFrame to CSV file
combined.to_csv('FinalResultMLP.csv')



""" # plot test data and model prediction
import matplotlib.pyplot as plt
plt.scatter(y_test, predictedMLP)
plt.plot(y_test, y_test, color='red')
plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.show()
 """






