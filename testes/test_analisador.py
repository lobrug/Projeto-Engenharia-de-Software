import unittest
from codigo.analisador import AnalisadorPartida
from codigo.leitura import carregar_json, extrair_finalizacoes, extrair_partida
from codigo.metricas import MetricaConversoes
from codigo.relatorio import gerar_relatorio

ID_FINAL_COPA_2022 = 3869685


class TestAnalisadorPartida(unittest.TestCase):
    def test_gera_o_mesmo_relatorio_que_o_fluxo_sem_facade(self):
        partidas = carregar_json("dados/partidas_copa_2022.json")
        eventos = carregar_json(f"dados/eventos_{ID_FINAL_COPA_2022}.json")
        esperado = gerar_relatorio(
            extrair_partida(partidas, ID_FINAL_COPA_2022),
            extrair_finalizacoes(eventos)
        )
        self.assertEqual(AnalisadorPartida().analisar(ID_FINAL_COPA_2022), esperado)

    def test_relatorio_da_final_da_copa_2022(self):
        relatorio = AnalisadorPartida().analisar(ID_FINAL_COPA_2022)
        self.assertIn("Argentina x France (2022-12-18)", relatorio)
        self.assertIn("Argentina | Finalizações: 20 | Gols: 3", relatorio)
        self.assertIn("France | Finalizações: 10 | Gols: 3", relatorio)

    def test_repassa_as_estrategias_escolhidas(self):
        relatorio = AnalisadorPartida().analisar(ID_FINAL_COPA_2022, [MetricaConversoes()])
        self.assertIn("Gols:", relatorio)
        self.assertNotIn("xG total:", relatorio)

    def test_rejeita_partida_inexistente(self):
        with self.assertRaises(ValueError):
            AnalisadorPartida().analisar(1)
