import pandas as pd  
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("/Users/ramrekhayadav/mlops/scikit-learn/encoded/sample.csv")
# print(df)

# ml can only understand numbers so we have to convert the categorical data into numerical 
# we can only apply level encoding on the categorical data like yes or no , male and femake where only two responses are there
# for the columns having more than two responses we have to use one hot encoding

le=LabelEncoder()
df_level=df.copy()

df_level["Gender_encoded"]=le.fit_transform(df_level["Gender"])
df_level["Passed_encoded"]=le.fit_transform(df_level["Passed"])

print(df_level.head())

# get_dummies is used for one hot encoding that is converting categorical data into numerical data where more than two responses are there

df_ecoded=pd.get_dummies(df_level,columns=["City"])
print(df_ecoded.head())

# let covert true and false into 1 and 0 for hot encoding
# converting boolean values to integers using astype(int)
df_ecoded["City_Bangalore"]=df_ecoded["City_Bangalore"].astype(int)
df_ecoded["City_Chennai"]=df_ecoded["City_Chennai"].astype(int)
df_ecoded["City_Mumbai"]=df_ecoded["City_Mumbai"].astype(int)
df_ecoded["City_Delhi"]=df_ecoded["City_Delhi"].astype(int)

print(df_ecoded.head()) 

# let save the encoded data to a csv file
df_ecoded.to_csv("/Users/ramrekhayadav/mlops/scikit-learn/encoded/encoded_data.csv",index=False)