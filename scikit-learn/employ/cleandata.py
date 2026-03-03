import pandas as pd
import numpy as np 

data={
    "name":["Alice","Bob","Charlie","David","Eva","Alice","Frank"],
    "age":[25,30,np.inf,35,-np.inf,25,40],
    "city":["New York","Los Angeles","New York","Chicago","Houston","New York","Chicago"],
    "salary":[70000,800,90000,None,5000000,70000,None]
}

df=pd.DataFrame(data)
print("Original DataFrame:",df)

# check the missing values
print("\nMissing values in each column:")

print(df.isnull().sum())

# now we will handle the missing values with the average of the column

df["salary"].fillna(df["salary"].mean(),inplace=True)

print(df)

# find the infinite values in the dataframe
numeric_df = df.select_dtypes(include=[np.number]) # select only numeric columns
print("\nInfinite values in each column:")
print(np.isinf(numeric_df).sum())

# replace the infinite values with the average of the column
df.replace([np.inf,-np.inf],np.nan,inplace=True)

print (df)
df["age"].fillna(df["age"].mean(),inplace=True)
print(df)

# drop the duplicate rows
df.drop_duplicates(inplace=True)
print("\nDataFrame after dropping duplicates:")
print(df)

# let handle outliers  and fix too low and too high salaries
low_limit  = df["salary"].quantile(0.10)   # bottom 10%
high_limit = df["salary"].quantile(0.90)   # top 10%

# Mean salary excluding extremes
mean_salary = df.loc[
    (df["salary"] >= low_limit) & (df["salary"] <= high_limit),
    "salary"
].mean()

# Replace too low and too high salaries with mean
df["salary"] = np.where(
    (df["salary"] < low_limit) | (df["salary"] > high_limit),
    mean_salary,
    df["salary"]
)

print("DataFrame after fixing too low & too high salaries:")
print(df)

# save the cleaned data to a csv file
df.to_csv("/Users/ramrekhayadav/mlops/scikit-learn/employ/cleaned_data.csv",index=False)