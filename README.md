# CanadaPost-Depot-Volume-Prediction
This is the capstone project, in cooperation with Canada Post, aimed at predicting depot volume.

# Project Summary
Despite the fact of being the largest parcel delivery company in Canada with around seven billion pieces of parcels delivered annually. Canada Post sets itself an ambitious goal of achieving 98% operational efficiency. Due to the fluctuation of parcel volumes to arrive in each depot caused by factors such as seasonality, special events, holidays, and even weather conditions, it is instrumental to have the ability to predict parcel volumes to be received for each depot so that resources can be effectively scheduled and allocated for improved operational efficiency and reduced overall cost. 
 
As per the requirement of the project sponsor, this project has two objectives:  
1. to conduct data explorations using selected depots’ historical volume data in order to identify any data/volume anomalies. For identified anomalies, explore the underlying causes.   
2. to develop a volume prediction model using Python programming language. The model is expected to have the capacity of making 14-day arrival parcel volume prediction for a particular depot with forecasted weather conditions in the next fourteen days. 
 
Canada Post provides the historical incoming parcel volume data for this project. The team collected weather data from the Government of Canada website in corresponding to the given locations and time period with hope to enhance the accuracy of the volume prediction model. The inclusion of weather data was proven to be valuable in terms of parcel volume prediction.
 
At the end of the project, the project team successfully achieved pre-defined goals with results meeting the sponsor’s requirements: 
1. Using Microsoft Power BI, we visually analyzed volume data from both data integrity perspective and volume irregularity perspective. For the identified volume anomalies, we researched potential causes, which were later verified.  
2. Using Python programming language, we developed three machine-learning models for the parcel volume prediction task. We developed two regression models, namely Decision Tree and MLP Regressor, and one ensemble model which is Random Forest. After using all three models to make independent predictions with satisfactory accuracies, we calculated the mathematical average of three predictive results and used it as our final volume prediction.  
3. We then compared model accuracy with weather data and without weather data respectively; we were convinced that weather data did improve prediction accuracy before we included weather data into our final prediction model.  
4. The final machine learning model developed is able to make parcel volume predictions for the next fourteen days for a particular depot with local forecasted weather conditions. 
5. The 14-day predicted volume can be imported to Microsoft Power BI, and generate a 14-day volume prediction chart for easy use by end users. 

# Dataset Information
depot.xlsx - The original depot volume data provided by Canada Post, refer 'CPC-Algonquin College - Depot Dashboard - Metadata Description.docx'

weather.xlsx - The historical weather data downloaded from Environment Canada

# Note
'depot.xlsx' has not been uploaded to this repository due to confidentiality reasons.
