# importar os arquivos e pastas
from flask import Flask, render_template, request, redirect, session
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


# rotas de produto ---------------------------------------------------------------------------------------------------

# carregar a pagina de produto
@app.route("/pagina/produto")
def paginna_produto():
    return render_template ("produtos.html")

# selecionar o produto
@app.route("/produto/<codigo>")
def acessar_produto(codigo):
            codigo = int(codigo)
            #recuperar os produtos
            produto = Produtos.selecionar_produto(codigo)

            lista_de_fotos = Produtos.selecionar_foto(codigo)
            print(f"DEBUG: Fotos para o produto {codigo}: {lista_de_fotos}")

            #recuperar as categorias
            categorias = Categoria.recuperar_categorias()

            # Recupera comentários do produto
            mensagens = Comentario.recuperar_comentario_produto(codigo)

            return render_template("produtos.html", produto=produto, categorias=categorias, mensagens=mensagens, fotos=lista_de_fotos)


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


# rotas do usuario ---------------------------------------------------------------------------------------------

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
    
    # agora pega o id do usuario tambem
    if esta_logado:
        session["id_usuario"] = esta_logado.get("id_usuario") 
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

    if Usuario.verificar_usuario_existente(usuario, email):
        return redirect("/pagina/cadastrar")

    else: 
        Usuario.cadastrar_usuario(usuario, email,  nome, endereco, telefone, senha)
    
        return redirect("/pagina/login")

# sair da conta
@app.route("/deslogar")
def sair_conta():
    session.clear()
    return redirect ("/")

# rotas do carrinho ----------------------------------------------------------------------------------

# acessar a pagina do carrinho
@app.route("/pagina/carrinho")
def pagina_carrinho():

    # Redireciona para a página de login se o usuario não estiver logado
    if "id_usuario" not in session:
        return redirect("/pagina/login") 

    # se o usuario estiver com a conta logada, pode acessar o carrinho
    if "id_usuario" in session:
        id_usuario = session["id_usuario"]
        itens_carrinho = Carrinho.recuperar_itens_carrinho(id_usuario)

    # Recuperar as categorias para o header
    categorias = Categoria.recuperar_categorias()

    return render_template("carrinho.html", itens_carrinho=itens_carrinho, categorias=categorias)

# adicionar item no carrinho
@app.route("/post/carrinho/adicionar", methods=["POST"])
def adicionar_produto():
    
    # Redireciona para a página de login se o usuario não estiver logado
    if "id_usuario" not in session:
        return redirect("/pagina/login") 

    cod_produto = request.form.get("cod_produto")
    id_usuario = session["id_usuario"]

    # se tiver o codigo do produto, ele é adicionado no carrinho
    if cod_produto:
        Carrinho.adicionar_produto_carrinho(id_usuario, int(cod_produto))

    return redirect(f"/produto/{cod_produto}") 

# remover item do carrinho
@app.route("/post/carrinho/remover/<id_carrinho>")
def remover_produto(id_carrinho):
    Carrinho.remover_item_carrinho(id_carrinho)
    return redirect("/pagina/carrinho")

# rotas de comentario ------------------------------------------------------------------------------------

# cadastrar comentario
@app.route("/post/comentario", methods = ["POST"])
def post_comentario():
    if "id_usuario" not in session:
        return redirect("/pagina/login") 
    
    id_usuario = session["id_usuario"]
    comentario = request.form.get("mensagem")
    cod_produto = request.form.get("cod_produto") 
    
     # Verifica se o produto foi encontrado e o comentário não está vazio
    if cod_produto and comentario:
        Comentario.adicionar_comentario_produto(id_usuario, int(cod_produto), comentario )
        return redirect(f"/produto/{cod_produto}")

# ------------------------------------------------------------------------------------------------------
# rodar o site
app.run(debug = True)