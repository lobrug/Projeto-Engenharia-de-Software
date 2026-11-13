import unittest
from codigo.relatorio import gerar_relatorio
from codigo.xg import calcular_xg
from codigo.conversoes import contar_conversoes


class TestRelatorio(unittest.TestCase):
    def test_criterio1_relatorio_identifica_partida_e_metricas_por_equipe(self):
        partida = {"nome": "Brasil x Argentina", "data": "05/11/2026", "equipes": ["Brasil", "Argentina"]}
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Goal", "distancia": 4.0, "angulo": 1.5707453534, "parte_corpo": "Right Foot"},
            {"equipe": "Argentina", "resultado": "Saved", "distancia": 31.6, "angulo": 0.2449786631, "parte_corpo": "Left Foot"}
        ]
        relatorio = gerar_relatorio(partida, finalizacoes)
        self.assertIn("Brasil x Argentina", relatorio)
        self.assertIn("05/11/2026", relatorio)
        self.assertIn("Brasil | Finalizações:", relatorio)
        self.assertIn("Argentina | Finalizações:", relatorio)
        self.assertIn("Gols:", relatorio)
        self.assertIn("xG total:", relatorio)

    def test_criterio2_relatorio_apresenta_valores_calculados(self):
        partida = {"nome": "Brasil x Argentina", "data": "05/11/2026", "equipes": ["Brasil", "Argentina"]}
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Goal", "distancia": 4.0, "angulo": 1.5707453534, "parte_corpo": "Right Foot"},
            {"equipe": "Brasil", "resultado": "Saved", "distancia": 31.6, "angulo": 0.2449786631, "parte_corpo": "Left Foot"},
            {"equipe": "Brasil", "resultado": "Goal", "distancia": 10.2, "angulo": 0.7266423406, "parte_corpo": "Head"}
        ]
        relatorio = gerar_relatorio(partida, finalizacoes)
        gols = contar_conversoes(finalizacoes, "Brasil")
        xg_total = sum(calcular_xg(finalizacao) for finalizacao in finalizacoes)
        self.assertIn(f"Brasil | Finalizações: 3 | Gols: {gols} | xG total: {xg_total:.2f}", relatorio)

    def test_criterio3_gera_relatorio_com_equipe_sem_finalizacoes(self):
        partida = {"nome": "Brasil x Argentina", "data": "05/11/2026", "equipes": ["Brasil", "Argentina"]}
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Goal", "distancia": 4.0, "angulo": 1.5707453534, "parte_corpo": "Right Foot"}
        ]
        relatorio = gerar_relatorio(partida, finalizacoes)
        self.assertIn("Argentina | Finalizações: 0 | Gols: 0 | xG total: 0.00", relatorio)