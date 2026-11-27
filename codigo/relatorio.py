from codigo.metricas import MetricaConversoes, MetricaXG, MetricaFinalizacoesNoAlvo, MetricaPrecisao, MetricaXGPorFinalizacao, MetricaGrandesOportunidades

def gerar_relatorio(partida, finalizacoes, estrategias=None):
    if estrategias is None: estrategias = [MetricaConversoes(), MetricaXG(), MetricaFinalizacoesNoAlvo(), MetricaPrecisao(), MetricaXGPorFinalizacao(), MetricaGrandesOportunidades()]
    linhas = [f"Relatório da partida: {partida['nome']} ({partida['data']})"]

    for equipe in partida["equipes"]:
        finalizacoes_equipe = [f for f in finalizacoes if f["equipe"] == equipe]
        linha = f"{equipe} | Finalizações: {len(finalizacoes_equipe)}"

        for estrategia in estrategias:
            valor = estrategia.calcular(finalizacoes, equipe)
            resultado = estrategia.formatar(valor)
            linha += f" | {estrategia.nome}: {resultado}"
        linhas.append(linha)

    return "\n".join(linhas)