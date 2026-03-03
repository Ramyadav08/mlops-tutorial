import pandas as pd   
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.model_selection import train_test_split

data={
    "hours_studied":[1,2,3,4,5,6,7,8,9,10],
    "attendance_percentage":[55,60,65,70,75,80,85,90,95,100]
}

df=pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# standardscaling mean =0 and standard deviation =1 which helps in normalizing the data between a particular range
# StandardScaler is used for standardization of data 
# StandardScaler = (X - mean) / std_dev
scaler=StandardScaler()
scaled_data=scaler.fit_transform(df)

df_standard_scaled=pd.DataFrame(scaled_data,columns=df.columns)
print("\nStandard Scaled DataFrame:")
print(df_standard_scaled)

#minmax scaling is used to scale the data between a particular range usually between 0 and 1
# MinMaxScaler = (X - min) / (max - min) 
minmax_scaler=MinMaxScaler()
minmax_scaled_data=minmax_scaler.fit_transform(df)
df_minmax_scaled=pd.DataFrame(minmax_scaled_data,columns=df.columns)
print("\nMin-Max Scaled DataFrame:")
print(df_minmax_scaled)

# Splitting the dataset into training and testing sets

X=df[["hours_studied"]]
y=df[["attendance_percentage"]]

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

print("\nTraining Features:")
print(X_train)

print("\nTesting Features:")
print(X_test)

# regration is used to predict the continuous values like salary , age , height etc that belong to numbers

# type of regression    
# 1. Linear Regression: Models the relationship between a dependent variable and one or more independent variables using a straight line.
# 2. classification regression: 
# >Logistic Regression: Used for binary classification problems, predicting the probability of a binary outcome.
# > K-Nearest Neighbors (KNN) Regression: Predicts the value of a data point based on the average of its k-nearest neighbors.
# > Decision Tree Regression: Uses a tree-like model of decisions to predict the value of a target variable based on input features.