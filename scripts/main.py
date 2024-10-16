
# main.py - Programa principal que gerencia o fluxo do sistema de monitoramento da lavoura
import numpy as np
import cv2
import cx_Oracle
from monitoramento import carregar_imagem_multiespectral, calcular_ndvi, detectar_problemas, detectar_problemas_avancado, identificar_pragas
from banco import conectar_banco, salvar_dados_banco, testar_conexao_banco
from visualizacao import gerar_mapa_ndvi, gerar_histograma_ndvi, plotar_imagem_multiespectral, plotar_areas_problemas
from util import salvar_dados_json, atualizar_dados_json, ler_dados_json, salvar_relatorio_texto, manipular_arquivos_txt

def exibir_menu():
    """
    Exibe o menu principal do programa e solicita a escolha do usuário.
    """
    opcoes = [
        "Carregar imagem multiespectral",
        "Calcular NDVI",
        "Detectar áreas problemáticas",
        "Análise Avançada de Problemas da Lavoura",
        "Identificação Técnica de Pragas via Imagens Multiespectrais e RGB",
        "Salvar dados em JSON",
        "Conectar e salvar dados no banco de dados Oracle",
        "Gerar mapa NDVI",
        "Trabalhar com arquivos TXT",
        "Testar conexão com o banco de dados",
        "Sair"
    ]

    print("\nMenu Principal:\n")
    for i, opcao in enumerate(opcoes, 1):
        print(f"{i}. {opcao}")

    while True:
        try:
            escolha = int(input("Escolha uma opção: "))
            if 1 <= escolha <= len(opcoes):
                return escolha
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida. Digite um número.")

def main():
    """
    Função principal que gerencia o fluxo do programa.
    """
    imagem_multiespectral = None
    ndvi = None
    problemas = None
    problemas_avancado = None
    pragas = None

    while True:
        escolha = exibir_menu()

        if escolha == 1:
            caminho_imagem = input("Digite o caminho da imagem multiespectral (ou deixe vazio para usar imagem simulada): ")
            try:
                if caminho_imagem.strip() == "":
                    imagem_multiespectral = carregar_imagem_multiespectral()
                    salvar_imagem = input("Deseja salvar a imagem simulada? (s/n): ").strip().lower()
                    if salvar_imagem == 's':
                        cv2.imwrite('imagem_simulada.tif', imagem_multiespectral)
                else:
                    imagem_multiespectral = carregar_imagem_multiespectral(caminho_imagem)
                print("Imagem carregada com sucesso.")
                plotar_imagem_multiespectral(imagem_multiespectral)
            except FileNotFoundError as e:
                print(e)

        elif escolha == 2:
            if imagem_multiespectral is not None:
                banda_nir = imagem_multiespectral[:, :, 3]  # Supondo que a 4ª camada seja NIR
                banda_vermelha = imagem_multiespectral[:, :, 2]  # Supondo que a 3ª camada seja Vermelha
                ndvi = calcular_ndvi(banda_nir, banda_vermelha)
                print("NDVI calculado com sucesso.")
                print(f"NDVI Médio: {np.mean(ndvi):.2f}")
                print(f"NDVI Mínimo: {np.min(ndvi):.2f}, NDVI Máximo: {np.max(ndvi):.2f}")
                gerar_histograma_ndvi(ndvi)
            else:
                print("Erro: Nenhuma imagem carregada. Carregue uma imagem primeiro.")

        elif escolha == 3:
            if ndvi is not None:
                problemas = detectar_problemas(ndvi, limiar=0.3)
                print("Detecção de áreas problemáticas concluída.")
                plotar_areas_problemas(ndvi, problemas)
            else:
                print("Erro: NDVI não calculado. Calcule o NDVI primeiro.")

        elif escolha == 4:
            if ndvi is not None:
                problemas_avancado = detectar_problemas_avancado(ndvi, limiar=0.3, tamanho_minimo=5)
                print("Análise avançada de problemas da lavoura concluída.")
                plotar_areas_problemas(ndvi, problemas_avancado)
            else:
                print("Erro: NDVI não calculado. Calcule o NDVI primeiro.")

        elif escolha == 5:
            if ndvi is not None:
                banda_verde = imagem_multiespectral[:, :, 1]  # Supondo que a 2ª camada seja Verde
                banda_azul = imagem_multiespectral[:, :, 0]  # Supondo que a 1ª camada seja Azul
                pragas = identificar_pragas(ndvi, banda_verde, banda_azul, limiar_ndvi=0.3, limiar_cor=50)
                print("Identificação técnica de possíveis pragas concluída.")
                plotar_areas_problemas(ndvi, pragas)
            else:
                print("Erro: NDVI não calculado. Calcule o NDVI primeiro.")

        elif escolha == 6:
            if ndvi is not None and (problemas is not None or problemas_avancado is not None or pragas is not None):
                dados_plantacao = {
                    "NDVI_Medio": float(np.mean(ndvi)),
                    "Problemas_Totais": int(np.sum(problemas if problemas_avancado is None else problemas_avancado)),
                    "Pragas_Totais": int(np.sum(pragas)) if pragas is not None else 0
                }
                nome_arquivo = input("Digite o nome do arquivo JSON para salvar os dados: ")
                salvar_dados_json(dados_plantacao, nome_arquivo)
            else:
                print("Erro: NDVI, problemas ou pragas não calculados. Calcule o NDVI primeiro.")

        elif escolha == 7:
            try:
                conexao = conectar_banco()
                salvar_dados_banco(conexao, ndvi, problemas, pragas)
            except cx_Oracle.DatabaseError as e:
                print("Erro ao conectar ao banco de dados:", e)

        elif escolha == 8:
            if ndvi is not None:
                gerar_mapa_ndvi(ndvi)
            else:
                print("Erro: NDVI não calculado. Calcule o NDVI primeiro.")

        elif escolha == 9:
            manipular_arquivos_txt()

        elif escolha == 10:
            testar_conexao_banco()

        elif escolha == 11:
            print("Saindo do programa.")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
