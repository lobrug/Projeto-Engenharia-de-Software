# PADRÃO STRATEGY

from abc import ABC, abstractmethod
from codigo.xg import calcular_xg
from codigo.conversoes import contar_conversoes

class MetricaOfensiva(ABC):
    nome = ""

    @abstractmethod
    def calcular(self, finalizacoes, equipe):
        """Calcula a métrica escolhida"""


class MetricaConversoes(MetricaOfensiva):
    nome = "Gols"

    def calcular(self, finalizacoes, equipe):
        return contar_conversoes(finalizacoes, equipe)

class MetricaXG(MetricaOfensiva):
    nome = "xG total"

    def calcular(self, finalizacoes, equipe):
        return sum(calcular_xg(finalizacao) for finalizacao in finalizacoes if finalizacao["equipe"] == equipe)