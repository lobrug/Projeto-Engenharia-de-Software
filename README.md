# Projeto-Engenharia-de-Software
Projeto feito para a disciplina de Engenharia de Software aplicando os conceitos aprendidos em aula.

Analisador de métricas ofensivas (xG e conversões em gol) a partir dos dados de eventos do [StatsBomb Open Data](https://github.com/hudl/open-data). A proposta, as histórias de usuário e o diagrama da arquitetura estão em `docs/`.

## Como executar

Requer Python 3, sem dependências externas. Na raiz do projeto:

```
python main.py
```

Gera o relatório da final da Copa do Mundo 2022 (Argentina x França), cujos dados estão em `dados/`. Para outra partida da Copa 2022, baixe o arquivo `data/events/<id>.json` do open-data, salve como `dados/eventos_<id>.json` e rode `python main.py <id>`.

## Testes

```
python -m unittest -v
```
