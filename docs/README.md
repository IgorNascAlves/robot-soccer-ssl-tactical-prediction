# Predição Tática Multiagente - Robot Soccer SSL

Este repositório contém a prova de conceito para o projeto da disciplina **CCM-109: Tópicos Especiais em Inteligência Artificial**, focada na predição tática de enxames de robôs da Robot Soccer Small Size League (SSL) utilizando modelagem sequencial profunda (LSTMs).

## Estrutura do Repositório
* `data/`: Contém os logs ProtoBuf brutos e os dados estruturados em tensores (Janelas Deslizantes).
* `src/`: Scripts Python para processamento de dados e treinamento dos modelos PyTorch.
* `docs/`: Documentação acadêmica, incluindo o artigo final e arquivos de referências bibliográficas.

## Como Executar
1. Instale as dependências: `pip install -r requirements.txt`
2. Extraia os dados brutos: `python src/data/make_dataset.py`
3. Inicie o treinamento do modelo LSTM: `python src/training/train.py`