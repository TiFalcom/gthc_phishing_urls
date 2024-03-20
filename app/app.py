from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        campo_preenchido = request.form['campo_preenchido']

        return render_template('index.html', campo_preenchido=campo_preenchido)
    return render_template('index.html')
