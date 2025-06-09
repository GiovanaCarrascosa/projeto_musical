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

#--------------------------------------------------------------#

app.secret_key = "b$nana123linguic222"
# ------------------------------------------------------------------------------------------------------# 

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
def acessar_produto(codigo):
            codigo = int(codigo)
            #recuperar os produtos
            produto = Produtos.selecionar_produto(codigo)

            #recuperar as categorias
            categorias = Categoria.recuperar_categorias()

            #enviar os produtos pra o template
            return render_template("produtos.html", produto = produto, categorias = categorias)

# produtos da categoria 
@app.route("/produto/categoria/<codigo>")
def acessar_produto_categoria(codigo):
    #recuperar os produtos
            produtos = Produtos.selecionar_categoria(codigo)
            categoria_atual = None
            #recuperar as categorias
            categorias = Categoria.recuperar_categorias()
            codigo = int(codigo)

            for categoria in categorias:
                 if categoria["cod_categoria"] == codigo:
                      categoria_atual = categoria["nome"]

            #enviar os produtos pra o template
            return render_template("produto-categoria.html", produtos = produtos, categorias = categorias, categoria_atual = categoria_atual)


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

    # session["usuario"] = "banana"

    # usuario = request.form.get("usuario")

    # senha = request.form.get("senha")

    # esta_logado = Usuario.logar_usuario(usuario, senha)

    # if esta_logado:
    #     return redirect("/")
    
    # else:
    #     return redirect("/pagina/login") 
    
    usuario = request.form.get("usuario")
    senha = request.form.get("senha")

    esta_logado = Usuario.logar_usuario(usuario, senha)

    if esta_logado:
        session["usuario_id"] = esta_logado.get("id_usuario") 
        session["usuario"] = esta_logado.get("usuario") 
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
    session.clear()
    return redirect ("/")

# rotas do carrinho

# acessar a pagina do carrinho
@app.route("/pagina/carrinho")
def pagina_carrinho():
    itens_carrinho = []
    if "usuario_id" in session:
        usuario_id = session["usuario_id"]
        itens_carrinho = Carrinho.recuperar_itens_carrinho(usuario_id)

    # Recuperar as categorias para o header
    categorias = Categoria.recuperar_categorias()

    return render_template("carrinho.html", itens_carrinho=itens_carrinho, categorias=categorias)

# adicionar item no carrinho
@app.route("/post/carrinho/adicionar", methods=["POST"])
def adicionar_produto():
    # codigo = int(codigo)
    #recuperar os produtos
    # produto = Produtos.selecionar_produto(codigo)

    #recuperar as categorias
    # carrinhos = Carrinho.recuperar_itens_carrinho()

            #enviar os produtos pra o template
    # return render_template("produtos.html", produto = produto, carrinho = carrinhos)

    if "usuario_id" not in session:
        return redirect("/pagina/login") # Redireciona para login se não estiver logado

    cod_produto = request.form.get("cod_produto")
    usuario_id = session["usuario_id"]

    print(f"DEBUG CARRINHO: Antes de adicionar: cod_produto={cod_produto}, usuario_id={usuario_id} (Tipo: {type(usuario_id)})")
    if cod_produto:
        Carrinho.adicionar_produto_carrinho(usuario_id, int(cod_produto))

    return redirect("/pagina/carrinho") # Redireciona para o carrinho após adicionar

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