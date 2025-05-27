from data.conexao import Conexao
import datetime

class Produtos:
    # recuperando os produtos cadastrados para inserir no site
    def recuperar_produtos():
        #criando a conexao
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary = True) 
        
        sql = """select cod_produto,
                titulo,
                descricao,
                preco,
                cod_categoria from tb_produtos;"""

        
        #executando o comando sql
        cursor.execute(sql)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado

    # selecionando um produto
    def selecionar_produto():
        pass

    # selecionando os produtos da categoria cd/vinil
    def selecionar_categoria_cd():
        pass

    # selecionando os produtos da categoria camiseta
    def selecionar_categoria_camiseta():
        pass

    # selecionando os produtos da categoria acessorio
    def selecionar_categoria_acessorio():
        pass