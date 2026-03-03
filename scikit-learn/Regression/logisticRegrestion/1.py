from sklearn.linear_model import LogisticRegression
import pandas as pd

data={
    "hours_studied":[1,2,3,4,5,6,7,8,9,10],
    "passed_exam":[0,0,0,0,1,1,1,1,1,1]   # 0=failed , 1=passed
}

df=pd.DataFrame(data)

X=df[["hours_studied"]]
y=df["passed_exam"]

model=LogisticRegression()
model.fit(X,y)
# making predictions
hours=float(input("Enter the number of hours studied: "))

predict_pass=model.predict([[hours]])[0]
result="Passed" if predict_pass==1 else "Failed"
print(f"Predicted result for studying {hours} hours: {result}")