# util.py - Módulo responsável por utilidades gerais, como manipulação de arquivos JSON e TXT
import json


def salvar_dados_json(dados, nome_arquivo):
    """
    Salva os dados em um arquivo JSON.
    :param dados: Dicionário contendo os dados a serem salvos
    :param nome_arquivo: Nome do arquivo JSON
    """
    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'
    with open(nome_arquivo, 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
    print(f"Dados salvos em {nome_arquivo} com sucesso.")


def ler_dados_json(nome_arquivo):
    """
    Lê dados de um arquivo JSON.
    :param nome_arquivo: Nome do arquivo JSON
    :return: Dicionário contendo os dados lidos
    """
    if not nome_arquivo.endswith('.json'):
        nome_arquivo += '.json'
    with open(nome_arquivo, 'r') as arquivo:
        dados = json.load(arquivo)
    return dados


def atualizar_dados_json(dados_atualizados, nome_arquivo):
    """
    Atualiza os dados em um arquivo JSON.
    :param dados_atualizados: Dicionário contendo os novos dados
    :param nome_arquivo: Nome do arquivo JSON
    """
    dados_existentes = ler_dados_json(nome_arquivo)
    dados_existentes.update(dados_atualizados)
    salvar_dados_json(dados_existentes, nome_arquivo)


def salvar_relatorio_texto(relatorio, nome_arquivo):
    """
    Salva o relatório em um arquivo de texto.
    :param relatorio: Texto do relatório a ser salvo
    :param nome_arquivo: Nome do arquivo TXT
    """
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(relatorio)
    print(f"Relatório salvo em {nome_arquivo} com sucesso.")


def ler_relatorio_texto(nome_arquivo):
    """
    Lê o conteúdo de um arquivo de texto.
    :param nome_arquivo: Nome do arquivo TXT
    :return: Conteúdo do arquivo como string
    """
    if not nome_arquivo.endswith('.txt'):
        nome_arquivo += '.txt'
    with open(nome_arquivo, 'r') as arquivo:
        return arquivo.read()


def manipular_arquivos_txt():
    """
    Função de exemplo para manipulação de arquivos TXT.
    Permite ler, salvar e atualizar arquivos de texto.
    """
    while True:
        print("\nMenu de Manipulação de Arquivos TXT:\n")
        print("1. Ler arquivo TXT")
        print("2. Salvar novo relatório TXT")
        print("3. Atualizar relatório TXT")
        print("4. Voltar ao menu principal")

        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            nome_arquivo = input("Digite o nome do arquivo TXT: ").strip()
            try:
                conteudo = ler_relatorio_texto(nome_arquivo)
                print(f"Conteúdo do arquivo {nome_arquivo}:")
                print(conteudo)
            except FileNotFoundError:
                print("Arquivo não encontrado.")

        elif escolha == '2':
            nome_arquivo = input("Digite o nome do arquivo TXT para salvar: ").strip()
            relatorio = input("Digite o conteúdo do relatório: ").strip()
            salvar_relatorio_texto(relatorio, nome_arquivo)

        elif escolha == '3':
            nome_arquivo = input("Digite o nome do arquivo TXT para atualizar: ").strip()
            conteudo_adicional = input("Digite o conteúdo adicional: ").strip()
            conteudo_existente = ler_relatorio_texto(nome_arquivo)
            conteudo_atualizado = conteudo_existente + "\n" + conteudo_adicional
            salvar_relatorio_texto(conteudo_atualizado, nome_arquivo)

        elif escolha == '4':
            break

        else:
            print("Opção inválida. Tente novamente.")
