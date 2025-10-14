from app import app
from flask import render_template


@app.route('/') #raiz do projeto
@app.route('/index') #rota alternativa
def index():
    nome = "Alanna"
    dados = {"profissao": "Analista de Risco", "Linkedin": "Alanna Santos"}
    return render_template('index.html', nome=nome, dados=dados)

@app.route('/contato')
def contato():
    return render_template('contato.html')
    