# banco.py - Módulo responsável pela conexão e operações com o banco de dados Oracle
import cx_Oracle
import numpy as np

def conectar_banco():
    """
    Conecta ao banco de dados Oracle.
    :return: Conexão ativa ao banco de dados
    """
    try:
        dsn_tns = cx_Oracle.makedsn('host', 'port', service_name='service_name')
        conexao = cx_Oracle.connect(user='usuario', password='senha', dsn=dsn_tns)
        return conexao
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        exit()

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
        # Exemplo de inserção de dados na tabela "monitoramento"
        cursor.execute("""
            INSERT INTO monitoramento (ndvi_medio, problemas_totais, pragas_totais)
            VALUES (:1, :2, :3)
        """, (float(np.mean(ndvi)), int(np.sum(problemas)), int(np.sum(pragas))))
        conexao.commit()
        print("Dados salvos no banco de dados com sucesso.")
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao salvar os dados no banco de dados Oracle: {e}")
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
    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()
