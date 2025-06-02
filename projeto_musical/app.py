# importar os arquivos e pastas
from flask import Flask, render_template, request, redirect, session, jsonify
import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_carrinho import Carrinho
from model.controler_produtos import Produtos
from model.controler_categorias import Categoria
from model.controler_usuario import Usuario
from model.controler_comentario import Comentario
app = Flask(__name__)
app.secret_key = "banana123"
# ------------------------------------------------------------------------------------------------------
# rotas

# pagina principal
@app.route("/")
def pagina_principal():

            #recuperar os produtos
            produtos = Produtos.recuperar_produtos()

            #recuperar as categorias
            categorias = Categoria.recuperar_categorias()

            #enviar os produtos pra o template
            return render_template("index.html", produtos = produtos, categorias = categorias)


# rotas de produto

# selecionar o produto
@app.route("/produto/<codigo>")
def acessar_produto():
    pass

# produtos da categoria cd/vinil
@app.route("/produto/categoria/cd")
def acessar_categoria_cd():
    pass

# produtos da categoria camiseta
@app.route("/produto/categoria/camiseta")
def acessar_categoria_camiseta():
    pass

# produtos da categoria acessorios
@app.route("/produto/categoria/acessorios")
def acessar_categoria_acessorios():
    pass

# rotas do usuario

# acessar a pagina de login
@app.route("/pagina/login")
def pagina_login():
    return render_template ("login.html")

# acessar a pagina de cadastro
@app.route("/pagina/cadastrar")
def pagina_cadastrar():
    return render_template ("cadastro.html")

# logar a conta
@app.route("/post/logar", methods = ["POST"])
def post_logar():
    usuario = request.form.get("usuario")

    senha = request.form.get("senha")

    esta_logado = Usuario.logar_usuario(usuario, senha)

    if esta_logado:
        return redirect("/")
    
    else:
        return redirect("/pagina/login") 

# se cadastrar
@app.route("/post/cadastro", methods = ["POST"])
def post_cadastro():
    usuario = request.form.get("cadastro-usuario")

    email = request.form.get("cadastro-email")
    
    nome = request.form.get("cadastro-nome")

    endereco = request.form.get("cadastro-endereco")

    telefone = request.form.get("cadastro-telefone")

    senha = request.form.get("cadastro-senha")

    Usuario.cadastrar_usuario(usuario, email,  nome, endereco, telefone, senha)
    
    return redirect("/pagina/login")

# sair da conta
@app.route("/deslogar")
def sair_conta():
    Usuario.logoff()
    return redirect ("/")

# rotas do carrinho

# acessar a pagina do carrinho
@app.route("/pagina/carrinho")
def pagina_carrinho():
    pass

# adicionar item no carrinho
@app.route("/post/carrinho/adicionar", methods=["POST"])
def adicionar_produto():
    pass

# remover item do carrinho
@app.route("/post/carrinho/remover", methods=["POST"])
def remover_produto():
    pass

# rotas de comentario

# cadastrar comentario
@app.route("/post/comentario", methods = ["POST"])
def post_mensagem():
    pass

# remover comentario
@app.route("/delete/comentario/<codigo>")
def delete_mensagem(codigo):
    pass
# ------------------------------------------------------------------------------------------------------
# rodar o site
app.run(debug = True)