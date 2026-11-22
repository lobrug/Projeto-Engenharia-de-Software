# PADRÃO FACADE

from pathlib import Path
from codigo.leitura import carregar_json, extrair_finalizacoes, extrair_partida
from codigo.relatorio import gerar_relatorio

# dados/ fica na raiz do projeto, um nível acima de codigo/
PASTA_DADOS = Path(__file__).resolve().parent.parent / "dados"
ARQUIVO_PARTIDAS = "partidas_copa_2022.json"


class AnalisadorPartida:
    """Ponto único de entrada: lê os dados, calcula as métricas e gera o relatório."""

    def __init__(self, pasta_dados=PASTA_DADOS, arquivo_partidas=ARQUIVO_PARTIDAS):
        self.pasta_dados = Path(pasta_dados)
        self.arquivo_partidas = arquivo_partidas

    def analisar(self, id_partida, estrategias=None):
        partida = self._carregar_partida(id_partida)
        finalizacoes = self._carregar_finalizacoes(id_partida)
        return gerar_relatorio(partida, finalizacoes, estrategias)

    def _carregar_partida(self, id_partida):
        partidas = carregar_json(self.pasta_dados / self.arquivo_partidas)
        return extrair_partida(partidas, id_partida)

    def _carregar_finalizacoes(self, id_partida):
        eventos = carregar_json(self.pasta_dados / f"eventos_{id_partida}.json")
        return extrair_finalizacoes(eventos)
