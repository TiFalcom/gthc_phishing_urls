#Vou fazer um get na raiz com hello world
#Vou fazer uma api para fazer get e testar em notebook
#Vou mostrar o caso com uma home page onde é possível obter o score


from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import os
import pandas as pd

app = FastAPI()

class Payload(BaseModel):
    url : str

class Score(BaseModel):
    score : float

model = pickle.load(open(os.path.join('models', 'pipeline-model.pkl'), 'rb'))

def predict(payload):
    payload = pd.DataFrame([payload.model_dump()])
    score = round(model.predict_proba(payload)[:,1][0]*1000,0)
    return score

@app.get("/api/v1/predict", response_model=Score, status_code=200)
def get_prediction(payload : Payload):
    
    score = predict(payload)

    return {'score' : score}