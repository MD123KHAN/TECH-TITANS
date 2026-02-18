import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Fake dataset for training
data = pd.DataFrame({
    "age": np.random.randint(1, 1000, 500),
    "urgency": np.random.randint(1, 10, 500),
    "adjournments": np.random.randint(0, 10, 500),
})

data["delay"] = (
    (data["age"] > 500) |
    (data["adjournments"] > 5)
).astype(int)

X = data[["age","urgency","adjournments"]]
y = data["delay"]

model = RandomForestClassifier()
model.fit(X,y)

pickle.dump(model, open("model.pkl","wb"))

print("Model Trained & Saved")
