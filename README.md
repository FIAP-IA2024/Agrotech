# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## IATron

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/hen-sarmento?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Henrique Sarmento</a>
- <a href="https://www.linkedin.com/in/edimilson-ribeiro/">Edimilson Ribeiro</a>
- <a href="https://www.linkedin.com/in/jacorrea"> Junior Correa</a> 
- <a href="https://www.linkedin.com/in/jonas-felipe-dos-santos-lima-b2346811b?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app">Jonas Felipe</a> 
- <a href="https://www.linkedin.com/in/jordanna-mar%C3%A7al-b94b57121/">Jordanna Marçal</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/in/lucas-gomes-moreira-15a8452a/">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/in/profandregodoi/">André Godoi</a>


## 📜 Descrição

 Sistema de Monitoramento de Lavoura - README

Este é um aplicativo para monitoramento e análise de lavouras usando imagens multiespectrais e índices de vegetação. Ele utiliza imagens multiespectrais para calcular o Índice de Vegetação por Diferença Normalizada (NDVI), detectar áreas problemáticas, identificar pragas e gerar relatórios detalhados. O aplicativo possui integração com bancos de dados Oracle para armazenamento dos dados obtidos, além de gerar visualizações gráficas dos resultados.

 Estrutura do Aplicativo

O sistema é dividido em diversos módulos que desempenham funções específicas:

- main.py: Programa principal que gerencia o fluxo da aplicação e apresenta o menu interativo ao usuário.
- monitoramento.py: Contém as funções responsáveis pela análise das imagens multiespectrais e cálculo do NDVI, além de detectar áreas problemáticas e pragas.
- banco.py: Contém funções para conectar ao banco de dados Oracle e armazenar os dados da lavoura.
- util.py: Funções utilitárias para manipulação de arquivos JSON e TXT.
- visualizacao.py: Contém funções para gerar visualizações dos dados, como mapas NDVI e histogramas.

 Funcionalidades do Aplicativo

 1. Carregar Imagem Multiespectral

Carrega uma imagem multiespectral para ser usada no monitoramento da lavoura. Se um caminho não for especificado, uma imagem simulada é gerada para testes. O usuário também pode optar por salvar a imagem simulada.

- Output: Exibe a imagem carregada, mostrando cada banda espectral separadamente.

 2. Calcular NDVI

Calcula o Índice de Vegetação por Diferença Normalizada (NDVI) com base nas bandas infravermelha (NIR) e vermelha da imagem multiespectral.

- Output: NDVI calculado com sucesso, valores mínimo, médio e máximo do NDVI, e histograma dos valores de NDVI.

 3. Detectar Áreas Problemáticas

Detecta áreas problemáticas da lavoura com base em um limiar de NDVI, identificando regiões de estresse ou com baixa vegetação.

- Output: Exibe um mapa do NDVI juntamente com as áreas problemáticas detectadas.

 4. Análise Avançada de Problemas da Lavoura

Realiza uma análise avançada para detectar áreas problemáticas levando em consideração um tamanho mínimo das áreas de interesse.

- Output: Exibe o mapa NDVI juntamente com as áreas problemáticas, considerando o tamanho mínimo especificado.

 5. Identificação de Pragas

Identifica possíveis pragas nas áreas da lavoura usando os valores das bandas verde e azul, além do NDVI calculado.

- Output: Exibe um mapa mostrando áreas com possíveis pragas.

 6. Salvar Dados em JSON

Salva os dados da lavoura (NDVI médio, áreas problemáticas e pragas) em um arquivo JSON especificado pelo usuário.

- Output: Mensagem de confirmação de que os dados foram salvos em JSON.

 7. Conectar e Salvar Dados no Banco de Dados Oracle

Conecta ao banco de dados Oracle e salva os dados da lavoura na tabela apropriada.

- Output: Mensagem de confirmação de que os dados foram salvos com sucesso ou mensagem de erro ao tentar conectar ao banco.

 8. Gerar Mapa NDVI

Gera uma visualização gráfica do NDVI para a área monitorada, mostrando a saúde da vegetação.

- Output: Mapa do NDVI, com uma barra de cores para indicar a saúde da vegetação.

 9. Trabalhar com Arquivos TXT

Permite ao usuário manipular relatórios em formato TXT, incluindo leitura, salvamento e atualização dos relatórios.

- Output: Mensagens de confirmação das operações com arquivos TXT.

 10. Testar Conexão com o Banco de Dados

Testa a conexão com o banco de dados Oracle, realizando uma consulta simples para verificar a disponibilidade.

- Output: Mensagem de confirmação da conexão ou erro ao tentar conectar.

 Orientação para Interpretação dos Outputs

- Imagem Multiespectral: Cada banda representa uma faixa espectral diferente. Isso é útil para análises específicas, como identificar saúde da vegetação e pragas.

- NDVI: O NDVI varia entre -1 e 1. Valores próximos a 1 indicam vegetação saudável, enquanto valores baixos (ou negativos) indicam áreas de estresse ou sem vegetação. O histograma dos valores de NDVI ajuda a visualizar a distribuição da saúde da vegetação em toda a lavoura.

- Áreas Problemáticas: As áreas em vermelho nos mapas representam regiões onde a vegetação está em estresse, ou onde a produção está abaixo do esperado. Essas áreas precisam de atenção especial, como irrigação ou controle de pragas.

- Pragas: Áreas indicadas como possíveis pragas são mostradas em um mapa, com base nas características espectrais e valores baixos de NDVI. Isso permite ao usuário tomar ações direcionadas, como aplicação de pesticidas.

- Banco de Dados: A confirmação da inserção dos dados no banco de dados Oracle indica que todas as análises foram salvas para consulta futura, permitindo comparações e análises de longo prazo.

- Manipulação de Arquivos JSON/TXT: Os relatórios em JSON e TXT são úteis para armazenar resultados de análises e gerar documentos que podem ser usados por outros sistemas ou para relatórios manuais.

 Requisitos do Sistema

- Python 3.6+
- Bibliotecas Python: `numpy`, `opencv-python`, `matplotlib`, `cx_Oracle` ou `oracledb`, `scipy`
- Oracle Instant Client: Necessário para conexão ao banco de dados Oracle

 Instruções de Uso

1. Certifique-se de que todas as bibliotecas estão instaladas.
2. Configure o Oracle Instant Client se desejar salvar os dados no banco de dados Oracle.
3. Execute `main.py` para iniciar o aplicativo e siga as instruções no menu.

Se precisar de mais assistência ou encontrar problemas, consulte os documentos das bibliotecas ou entre em contato com o desenvolvedor responsável.

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>scripts</b>: Codigos do projeto

- <b>README.md</b>: Instruções

## 🔧 Como executar o código

main.py


## 🗃 Histórico de lançamentos
* 0.2.0 - 15/10/2024
    * 
* 0.1.0 - 13/10/2024
    *

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


