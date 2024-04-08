from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import json
import pickle
from pathlib import Path
from pydantic import BaseModel
import os
import pandas as pd

project_dir = Path('__main__').resolve().parent.parent

app = FastAPI()

templates = Jinja2Templates(directory="templates")

class Payload(BaseModel):
    url : str
    
class Score(BaseModel):
    score : int

model = pickle.load(open(os.path.join(project_dir, 'models', 'pipeline-model.pkl'), 'rb'))

@app.get("/")
def get_home(request : Request):
    return templates.TemplateResponse("index.html", {"request" : request})


def predict(payload):
    payload = pd.DataFrame([payload.model_dump()])
    score = round(model.predict_proba(payload)[:,1][0]*1000,0)
    return score


@app.post("/")
def post_home(request : Request, url : str = Form(...)):
    payload = Payload(url=url)
    score = predict(payload)

    return templates.TemplateResponse("index_scored.html", {"request" : request, "url" : payload.url, "score" : score})


@app.post("/predict", response_model=Score, status_code=200)
def get_prediction(payload : Payload):
    
    score = predict(payload)

    return {'score' : score}
