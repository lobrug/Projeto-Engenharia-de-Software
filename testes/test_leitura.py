import math
import unittest
from codigo.leitura import calcular_distancia, calcular_angulo, extrair_finalizacoes, extrair_partida


def criar_chute(equipe, resultado, location, periodo=1, parte_corpo="Right Foot"):
    return {
        "type": {"name": "Shot"},
        "period": periodo,
        "team": {"name": equipe},
        "location": location,
        "shot": {
            "outcome": {"name": resultado},
            "body_part": {"name": parte_corpo}
        }
    }


class TestLeitura(unittest.TestCase):
    def test_distancia_ate_o_centro_do_gol(self):
        self.assertAlmostEqual(calcular_distancia(100.0, 40.0), 20.0)
        self.assertAlmostEqual(calcular_distancia(90.0, 30.0), math.hypot(30.0, 10.0))

    def test_angulo_entre_as_traves(self):
        self.assertAlmostEqual(calcular_angulo(100.0, 40.0), 2 * math.atan(4 / 20))
        self.assertGreater(calcular_angulo(110.0, 40.0), calcular_angulo(100.0, 40.0))

    def test_extrai_apenas_finalizacoes_no_formato_do_sistema(self):
        eventos = [
            {"type": {"name": "Pass"}, "period": 1},
            criar_chute("Argentina", "Goal", [108.0, 40.0], parte_corpo="Left Foot")
        ]
        finalizacoes = extrair_finalizacoes(eventos)
        self.assertEqual(len(finalizacoes), 1)
        self.assertEqual(finalizacoes[0]["equipe"], "Argentina")
        self.assertEqual(finalizacoes[0]["resultado"], "Goal")
        self.assertEqual(finalizacoes[0]["parte_corpo"], "Left Foot")
        self.assertAlmostEqual(finalizacoes[0]["distancia"], 12.0)

    def test_desconsidera_disputa_de_penaltis(self):
        eventos = [
            criar_chute("Argentina", "Goal", [108.0, 40.0], periodo=4),
            criar_chute("Argentina", "Goal", [108.0, 40.0], periodo=5)
        ]
        self.assertEqual(len(extrair_finalizacoes(eventos)), 1)

    def test_extrai_dados_da_partida(self):
        partidas = [{
            "match_id": 1,
            "match_date": "2022-12-18",
            "home_team": {"home_team_name": "Argentina"},
            "away_team": {"away_team_name": "France"}
        }]
        partida = extrair_partida(partidas, 1)
        self.assertEqual(partida["nome"], "Argentina x France")
        self.assertEqual(partida["data"], "2022-12-18")
        self.assertEqual(partida["equipes"], ["Argentina", "France"])

    def test_rejeita_partida_inexistente(self):
        with self.assertRaises(ValueError):
            extrair_partida([], 1)
