import pandas as pd
import mysql.connector
from mysql.connector import Error


def conectar_mysql():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='bancos',
            user='root',
            password=''
        )
        if connection.is_connected():
            print("Conexão ao MySQL estabelecida.")
            return connection
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None


def inserir_dados(connection, tabela, dados):
    cursor = connection.cursor()
    for _, linha in dados.iterrows():
        try:
            query = f"INSERT INTO {tabela} (codigo_de_compensacao, nome_da_instituicao) VALUES (%s, %s)"
            cursor.execute(query, tuple(linha))
            connection.commit()
        except Error as e:
            print(f"Erro ao inserir dados: {e}")
            connection.rollback()
    cursor.close()


dados_excel = pd.read_excel('./bancos.xls')


conexao = conectar_mysql()

if conexao:
    tabela_mysql = 'banco'

    inserir_dados(conexao, tabela_mysql, dados_excel)

    
    conexao.close()
