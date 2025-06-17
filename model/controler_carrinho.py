from data.conexao import Conexao
class Carrinho:
    def adicionar_produto_carrinho(id_usuario, cod_produto):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor() 

        sql = """
            INSERT INTO tb_carrinho (id_usuario, cod_produto)
            VALUES (%s, %s);
        """
        valores = (id_usuario, cod_produto)
        
        cursor.execute(sql, valores)
        conexao.commit() 
        
        cursor.close()
        conexao.close()
        return True

    def recuperar_itens_carrinho(id_usuario):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor(dictionary=True) 

        sql = """
            SELECT 
                tb_carrinho.id_carrinho,
                tb_produtos.cod_produto,
                tb_produtos.titulo,
                tb_produtos.preco,
                tb_produtos.descricao
            FROM tb_carrinho
            JOIN tb_produtos ON tb_carrinho.cod_produto = tb_produtos.cod_produto
            WHERE tb_carrinho.id_usuario = %s;
        """
        valores = (id_usuario,)
        cursor.execute(sql, valores)
        resultado = cursor.fetchall()
        
        cursor.close()
        conexao.close()
        return resultado
    
   
    def remover_item_carrinho(id_carrinho):
        conexao = Conexao.criar_conexao()
        cursor = conexao.cursor()

        sql = "DELETE FROM tb_carrinho WHERE id_carrinho = %s;"
        cursor.execute(sql, (id_carrinho,))
        conexao.commit()
        
        cursor.close()
        conexao.close()
        return True 

