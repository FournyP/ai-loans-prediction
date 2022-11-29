# -*- coding: utf-8 -*-

import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn
from pydantic import create_model

# Create the app
app = FastAPI()

# Load trained Pipeline
model = load_model("model_api")

# Create input/output pydantic models
input_model = create_model("model_api_input", **{'age': 42, 'job': 'technician', 'marital': 'married', 'education': 'secondary', 'default': 0, 'balance': 334, 'housing': 1, 'loan': 0})
output_model = create_model("model_api_output", Target_prediction='no')


# Define predict function
@app.post("/predict", response_model=output_model)
def predict(data: input_model):
    data = pd.DataFrame([data.dict()])
    predictions = predict_model(model, data=data)
    return {"Target_prediction": predictions["prediction_label"].iloc[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
