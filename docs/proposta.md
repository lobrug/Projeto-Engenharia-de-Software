# 1. Definição do Trio

- Lorenzo Brugnolo Rosa
- Luiz Bonfá dos Santos
- João Victor Lourenço

# 2. Descrição do Sistema

O projeto consiste em um analisador tático de métricas ofensivas, com foco em gols esperados (xG) e assistências esperadas (xA), voltado a analistas de desempenho e comissões técnicas.

O sistema recebe arquivos JSON ou CSV com dados dos eventos de uma partida, e a partir desses dados, estima a probabilidade de uma finalização resultar em gol, considerando diversas métricas como a distância e o ângulo em relação ao gol. Como resultado, gera um relatório em texto sobre a criação de oportunidades e a eficiência da equipe nas finalizações.

# 3. Pesquisa de Justificativa

**Referência:** Stats Perform. “Expected Goals (xG): The Football Metric Changing Analysis, Betting, and Fan Engagement”. Disponível em: [Stats Perform](https://www.statsperform.com/insights/expected-goals-xg-the-football-metric-changing-analysis-betting-and-fan-engagement/).

**Resumo:** A métrica de gols esperados (xG) estima, em uma escala de 0 a 1, a probabilidade de uma finalização resultar em gol. Assim, permite avaliar a qualidade das oportunidades criadas para além da quantidade de chutes. Modelos como o da Opta utilizam aprendizado de máquina e dados dos eventos da partida, considerando fatores como distância, ângulo e pressão defensiva.

O sistema proposto busca automatizar essa análise e reunir os resultados em um relatório que ajude a comissão técnica a identificar padrões ofensivos e aspectos que precisam ser trabalhados nos treinos. Esses dados complementam a observação das partidas e oferecem uma base para avaliar o desempenho da equipe.