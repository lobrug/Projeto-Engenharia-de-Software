## Historia 1 — Estimar o xG (chance de gol) de cada finalização

Como analista de desempenho, eu quero consultar a chance de gol de cada finalização para avaliar a qualidade ofensiva do time.

### Criterios de Aceitação

- 1: toda finalização deve receber um valor de xG entre 0 e 1.
- 2: uma finalização com os mesmos dados de entrada deve produzir o mesmo xG quando avaliada pela mesma versão do modelo.
- 3: uma finalização sem os dados exigidos pelo modelo deve gerar um erro de validação, sem receber um valor de xG.

## Historia 2 — Consultar o número de conversões em gol da equipe

Como analista de desempenho, eu quero consultar quantas finalizações da equipe resultaram em gol na partida, para avaliar o aproveitamento da equipe.

### Critérios de aceitação

- 1: o total de conversões deve corresponder à quantidade de finalizações da equipe cujo resultado foi gol. Por exemplo, cinco finalizações com dois gols devem resultar em duas conversões.
- 2: finalizações da equipe adversária e finalizações que não resultaram em gol não devem entrar nessa contagem.
- 3: uma equipe sem finalizações ou sem finalizações convertidas em gol deve apresentar zero conversões.

## Historia 3 — Gerar um relatório da partida

Como integrante da comissão técnica, quero gerar um relatório em texto com as métricas ofensivas da partida, para consultar e compartilhar os resultados da análise.

### Critérios de aceitação

- 1: o relatório deve identificar a partida e apresentar, por equipe, a quantidade de finalizações, os gols e o xG total.
- 2: os valores apresentados devem corresponder aos resultados calculados pelo sistema para a partida selecionada.
- 3: uma equipe sem finalizações deve aparecer no relatório com a quantidade de finalizações e o xG iguais a zero, sem impedir sua geração.