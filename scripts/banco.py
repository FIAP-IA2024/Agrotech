import sys
import cx_Oracle
import numpy as np
import traceback
import pandas as pd

def ler_arquivo_conexao():
    """
    Lê os parâmetros de conexão a partir do arquivo 'conexao.txt'.
    :return: Um dicionário com os parâmetros de conexão
    """
    parametros = {}
    try:
        with open('conexao.txt', 'r') as arquivo:
            for linha in arquivo:
                chave, valor = linha.strip().split('=')
                parametros[chave.strip()] = valor.strip()
        return parametros
    except FileNotFoundError:
        print("Erro: O arquivo 'conexao.txt' não foi encontrado.")
        sys.exit(1)
    except Exception as e:
        print(f"Erro ao ler o arquivo 'conexao.txt': {e}")
        traceback.print_exc()
        sys.exit(1)

def conectar_banco():
    """
    Conecta ao banco de dados Oracle utilizando parâmetros do arquivo 'conexao.txt'.
    :return: Conexão ativa ao banco de dados
    """
    try:
        parametros = ler_arquivo_conexao()
        dsn_tns = cx_Oracle.makedsn(parametros['host'], parametros['porta'], service_name=parametros['sid'])
        conexao = cx_Oracle.connect(user=parametros['usuario'], password=parametros['senha'], dsn=dsn_tns)
        return conexao
    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        traceback.print_exc()
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
    Além disso, armazena os dados em estruturas de dados Python: lista, tupla, dicionário e tabela de memória (DataFrame do pandas).
    
    :param conexao: Conexão ativa ao banco de dados
    :param ndvi: Array contendo os valores de NDVI
    :param problemas: Máscara binária indicando áreas problemáticas
    :param pragas: Máscara binária indicando possíveis áreas com pragas
    """
    try:
        cursor = conexao.cursor()

        # Verifica se a tabela existe e a cria se necessário
        verificar_e_criar_tabela(cursor)
        
        # Calcula os valores a serem inseridos
        ndvi_medio = float(np.mean(ndvi))
        problemas_totais = int(np.sum(problemas))
        pragas_totais = int(np.sum(pragas))
        
        # Inserção de dados na tabela 'monitoramento'
        cursor.execute("""
            INSERT INTO monitoramento (ndvi_medio, problemas_totais, pragas_totais)
            VALUES (:1, :2, :3)
        """, (ndvi_medio, problemas_totais, pragas_totais))
        
        conexao.commit()
        print("Dados salvos no banco de dados com sucesso.")
        
        # --- Criação de Estruturas de Dados ---
        
        # 1. Lista
        dados_lista = [ndvi_medio, problemas_totais, pragas_totais]
        print(f"Dados armazenados em lista: {dados_lista}")
        
        # 2. Tupla
        dados_tupla = (ndvi_medio, problemas_totais, pragas_totais)
        print(f"Dados armazenados em tupla: {dados_tupla}")
        
        # 3. Dicionário
        dados_dicionario = {
            'ndvi_medio': ndvi_medio,
            'problemas_totais': problemas_totais,
            'pragas_totais': pragas_totais
        }
        print(f"Dados armazenados em dicionário: {dados_dicionario}")
        
        # 4. Tabela de Memória (DataFrame do pandas)
        dados_dataframe = pd.DataFrame([dados_dicionario])
        print("Dados armazenados em tabela de memória (DataFrame):")
        print(dados_dataframe)
        
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

def main():
    """
    Função principal para testar a conexão e salvar dados de exemplo.
    """
    testar_conexao_banco()
    
    # Dados de exemplo
    ndvi = np.array([0.2, 0.3, 0.5, 0.4, 0.6])
    problemas = np.array([0, 1, 0, 1, 0])
    pragas = np.array([1, 0, 0, 1, 1])
    
    try:
        conexao = conectar_banco()
        salvar_dados_banco(conexao, ndvi, problemas, pragas)
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
    finally:
        if 'conexao' in locals() and conexao:
            conexao.close()

if __name__ == "__main__":
    main()