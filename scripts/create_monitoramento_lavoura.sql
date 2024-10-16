-- create_monitoramento_lavoura.sql

CREATE TABLE monitoramento_lavoura (
    id NUMBER GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY,
    data_analise DATE NOT NULL,
    caminho_imagem VARCHAR2(255),
    ndvi_medio NUMBER(5,2),
    ndvi_minimo NUMBER(5,2),
    ndvi_maximo NUMBER(5,2),
    problemas_totais NUMBER,
    problemas_avancados NUMBER,
    pragas_totais NUMBER,
    relatorio_json CLOB,
    data_criacao TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_monitoramento_data_analise ON monitoramento_lavoura(data_analise);

-- Comentários adicionais sobre a tabela
COMMENT ON TABLE monitoramento_lavoura IS 'Tabela para armazenar dados de monitoramento da lavoura, incluindo NDVI, detecção de problemas e pragas.';
COMMENT ON COLUMN monitoramento_lavoura.id IS 'Chave primária, identificador único para cada registro.';
COMMENT ON COLUMN monitoramento_lavoura.data_analise IS 'Data em que a análise foi realizada.';
COMMENT ON COLUMN monitoramento_lavoura.caminho_imagem IS 'Caminho do arquivo da imagem multiespectral utilizada.';
COMMENT ON COLUMN monitoramento_lavoura.ndvi_medio IS 'Valor médio do NDVI calculado.';
COMMENT ON COLUMN monitoramento_lavoura.ndvi_minimo IS 'Valor mínimo do NDVI calculado.';
COMMENT ON COLUMN monitoramento_lavoura.ndvi_maximo IS 'Valor máximo do NDVI calculado.';
COMMENT ON COLUMN monitoramento_lavoura.problemas_totais IS 'Quantidade total de áreas problemáticas detectadas.';
COMMENT ON COLUMN monitoramento_lavoura.problemas_avancados IS 'Quantidade total de problemas detectados na análise avançada.';
COMMENT ON COLUMN monitoramento_lavoura.pragas_totais IS 'Quantidade total de pragas identificadas.';
COMMENT ON COLUMN monitoramento_lavoura.relatorio_json IS 'Dados adicionais em formato JSON.';
COMMENT ON COLUMN monitoramento_lavoura.data_criacao IS 'Timestamp de quando o registro foi criado.';
