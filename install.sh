python3.9 -m venv venv;
. venv/bin/activate;
pip install -r requirements.txt;
pre-commit install;
ipython3 kernel install --user --name=venv;