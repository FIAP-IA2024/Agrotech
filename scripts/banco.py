import sys
import cx_Oracle
import numpy as np
import traceback

def conectar_banco():
    """
    Conecta ao banco de dados Oracle.
    :return: Conexão ativa ao banco de dados
    """
    try:
        dsn_tns = cx_Oracle.makedsn('oracle.fiap.com.br', '1521', service_name='ORCL')
        conexao = cx_Oracle.connect(user="RM559800", password="010285", dsn=dsn_tns)
        return conexao
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        traceback.print_exc()  # Mostra o rastreamento completo do erro
        sys.exit(1)

def verificar_e_criar_tabela(cursor):
    """
    Verifica se a tabela 'monitoramento' existe e, caso contrário, cria a tabela no banco de dados Oracle.
    """
    try:
        # Verifica se a tabela existe no esquema atual
        cursor.execute("""
            SELECT table_name 
            FROM user_tables 
            WHERE table_name = 'MONITORAMENTO'
        """)
        tabela_existe = cursor.fetchone()
        
        if tabela_existe is None:
            # A tabela não existe, então cria a tabela
            cursor.execute("""
                CREATE TABLE monitoramento (
                    ndvi_medio FLOAT,
                    problemas_totais INT,
                    pragas_totais INT
                )
            """)
            print("Tabela 'monitoramento' criada com sucesso.")
        else:
            print("Tabela 'monitoramento' já existe.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao verificar/criar a tabela 'monitoramento': {e}")
        traceback.print_exc()
        raise

def salvar_dados_banco(conexao, ndvi, problemas, pragas):
    """
    Salva os dados de monitoramento da lavoura no banco de dados Oracle.
    :param conexao: Conexão ativa ao banco de dados
    :param ndvi: Array contendo os valores de NDVI
    :param problemas: Máscara binária indicando áreas problemáticas
    :param pragas: Máscara binária indicando possíveis áreas com pragas
    """
    try:
        cursor = conexao.cursor()

        # Verifica se a tabela existe e a cria se necessário
        verificar_e_criar_tabela(cursor)
        
        # Inserção de dados na tabela 'monitoramento'
        cursor.execute("""
            INSERT INTO monitoramento (ndvi_medio, problemas_totais, pragas_totais)
            VALUES (:1, :2, :3)
        """, (float(np.mean(ndvi)), int(np.sum(problemas)), int(np.sum(pragas))))
        
        conexao.commit()
        print("Dados salvos no banco de dados com sucesso.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao salvar os dados no banco de dados Oracle: {e}")
        traceback.print_exc()
    finally:
        cursor.close()

def testar_conexao_banco():
    """
    Testa a conexão com o banco de dados Oracle, realizando uma consulta simples.
    """
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT 1 FROM dual")
        resultado = cursor.fetchone()
        if resultado:
            print("Conexão com o banco de dados Oracle testada com sucesso.")
        cursor.close()
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao testar a conexão com o banco de dados Oracle: {e}")
        traceback.print_exc()
    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()