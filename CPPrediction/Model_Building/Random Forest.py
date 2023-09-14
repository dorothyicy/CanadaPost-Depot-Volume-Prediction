"""
Created on Mon Mar 20 2023
@author: Ching Yue Ip
"""


# Import necessary libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

#import data from excel
df = pd.read_csv("Merge_temp.csv")

#select the features (x) and target (y) for model
x = df.drop(["ACTUAL_VOLUME"], axis=1)
y = df["ACTUAL_VOLUME"]

#split the dataset into train and test
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2,random_state=42)

# Create a RandomForest model
modelRF =  RandomForestRegressor(n_estimators=50,  random_state=42)

# Train the model on the training data
modelRF.fit(X_train, y_train)

# Make predictions on the testing data
predictedRF = modelRF.predict(X_test)


# Evaluate the model
r2 = r2_score(y_test, predictedRF)
print(f'Random Forest R2: {r2}')

#create result DataFrame
result = pd.DataFrame({'Actual': y_test, 'Predicted_RF': predictedRF}).astype('int')
combined = pd.concat([result,X_test], axis=1)

#export result DataFrame to CSV file
combined.to_csv('FinalResultRF.csv')

#visualize the model
import matplotlib.pyplot as plt

plt.scatter(y_test, predictedRF)
plt.plot(y_test, y_test, color='red')
plt.xlabel('True values')
plt.ylabel('Predicted values')
plt.show() 
