from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI()

# Load model
model = pickle.load(open("decision_tree_model.pkl", "rb"))

@app.post("/predict")
def predict(data: list):
    prediction = model.predict(np.array(data))
    return {"prediction": prediction.tolist()}
