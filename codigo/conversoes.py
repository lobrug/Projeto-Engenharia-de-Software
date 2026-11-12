RESULTADO_GOL = "Goal"


def contar_conversoes(finalizacoes, equipe):
    """Conta quantas finalizações da equipe informada terminaram em gol."""
    return sum(
        1
        for finalizacao in finalizacoes
        if finalizacao["equipe"] == equipe and finalizacao["resultado"] == RESULTADO_GOL
    )
