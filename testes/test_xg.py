import unittest
from codigo.xg import calcular_xg


class TestXG(unittest.TestCase):
    def test_criterio1_xg_entre_zero_e_um(self):
        finalizacao = {
            "distancia": 4.0,
            "angulo": 1.5707453534,
            "parte_corpo": "Right Foot"
        }
        xg = calcular_xg(finalizacao)
        self.assertGreaterEqual(xg,0)
        self.assertLessEqual(xg,1)

    def test_criterio2_mesmas_saidas_para_mesmas_entradas(self):
        finalizacao = {
            "distancia": 4.0,
            "angulo": 1.5707453534,
            "parte_corpo": "Right Foot"
        }
        primeiro_xg = calcular_xg(finalizacao.copy())
        segundo_xg = calcular_xg(finalizacao.copy())
        self.assertEqual(primeiro_xg,segundo_xg)

    def test_criterio3_rejeita_finalizacao_com_dados_ausentes(self):
        finalizacao = {
            "distancia": 4.0,
            "angulo": 1.5707453534,
            "parte_corpo": "Right Foot"
        }

        for campo in finalizacao:
            finalizacao1 = finalizacao.copy()
            del finalizacao1[campo]

            with self.subTest(campo_ausente=campo):
                with self.assertRaises(ValueError):
                    calcular_xg(finalizacao1)