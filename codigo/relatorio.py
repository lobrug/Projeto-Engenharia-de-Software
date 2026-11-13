from codigo.xg import calcular_xg
from codigo.conversoes import contar_conversoes


def gerar_relatorio(partida, finalizacoes):
    linhas = [f"Relatório da partida: {partida['nome']} ({partida['data']})"]

    for equipe in partida["equipes"]:
        finalizacoes_equipe = [f for f in finalizacoes if f["equipe"] == equipe]
        gols = contar_conversoes(finalizacoes, equipe)
        xg_total = sum(calcular_xg(f) for f in finalizacoes_equipe)
        linhas.append(f"{equipe} | Finalizações: {len(finalizacoes_equipe)} | Gols: {gols} | xG total: {xg_total:.2f}")

    return "\n".join(linhas)
