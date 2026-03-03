from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error

#mae is mean absolute error that means average of absolute difference between actual and predicted values
#mse is mean squared error that means average of squared difference between actual and predicted values
#rmse is root mean squared error that means square root of mean squared error

import numpy as np

# Actual values
y_true=[90,60,80,100]

# Predicted values
y_pred=[85,70,70,95]

#how to find mae y_true - y_pred and take absolute(remove -) value and then take mean

mae=mean_absolute_error(y_true,y_pred)

print(f"Mean Absolute Error (MAE):{mae}")

mse=mean_squared_error(y_true,y_pred)

print(f"Mean Squared Error (MSE):{mse}")
rmse=root_mean_squared_error(y_true,y_pred)
print(f"Root Mean Squared Error (RMSE):{rmse}")