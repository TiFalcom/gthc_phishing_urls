from fastapi import FastAPI
import json
import pickle
from pathlib import Path
from pydantic import BaseModel
import os
import pandas as pd

project_dir = Path('__main__').resolve().parent.parent

app = FastAPI()

class Payload(BaseModel):
    url_length : float
    n_dots : float
    n_hypens : float
    n_underline : float
    n_slash : float
    n_questionmark : float
    n_equal : float
    n_at : float
    n_and : float
    n_exclamation : float
    n_space : float
    n_tilde : float
    n_comma : float
    n_plus : float
    n_asterisk : float
    n_hastag : float
    n_dollar : float
    n_percent : float
    n_redirection : float
    
class Score(BaseModel):
    score : int

clf = pickle.load(open(os.path.join(project_dir, 'models', 'model.pkl'), 'rb'))

@app.get("/")
def get_home():
    return "API ML Phishing URL"

@app.post("/predict", response_model=Score, status_code=200)
def get_prediction(payload : Payload):
    
    payload = pd.DataFrame([payload.dict()])
    score = round(clf.predict_proba(payload)[:,1][0]*1000,0)

    return {'score' : score}