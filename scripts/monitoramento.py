# monitoramento.py - Módulo responsável pelas funcionalidades de monitoramento da lavoura
import numpy as np
import cv2
import scipy.ndimage as ndimage

def carregar_imagem_multiespectral(caminho_imagem=None):
    """
    Carrega uma imagem multiespectral, onde cada banda espectral é uma camada separada.
    Caso nenhum caminho seja fornecido, uma imagem simulada é gerada.
    :param caminho_imagem: Caminho da imagem multiespectral (ex: TIFF)
    :return: Array NumPy contendo as diferentes bandas espectrais
    """
    if caminho_imagem:
        imagem = cv2.imread(caminho_imagem, cv2.IMREAD_UNCHANGED)
        if imagem is None:
            raise FileNotFoundError(f"Não foi possível encontrar a imagem no caminho especificado: {caminho_imagem}")
        return imagem
    else:
        # Gera uma imagem multiespectral simulada com 4 bandas
        return np.random.rand(100, 100, 4) * 255


def calcular_ndvi(banda_nir, banda_vermelha):
    """
    Calcula o Índice de Vegetação por Diferença Normalizada (NDVI).
    :param banda_nir: Array contendo os valores da banda NIR (infravermelho próximo)
    :param banda_vermelha: Array contendo os valores da banda vermelha
    :return: Array contendo os valores de NDVI
    """
    # Evitar divisão por zero
    banda_nir = banda_nir.astype(float)
    banda_vermelha = banda_vermelha.astype(float)
    ndvi = (banda_nir - banda_vermelha) / (banda_nir + banda_vermelha + 1e-10)
    return ndvi


def detectar_problemas(ndvi, limiar=0.3):
    """
    Detecta áreas problemáticas com base no valor do NDVI.
    :param ndvi: Array contendo os valores de NDVI
    :param limiar: Limiar para detecção de áreas problemáticas
    :return: Máscara binária indicando áreas problemáticas
    """
    return ndvi < limiar


def detectar_problemas_avancado(ndvi, limiar=0.3, tamanho_minimo=5):
    """
    Detecta áreas problemáticas com uma análise avançada que considera o tamanho mínimo da área.
    :param ndvi: Array contendo os valores de NDVI
    :param limiar: Limiar para detecção de áreas problemáticas
    :param tamanho_minimo: Tamanho mínimo da área problemática para ser considerada
    :return: Máscara binária indicando áreas problemáticas
    """
    problemas = detectar_problemas(ndvi, limiar)
    problemas_rotulados, num_features = ndimage.label(problemas)
    tamanhos = ndimage.sum(problemas, problemas_rotulados, range(num_features + 1))
    mascara_areas_grandes = tamanhos >= tamanho_minimo
    return mascara_areas_grandes[problemas_rotulados]


def identificar_pragas(ndvi, banda_verde, banda_azul, limiar_ndvi=0.3, limiar_cor=50):
    """
    Identifica possíveis pragas com base no NDVI e nos valores das bandas verde e azul.
    :param ndvi: Array contendo os valores de NDVI
    :param banda_verde: Array contendo os valores da banda verde
    :param banda_azul: Array contendo os valores da banda azul
    :param limiar_ndvi: Limiar de NDVI para indicar vegetação problemática
    :param limiar_cor: Limiar de cor para identificar possíveis pragas
    :return: Máscara binária indicando áreas com possível presença de pragas
    """
    pragas = (ndvi < limiar_ndvi) & (banda_verde > limiar_cor) & (banda_azul > limiar_cor)
    return pragas
