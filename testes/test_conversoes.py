import unittest
from codigo.conversoes import contar_conversoes


class TestConversoes(unittest.TestCase):
    def test_criterio1_conta_finalizacoes_convertidas_em_gol(self):
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Goal"},
            {"equipe": "Brasil", "resultado": "Saved"},
            {"equipe": "Brasil", "resultado": "Goal"},
            {"equipe": "Brasil", "resultado": "Off T"},
            {"equipe": "Brasil", "resultado": "Blocked"}
        ]
        conversoes = contar_conversoes(finalizacoes, "Brasil")
        self.assertEqual(conversoes, 2)

    def test_criterio2_desconsidera_gols_do_adversario(self):
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Goal"},
            {"equipe": "Argentina", "resultado": "Goal"},
            {"equipe": "Argentina", "resultado": "Goal"}
        ]
        conversoes = contar_conversoes(finalizacoes, "Brasil")
        self.assertEqual(conversoes, 1)

    def test_criterio2_desconsidera_finalizacoes_sem_gol(self):
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Saved"},
            {"equipe": "Brasil", "resultado": "Goal"},
            {"equipe": "Brasil", "resultado": "Off T"},
            {"equipe": "Brasil", "resultado": "Post"}
        ]
        conversoes = contar_conversoes(finalizacoes, "Brasil")
        self.assertEqual(conversoes, 1)

    def test_criterio3_retorna_zero_para_equipe_sem_finalizacoes(self):
        finalizacoes = [
            {"equipe": "Argentina", "resultado": "Goal"},
            {"equipe": "Argentina", "resultado": "Saved"}
        ]
        conversoes = contar_conversoes(finalizacoes, "Brasil")
        self.assertEqual(conversoes, 0)

    def test_criterio3_retorna_zero_para_equipe_sem_gols(self):
        finalizacoes = [
            {"equipe": "Brasil", "resultado": "Saved"},
            {"equipe": "Brasil", "resultado": "Off T"},
            {"equipe": "Brasil", "resultado": "Blocked"}
        ]
        conversoes = contar_conversoes(finalizacoes, "Brasil")
        self.assertEqual(conversoes, 0)
