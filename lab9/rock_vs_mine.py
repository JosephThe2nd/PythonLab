#Workflow - Sonar Data - Data pre processing - Train Test split - Logistic Regression model - 
# New data - Trained Logistic Regression model -  Rock or mine
#Rock Vs Mine Prediction

#Importing Dependencies
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Data collection and Data Processing 

#loading the dataset to a pandas Dataframe
sonar_data = pd.read_csv('C:\\Users\\covas\\Documents\\GitHub\\PythonLab\\lab9\\Copy of sonar data.csv', header=None)

#print(sonar_data.head())

#number of rows and colums
#print(sonar_data.shape)

#print(sonar_data.describe()) #describe  - statistical measures of the data

#coloana 60 , cate Roci si cate Mine sunt(cu cat numerele sunt mai apropiate, cu atat predictia mai buna)
#print(sonar_data[60].value_counts()) 


#grouping by type R/M
#print(sonar_data.groupby(60).mean())

#separating data and labels
X = sonar_data.drop(columns=60, axis = 1) #values
Y = sonar_data[60] #label
print(X)
print(Y)

#Training and Test data
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1, stratify=Y, random_state=1)#10% test
print (X.shape, X_train.shape, X_test.shape)

#Model training  -> Logistic Regression 
model = LogisticRegression()

#Training the Logistic Regression Model with training data
model.fit(X_train,Y_train)

#Model evaluation
#accuraacy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)
print("Accuracy on training data:", training_data_accuracy)

#accuraacy on test data
X_test_prediction = model.predict(X_test)
testing_data_accuracy = accuracy_score(X_test_prediction, Y_test)
print("Accuracy on testing data:", testing_data_accuracy)

#Making a Predictive System

#this is rock
input_data = (0.0270,0.0163,0.0341,0.0247,0.0822,0.1256,0.1323,0.1584,0.2017,0.2122,0.2210,0.2399,0.2964,0.4061,0.5095,0.5512,0.6613,0.6804,0.6520,0.6788,0.7811,0.8369,0.8969,0.9856,1.0000,0.9395,0.8917,0.8105,0.6828,0.5572,0.4301,0.3339,0.2035,0.0798,0.0809,0.1525,0.2626,0.2456,0.1980,0.2412,0.2409,0.1901,0.2077,0.1767,0.1119,0.0779,0.1344,0.0960,0.0598,0.0330,0.0197,0.0189,0.0204,0.0085,0.0043,0.0092,0.0138,0.0094,0.0105,0.0093)
#this is a mine
#0.0270,0.0163,0.0341,0.0247,0.0822,0.1256,0.1323,0.1584,0.2017,0.2122,0.2210,0.2399,0.2964,0.4061,0.5095,0.5512,0.6613,0.6804,0.6520,0.6788,0.7811,0.8369,0.8969,0.9856,1.0000,0.9395,0.8917,0.8105,0.6828,0.5572,0.4301,0.3339,0.2035,0.0798,0.0809,0.1525,0.2626,0.2456,0.1980,0.2412,0.2409,0.1901,0.2077,0.1767,0.1119,0.0779,0.1344,0.0960,0.0598,0.0330,0.0197,0.0189,0.0204,0.0085,0.0043,0.0092,0.0138,0.0094,0.0105,0.0093

# changing the input_data to a numpy array (bcs it is faster than the list)
input_data_as_numpy_array = np.asarray(input_data)  

#reshape the np array as we are predicting for  one istance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = model.predict(input_data_reshaped)
if(prediction[0] =='R'):
    print("The object is a Rock")
else: print("The object is a mine")







        


