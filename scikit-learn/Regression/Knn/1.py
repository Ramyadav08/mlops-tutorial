from sklearn.neighbors import KNeighborsClassifier

import pandas as pd

data = {
    "weight": [5, 6, 7, 8, 9, 10],
    "size":   [1, 2, 3, 4, 5, 6],
    "fruit":  [0, 0, 0, 1, 1, 1]  # 0=Apple, 1=Banana
}

df = pd.DataFrame(data)

X = df[["weight", "size"]]
y = df["fruit"]

# print(X.shape)

model=KNeighborsClassifier(n_neighbors=3)
model.fit(X,y)

# making predictions
ws_input=float(input("Enter the weight: "))
size_input=float(input("Enter the size of the fruit: "))

predict_fruit=model.predict([[ws_input,size_input]])[0]

fruit="Apple" if predict_fruit==0 else "Banana"
print(f"Predicted fruit for weight {ws_input} and size {size_input}: {fruit}")
