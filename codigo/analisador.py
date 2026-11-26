# PADRÃO FACADE

from codigo.adapter import StatsBombAdapter
from codigo.relatorio import gerar_relatorio


class AnalisadorPartida:
    """Ponto único de entrada: lê os dados, calcula as métricas e gera o relatório."""

    def __init__(self, fonte_dados=None):
        self.fonte_dados = fonte_dados if fonte_dados is not None else StatsBombAdapter()

    def analisar(self, id_partida, estrategias=None):
        partida = self.fonte_dados.obter_partida(id_partida)
        finalizacoes = self.fonte_dados.obter_finalizacoes(id_partida)
        return gerar_relatorio(partida, finalizacoes, estrategias)
