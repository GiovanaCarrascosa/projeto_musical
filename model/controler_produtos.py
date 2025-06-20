from data.conexao import Conexao
import datetime

class Produtos:
    # recuperando os produtos cadastrados para inserir no site
    def recuperar_produtos():
        #criando a conexao
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary = True) 
        
        # sql = """select cod_produto,
        #          titulo,
        #          descricao,
        #          preco,
        #          cod_categoria from tb_produtos;"""

        sql = """
            SELECT tb_produtos.cod_produto,
                   tb_produtos.titulo,
                   tb_produtos.descricao,
                   tb_produtos.preco,
                   tb_produtos.cod_categoria,
                   tb_fotos_produto.url_foto
            FROM tb_produtos
            INNER JOIN tb_fotos_produto
            ON tb_produtos.cod_produto = tb_fotos_produto.cod_produto
            
            group by tb_produtos.cod_produto;
        """
        
        #executando o comando sql
        cursor.execute(sql)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall()
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado


    # selecionando um produto
    def selecionar_produto(codigo):
        #criando a conexao
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary = True) 

        sql = """
            SELECT tb_produtos.cod_produto,
                tb_produtos.titulo,
                tb_produtos.descricao,
                tb_produtos.preco,
                tb_produtos.cod_categoria
            FROM tb_produtos
            WHERE tb_produtos.cod_produto = %s;
        """

        valor = (codigo,)
        #executando o comando sql
        cursor.execute(sql, valor)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchone() 


        
        #fecho a conexao com o banco
        
        conexao.close()

        return resultado
    
       # selecionando um produto
    def selecionar_foto(codigo):
        #criando a conexao
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary = True) 

        sql = """
            SELECT url_foto, cod_produto from tb_fotos_produto where cod_produto = %s;
        """

        valor = (codigo,)
        #executando o comando sql
        cursor.execute(sql, valor)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall() 


        
        #fecho a conexao com o banco
        
        conexao.close()

        return resultado
    
    # recuperando a foto
    def selecionar_foto(codigo):
        #criando a conexao
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary = True) 

        sql = """
            SELECT url_foto, cod_produto from tb_fotos_produto where cod_produto = %s;
        """

        valor = (codigo,)
        #executando o comando sql
        cursor.execute(sql, valor)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall() 


        
        #fecho a conexao com o banco
        
        conexao.close()

        return resultado




    # selecionando os produtos da categoria cd/vinil
    def selecionar_categoria(codigo):
        #criando a conexao
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary = True) 

        sql = """
            SELECT tb_produtos.cod_produto,
                   tb_produtos.titulo,
                   tb_produtos.descricao,
                   tb_produtos.preco,
                   tb_produtos.cod_categoria,
                   tb_fotos_produto.url_foto
            FROM tb_produtos
            INNER JOIN tb_fotos_produto
            ON tb_produtos.cod_produto = tb_fotos_produto.cod_produto
            WHERE tb_produtos.cod_categoria = %s

            group by tb_produtos.cod_produto;
        """
        
        valor = (codigo,)
        #executando o comando sql
        cursor.execute(sql, valor)

        #recuperando os dados e armazenando em uma variavel
        resultado = cursor.fetchall() 
        
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

        return resultado