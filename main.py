import sys
from codigo.leitura import carregar_json, extrair_finalizacoes, extrair_partida
from codigo.relatorio import gerar_relatorio

ID_PARTIDA_PADRAO = 3869685  # Final da Copa do Mundo 2022: Argentina x França


def main():
    id_partida = int(sys.argv[1]) if len(sys.argv) > 1 else ID_PARTIDA_PADRAO

    partidas = carregar_json("dados/partidas_copa_2022.json")
    eventos = carregar_json(f"dados/eventos_{id_partida}.json")

    partida = extrair_partida(partidas, id_partida)
    finalizacoes = extrair_finalizacoes(eventos)

    print(gerar_relatorio(partida, finalizacoes))


if __name__ == "__main__":
    main()
