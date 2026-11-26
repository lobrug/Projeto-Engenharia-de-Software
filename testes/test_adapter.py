import unittest
from codigo.adapter import PASTA_DADOS, FonteDadosPartida, StatsBombAdapter
from codigo.leitura import carregar_json, extrair_finalizacoes, extrair_partida

ID_FINAL_COPA_2022 = 3869685


class TestStatsBombAdapter(unittest.TestCase):
    def test_segue_a_interface_de_fonte_de_dados(self):
        self.assertIsInstance(StatsBombAdapter(), FonteDadosPartida)

    def test_obtem_a_mesma_partida_que_a_leitura_sem_adapter(self):
        partidas = carregar_json(PASTA_DADOS / "partidas_copa_2022.json")
        esperado = extrair_partida(partidas, ID_FINAL_COPA_2022)
        self.assertEqual(StatsBombAdapter().obter_partida(ID_FINAL_COPA_2022), esperado)

    def test_obtem_as_mesmas_finalizacoes_que_a_leitura_sem_adapter(self):
        eventos = carregar_json(PASTA_DADOS / f"eventos_{ID_FINAL_COPA_2022}.json")
        esperado = extrair_finalizacoes(eventos)
        self.assertEqual(StatsBombAdapter().obter_finalizacoes(ID_FINAL_COPA_2022), esperado)

    def test_converte_a_partida_para_o_formato_do_sistema(self):
        partida = StatsBombAdapter().obter_partida(ID_FINAL_COPA_2022)
        self.assertEqual(partida["nome"], "Argentina x France")
        self.assertEqual(partida["data"], "2022-12-18")
        self.assertEqual(partida["equipes"], ["Argentina", "France"])

    def test_converte_as_finalizacoes_para_o_formato_do_sistema(self):
        finalizacoes = StatsBombAdapter().obter_finalizacoes(ID_FINAL_COPA_2022)
        self.assertEqual(len(finalizacoes), 30)
        for finalizacao in finalizacoes:
            with self.subTest(finalizacao=finalizacao):
                self.assertEqual(set(finalizacao), {"equipe", "resultado", "distancia", "angulo", "parte_corpo"})

    def test_rejeita_partida_inexistente(self):
        with self.assertRaises(ValueError):
            StatsBombAdapter().obter_partida(1)
