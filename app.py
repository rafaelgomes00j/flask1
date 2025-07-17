# Introduçao ao flask - Framework Python para aplicaçao WEB
# Requisiçao WEB -> GET e POST 
# Insntalaçao do Flask -> pip install flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    # ENVIANDO VARIAVEIS PARA O HTML
    nome = 'Rafael'
    idade = 30
    gmail = "joao9969@gmail.com"
    return render_template('index.html', name = nome, idade = idade,
    gmail = gmail)


@app.route('/dicionarios')
def dicionarios():
    # ENVIANDO DICIONARIOS PARA O HTML 
    usuario = {
        "nome": "Rafael",
        "idade": 20,
        "gmail": "9434rafarafa@gmail.com"
    }
    return render_template ('dicionarios.html', usuario= usuario )

@app.route('/condicionais')
def condicionais():
    nota = 3
    Logado = True
    usuario = {
        "nome": "Rafael",
        "idade": 20,
        "gmail": "9434rafarafa@gmail.com"
    }
    return render_template ('condicionais.html',Logado= Logado,
    nota = nota, usuario = usuario)


@app.route('/listas')
def listas():
    listasUsuarios = ['Maria', 'Joao', 'Rafa']

    return render_template('listas.html', listasUsuarios= listasUsuarios)


if __name__ == '__main__':
    app.run(debug=True)