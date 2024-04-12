import pandas as pd
import mysql.connector
from mysql.connector import Error

# Função para conectar ao banco de dados MySQL
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

# Função para inserir dados no banco de dados MySQL
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

# Lendo dados do arquivo Excel
dados_excel = pd.read_excel('./bancos.xls')

# Conectando ao banco de dados MySQL
conexao = conectar_mysql()

if conexao:
    # Nome da tabela no banco de dados
    tabela_mysql = 'bancos_banco'

    # Inserindo os dados no banco de dados MySQL
    inserir_dados(conexao, tabela_mysql, dados_excel)

    # Fechando a conexão com o banco de dados
    conexao.close()
