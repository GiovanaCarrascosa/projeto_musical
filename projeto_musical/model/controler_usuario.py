from hashlib import sha256
from data.conexao import Conexao
from flask import session

class Usuario:
    # cadastrando o usuario
    def cadastrar_usuario(usuario, email, nome, endereco, telefone, senha):

         #criptografando a senha

        senha = sha256(senha.encode()).hexdigest()

        
        #criptografando a senha

        senha = sha256(senha.encode()).hexdigest()


        #cadastrando as informações no banco de dados
            
        #criando a conexao
            
        conexao = Conexao.criar_conexao()
            
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor()

        #criando o sql que sera executado
            
        sql = """INSERT INTO tb_usuarios (

                        usuario, 
                        email,
                        nome_pessoa,
                        endereco,
                        telefone,
                        senha)
                        
                    VALUES (
                        %s, %s, %s,%s, %s, %s)"""

                        login, 
                        senha,
                        nome)
                        
                    VALUES (
                        %s, %s, %s)"""

                        
        valores = (usuario, email, nome, endereco, telefone, senha)
            
        #executando o comando sql
        cursor.execute(sql, valores)
            
        #confirmo a alteração
        conexao.commit()
            
        #fecho a conexao com o banco
        cursor.close()
        conexao.close()

    # logando o usuario 
    def logar_usuario(usuario, senha):
       #criptografando a senha

        senha = sha256(senha.encode()).hexdigest()
        #cadastrando as informações no banco de dados
            
        #criando a conexao
            
        conexao = Conexao.criar_conexao()
            
        #o cursor sera responsavel por manipular o banco de dados
        cursor = conexao.cursor(dictionary=True)

        #criando o sql que sera executado
            
        sql = """SELECT usuario from tb_usuarios
                WHERE usuario = %s and binary senha = %s; """
                        
        valores = (usuario, senha)
            
        #executando o comando sql
        cursor.execute(sql, valores)

        resultado = cursor.fetchone()

        conexao.close()
        cursor.close()

        if resultado:
            session["usuario"] = resultado['usuario']
            return True
        
        else:
            return False
    
    # deslogar a conta
    def logoff():
        session.clear()
            