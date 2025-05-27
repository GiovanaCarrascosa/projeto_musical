from data.conexao import Conexao
import datetime

class Categoria:
    # recupera os comentarios registrados anteriormente
    def recuperar_categorias():
        #criando a conexao
        
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary = True) 
        
        sql = """select nome from tb_categorias;"""

        
        #executando o comando sql
        cursor.execute(sql)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado