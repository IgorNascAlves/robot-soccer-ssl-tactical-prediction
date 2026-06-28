# Proposta de Projeto (Entrega 1)

**Título:** Predição Tática e Coordenação Multiagente: Uma Abordagem Sequencial Profunda no Ambiente Robot Soccer SSL

## 1. Descrição do Problema e Motivação
A orquestração de múltiplos agentes em ambientes dinâmicos (como robôs autônomos ou sistemas de enxame) baseia-se tradicionalmente em máquinas de estado. A transição para um controle descentralizado e emergente exige que os sistemas compreendam o estado global a partir de interações temporais. O problema central deste projeto é treinar um modelo de Deep Learning para modelar a dependência temporal da movimentação de um time de robôs e inferir sua tática global, utilizando o ambiente da Robot Soccer Small Size League (SSL). Esta prova de conceito é o passo fundamental para a futura aplicação de arquiteturas análogas às de Large Language Models (LLMs) na orquestração de enxames e biologia sintética.

## 2. Base de Dados e Pré-processamento
O conjunto de dados será construído a partir de logs oficiais de telemetria da Robot Soccer SSL, extraídos de repositórios públicos na nuvem.
Os arquivos de replay, originalmente em binário (ProtoBuf), serão pré-processados e convertidos para tensores. Para capturar a evolução da jogada, os dados espaciais (coordenadas $x, y$ e orientação $\theta$ dos aliados, adversários e bola) serão estruturados em janelas deslizantes (sliding windows) de tamanho $T$. Dessa forma, a rede receberá como entrada uma série temporal multivariada, onde cada amostra representa a cinemática do enxame nos últimos segundos da partida.

## 3. Abordagem Metodológica e Arquitetura
Para lidar com a natureza sequencial dos dados de telemetria, o projeto será desenvolvido em PyTorch, com foco nas arquiteturas avançadas abordadas na disciplina.
A rede principal utilizará camadas de Redes Neurais Recorrentes, especificamente LSTMs (ou blocos de Transformers, caso a dimensionalidade temporal demande mecanismos de Attention). O modelo processará a sequência de estados do jogo para realizar uma tarefa de classificação (ex: identificar se o padrão atual é um ataque coordenado ou transição defensiva) ou de regressão (prever a posição futura dos agentes).
O treinamento envolverá a otimização da função de custo (como Cross-Entropy para classificação) utilizando otimizadores avançados (ex: Adam) e técnicas de retropropagação através do tempo (BPTT).

## 4. Otimização, Regularização e Avaliação
Para garantir a capacidade de generalização do modelo e evitar o sobreajuste (overfitting) aos times específicos do dataset, serão aplicadas técnicas de regularização como Dropout e Early Stopping durante a fase de treinamento. O desempenho da arquitetura LSTM/Transformer será avaliado contra um conjunto de validação isolado, utilizando métricas como Loss, Acurácia e F1-Score, demonstrando o ganho prático das arquiteturas profundas na resolução de problemas complexos de coordenação.
