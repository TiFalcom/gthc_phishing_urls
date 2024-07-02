from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import json
import pickle
from pathlib import Path
from pydantic import BaseModel
import os
import pandas as pd

app = FastAPI()

templates = Jinja2Templates(directory=os.path.join("app", "templates"))

class ClasseURL(BaseModel):
    url : str
    

class ClasseScore(BaseModel):
    score : float


model = pickle.load(open('app/models/pipeline-model.pkl', 'rb'))


def predict(classe_url):
    url = pd.DataFrame([classe_url.model_dump()])
    score = round(model.predict_proba(url)[:,1][0]*1000, 0)
    return score



@app.get("/")
def get_home(request : Request):
    return templates.TemplateResponse("index.html", {"request" : request})


@app.post("/")
def post_home(request : Request, url : str = Form(...)):
    payload = ClasseURL(url=url)
    score = predict(payload)

    return templates.TemplateResponse("index_scored.html", {"request" : request, "url" : payload.url, "score" : score})



@app.post('/e_phishing', response_model=ClasseScore)
def get_prediction(classe_url : ClasseURL):
    score = predict(classe_url)
    return {"score" : score}



@app.get("/ola_mundo")
def home():
    return {"Ola Mundo!" : "Minha primeira aplicacao"}