#mlflow tracing server

import mlflow

mlflow.set_tracking_uri("http://127.0.0.1:5000")


mlflow.set_experiment("check the local host connection!")
with mlflow.start_run():
    mlflow.log_metric("test",1)
    mlflow.log_metric("ram",2)
    
    