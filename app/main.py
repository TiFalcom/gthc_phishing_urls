from fastapi import FastAPI
import pickle
from pathlib import Path
import os

project_dir = Path('__main__').resolve().parent.parent

app = FastAPI()

clf = pickle.load(open(os.path.join(project_dir, 'models', 'model.pkl'), 'rb'))

@app.get("/")
def home():
    params = clf.get_params()
    return f"Minha api esta no ar!!!!\n{params}"