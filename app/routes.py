from app import app
from flask import render_template, request, flash, redirect, make_response
from werkzeug.utils import redirect

@app.route("/")
def homepage():
    return "Opa, e aí!"

@app.route("/criar_cookie")
def criar_cookie():
    resposta = make_response("Criei um Cookie!")
    resposta.set_cookie("nome_usuario", "Camie")
    resposta.set_cookie("gosta", "calopsitas")
    return resposta 

@app.route("/ver_cookie")
def ver_cookie():
    cookies = request.cookies # "request.cookies" aloca os cookies na variável "cookies"
    #nome_usuario = cookies["nome_usuario"]
    #nome_usuario = cookies.get("nome_usuario")
    return cookies

@app.route("/index", defaults={"nome":"Psita", "profissao":"programador", "canal":"PsitaDev"})
@app.route("/index/<nome>/<profissao>/<canal>")
def index(nome,profissao,canal):
    dados = {"profissao": profissao, "canal": canal}
    return render_template("index.html", nome=nome, dados=dados)

@app.route("/page/<string:user>")
def page(user):
    return 'User: ' + user

# Query Strings (Strings de Consulta) é um conjunto de chaves e valores que são codificados na URL.
# O ponto de interrogação '?' inicia uma String de Consulta. Exemplo:
# https://www.google.com/search?q=query+string
# No caso acima, existe um "+" pois em URL não são permitidos barras de espaço, então normalmente é substituído por um sinal de '+' ou '%'.
# Cada argumento é separado por um &. Exemplo:
# http://127.0.0.1:5000/params?arg1=camie&arg2=psita

@app.route("/params")
def params(): # Não é necessário passar parâmetros dentro da função, pois os parâmetros já estão nas Strings de consulta
    args = request.args
    arg1 = ""
    arg2 = ""
    title = "default"

    for key, value in args.items():
        print(f"{key}:{value}")

    if "nome" in args:
        nome = args.get("nome")
        print(nome)

    if request.args: # Pra caso se você não saiba se a rota vai receber os parâmetros ou não
        arg1 = args.get("nome")
        arg2 = args["idade"]

        if "title" in args:
            title = request.args.get("title")

        print(title)
        print(arg1, arg2)

    #arg1 = request.args['arg1'] # .args é um dicionário com todos os parâmetros da Query String (String de Consulta)
    #arg2 = request.args['arg2']

    return "Argumento um: {} Argumento dois: {}".format(args, args)

@app.route('/query')
def query():
    if request.args:
        args = request.args
        serialized = ", ".join(f"{k}: {v}" for k, v in args.items())
        
        print(request.query_string)

        return f"(Query) {serialized}"
    
    else:
        return "Nenhuma Query foi recebida"

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