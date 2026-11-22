# PADRÃO FACADE

from codigo.leitura import carregar_json, extrair_finalizacoes, extrair_partida
from codigo.relatorio import gerar_relatorio

PASTA_DADOS = "dados"
ARQUIVO_PARTIDAS = "partidas_copa_2022.json"


class AnalisadorPartida:
    """Ponto único de entrada: lê os dados, calcula as métricas e gera o relatório."""

    def __init__(self, pasta_dados=PASTA_DADOS, arquivo_partidas=ARQUIVO_PARTIDAS):
        self.pasta_dados = pasta_dados
        self.arquivo_partidas = arquivo_partidas

    def analisar(self, id_partida, estrategias=None):
        partida = self._carregar_partida(id_partida)
        finalizacoes = self._carregar_finalizacoes(id_partida)
        return gerar_relatorio(partida, finalizacoes, estrategias)

    def _carregar_partida(self, id_partida):
        partidas = carregar_json(f"{self.pasta_dados}/{self.arquivo_partidas}")
        return extrair_partida(partidas, id_partida)

    def _carregar_finalizacoes(self, id_partida):
        eventos = carregar_json(f"{self.pasta_dados}/eventos_{id_partida}.json")
        return extrair_finalizacoes(eventos)
