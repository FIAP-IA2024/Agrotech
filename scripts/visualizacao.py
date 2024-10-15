# visualizacao.py - Módulo responsável pela visualização dos dados, como a geração de mapas NDVI
import matplotlib.pyplot as plt
import numpy as np


def gerar_mapa_ndvi(ndvi):
    """
    Gera um mapa visual do NDVI para a área monitorada.
    :param ndvi: Array NumPy com os valores de NDVI
    """
    plt.imshow(ndvi, cmap='RdYlGn')
    plt.colorbar()
    plt.title("Mapa NDVI - Saúde da Vegetação")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.show()


def gerar_histograma_ndvi(ndvi):
    """
    Gera um histograma dos valores de NDVI para analisar a distribuição dos valores de saúde da vegetação.
    :param ndvi: Array NumPy com os valores de NDVI
    """
    plt.hist(ndvi.flatten(), bins=50, color='green', alpha=0.7)
    plt.title("Histograma dos Valores de NDVI")
    plt.xlabel("Valor de NDVI")
    plt.ylabel("Frequência")
    plt.grid(axis='y', linestyle='--')
    plt.show()


def plotar_imagem_multiespectral(imagem):
    """
    Plota uma imagem multiespectral, mostrando cada banda separadamente.
    :param imagem: Array NumPy contendo as diferentes bandas espectrais
    """
    num_bandas = imagem.shape[2]
    fig, axes = plt.subplots(1, num_bandas, figsize=(15, 5))
    fig.suptitle("Bandas Espectrais da Imagem Multiespectral")
    for i in range(num_bandas):
        axes[i].imshow(imagem[:, :, i], cmap='gray')
        axes[i].set_title(f"Banda {i + 1}")
        axes[i].axis('off')
    plt.show()


def plotar_areas_problemas(ndvi, problemas):
    """
    Plota o mapa do NDVI juntamente com as áreas problemáticas detectadas.
    :param ndvi: Array NumPy com os valores de NDVI
    :param problemas: Máscara binária indicando áreas problemáticas
    """
    plt.figure(figsize=(10, 6))
    plt.imshow(ndvi, cmap='RdYlGn', alpha=0.7)
    plt.imshow(problemas, cmap='Reds', alpha=0.4)
    plt.title("Mapa NDVI com Áreas Problemáticas")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.colorbar(label="NDVI")
    plt.show()
