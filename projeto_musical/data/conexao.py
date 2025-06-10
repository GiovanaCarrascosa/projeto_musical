import mysql.connector

class Conexao: 

    def criar_conexao():

            # conexao = mysql.connector.connect(
            #     host="bdmusicalizando-musicalizando.j.aivencloud.com",
            #     port= 28927,
            #     user="avnadmin",
            #     password="AVNS_qqBT8-vioTzb14zwf3o",
            #     database = "defaultdb"
            #     )
            
            conexao = mysql.connector.connect(
                host="localhost",
                port= 3306,
                user="root",
                password="root",
                database = "db_musicalizando"
                )
            return conexao