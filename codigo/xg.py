import math

INTERCEPTO = -1.6086323280381432
COEF_DISTANCIA = 0.09458330048327881
COEF_ANGULO = 1.523290920858915

def calcular_xg(finalizacao):

    for campo in ("distancia", "angulo", "parte_corpo"):
        if campo not in finalizacao:
            raise ValueError(f"Campo obrigatório ausente: {campo}")

    PESOS_PARTE_CORPO = {
        "Head": -0.8973745995538472,
        "Left Foot": 0.42838453367368506,
        "Other": -0.03455287582342893,
        "Right Foot": 0.503542941703537,
    }

    z = (
        INTERCEPTO
        - COEF_DISTANCIA * finalizacao["distancia"]
        + COEF_ANGULO * finalizacao["angulo"]
        + PESOS_PARTE_CORPO[finalizacao["parte_corpo"]]
    )

    return 1 / (1 + math.exp(-z))