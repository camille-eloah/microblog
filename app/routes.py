from app import app
from flask import render_template, request, flash
from werkzeug.utils import redirect

@app.route("/")
@app.route("/index", defaults={"nome":"Psita"})
@app.route("/index/<nome>/<profissao>/<canal>")
def index(nome,profissao,canal):
    dados = {"profissao": profissao, "canal": canal}
    return render_template("index.html", nome=nome, dados=dados)

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/autenticar", methods=['POST'])
def autenticar():
    user = request.form.get("user")
    password = request.form.get("password")
    if user == "admin" and password == "senha123":
        return "usuario: {} e senha {}".format(user, password)
    else: 
        flash("Dados inválidos!")
        flash("Login ou senha inválidos!")
        return redirect('/login')