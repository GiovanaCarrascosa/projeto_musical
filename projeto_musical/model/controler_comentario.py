from data.conexao import Conexao
import datetime

class Comentario:
    # recupera os comentarios registrados anteriormente
    def recuperar_comentario_produto():
        #criando a conexao
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor(dictionary = True) #o dictionary é pra recuperar dados
       
        sql = """select nome as tb_usuarios.usuario,
                tb_comentario.comentario,
                tb_comentario.cod_comentario,
                tb_comentario.data_hora
                FROM tb_usuarios
            INNER JOIN tb_comentario
            ON tb_usuarios.id_usuario = tb_comentario.id_comentario;"""

       
        #executando o comando sql
        cursor.execute(sql)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall()
       
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado

    # adiciona um comentario no produto selecionado
    def adicionar_comentario_produto(usuario, comentario):
        data_hora = datetime.datetime.today()
       
        #criando a conexao
       
        conexao = Conexao.criar_conexao()
       
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o sql que sera executado
       
        sql = """INSERT INTO tb_usuarios.usuario,
                        tb_comentario.comentario,
                        tb_comentario.data_comentario
            FROM tb_usuarios
            INNER JOIN tb_comentario
            ON tb_usuarios.id_usuario = tb_comentario.id_comentario;
                   
                VALUES (
                    %s, %s, %s)"""
                   
        valores = (usuario, comentario, data_hora)
       
        #executando o comando sql
        cursor.execute(sql, valores)
       
        #confirmo a alteração
        conexao.commit()
       
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    # remove o comentario do produto
    def remover_comentario_produto(id_comentario):
        #criando a conexao
        conexao = Conexao.criar_conexao()

        cursor = conexao.cursor()
       
        sql = """delete from tb_comentario where id_comentario = %s;
        """

        valor = (id_comentario,) #coloca a , pra saber que é uma tupla
        #executando o comando sql
        cursor.execute(sql, valor)

        #comitando
        conexao.commit()
       
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()


