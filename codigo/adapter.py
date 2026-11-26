# PADRÃO ADAPTER

from abc import ABC, abstractmethod
from pathlib import Path
from codigo.leitura import carregar_json, extrair_finalizacoes, extrair_partida

# dados/ fica na raiz do projeto, um nível acima de codigo/
PASTA_DADOS = Path(__file__).resolve().parent.parent / "dados"
ARQUIVO_PARTIDAS = "partidas_copa_2022.json"


class FonteDadosPartida(ABC):
    """Formato que o sistema espera de qualquer fonte de dados."""

    @abstractmethod
    def obter_partida(self, id_partida):
        """Devolve {"nome", "data", "equipes"} da partida."""

    @abstractmethod
    def obter_finalizacoes(self, id_partida):
        """Devolve a lista de finalizações com equipe, resultado, distância, ângulo e parte do corpo."""


class StatsBombAdapter(FonteDadosPartida):
    """Converte os JSONs da StatsBomb para o formato usado pelo sistema."""

    def __init__(self, pasta_dados=PASTA_DADOS, arquivo_partidas=ARQUIVO_PARTIDAS):
        self.pasta_dados = Path(pasta_dados)
        self.arquivo_partidas = arquivo_partidas

    def obter_partida(self, id_partida):
        partidas = carregar_json(self.pasta_dados / self.arquivo_partidas)
        return extrair_partida(partidas, id_partida)

    def obter_finalizacoes(self, id_partida):
        eventos = carregar_json(self.pasta_dados / f"eventos_{id_partida}.json")
        return extrair_finalizacoes(eventos)
