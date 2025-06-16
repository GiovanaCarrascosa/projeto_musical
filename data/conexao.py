import mysql.connector

class Conexao: 

    def criar_conexao():

            conexao = mysql.connector.connect(
                host="localhost",
                port= 3306,
                user="root",
                password="root",
                database = "db_musicalizando"
                )

            # conexao = mysql.connector.connect(
            #     host="db-musicalizando-giovana-musicalizando-giovana.j.aivencloud.com",
            #     port= 17765,    
            #     user="avnadmin",
            #     password="AVNS_8ClJjgr5BH5-nTryTM_",
            #     database = "db_musicalizando"
            #     )
             
            return conexao