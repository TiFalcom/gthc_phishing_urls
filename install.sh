python -m venv venv;
. venv/Scripts/activate;
pip install -r requirements.txt;
pre-commit install;
ipython kernel install --user --name=venv;