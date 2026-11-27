# PADRÃO STRATEGY

from abc import ABC, abstractmethod
from codigo.xg import calcular_xg
from codigo.conversoes import contar_conversoes

class MetricaOfensiva(ABC):
    nome = ""

    @abstractmethod
    def calcular(self, finalizacoes, equipe):
        """Calcula a métrica escolhida"""

    def formatar(self, valor):
        return str(valor)


class MetricaConversoes(MetricaOfensiva):
    nome = "Gols"

    def calcular(self, finalizacoes, equipe):
        return contar_conversoes(finalizacoes, equipe)


class MetricaXG(MetricaOfensiva):
    nome = "xG total"

    def calcular(self, finalizacoes, equipe):
        return sum(calcular_xg(finalizacao) for finalizacao in finalizacoes if finalizacao["equipe"] == equipe)

    def formatar(self, valor):
        return f"{valor:.2f}"


class MetricaFinalizacoesNoAlvo(MetricaOfensiva):
    nome = "Finalizações no alvo"

    def calcular(self, finalizacoes, equipe):
        return sum(1 for f in finalizacoes if f["equipe"] == equipe and f["resultado"] in ("Goal", "Saved", "Saved to Post"))

class MetricaPrecisao(MetricaOfensiva):
    nome = "Precisão"

    def calcular(self, finalizacoes, equipe):
        total = sum(1 for f in finalizacoes if f["equipe"] == equipe)
        alvo = MetricaFinalizacoesNoAlvo().calcular(finalizacoes, equipe)
        return 100 * alvo / total if total else 0

    def formatar(self, valor):
        return f"{valor:.2f}%"


class MetricaXGPorFinalizacao(MetricaOfensiva):
    nome = "xG por finalização"

    def calcular(self, finalizacoes, equipe):
        total = sum(1 for f in finalizacoes if f["equipe"] == equipe)
        xg = MetricaXG().calcular(finalizacoes, equipe)
        return xg / total if total else 0

    def formatar(self, valor):
        return f"{valor:.3f}"


class MetricaGrandesOportunidades(MetricaOfensiva):
    nome = "Grandes oportunidades"

    def calcular(self, finalizacoes, equipe):
        return sum(1 for f in finalizacoes if f["equipe"] == equipe and calcular_xg(f) >= 0.30
        )