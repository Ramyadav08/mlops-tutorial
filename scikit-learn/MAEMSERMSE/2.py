from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error
from sklearn.linear_model import LinearRegression

import numpy as np
import pandas as pd

data={
    "Hours":[1,2,3,4,5],
    "Scores":[50,60,70,80,90]
}

df= pd.DataFrame(data)

X= df[["Hours"]]    
y= df["Scores"]

model= LinearRegression()
model.fit(X,y)

predicted_scores=model.predict(X)
mae=mean_absolute_error(y,predicted_scores)
mse=mean_squared_error(y,predicted_scores)
rmse=root_mean_squared_error(y,predicted_scores)
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")

new_prediction=model.predict([[6]])
print(f"Predicted score for studying 6 hours: {new_prediction[0]}")