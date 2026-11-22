import sys
from codigo.analisador import AnalisadorPartida

ID_PARTIDA_PADRAO = 3869685  # Final da Copa do Mundo 2022: Argentina x França


def main():
    id_partida = int(sys.argv[1]) if len(sys.argv) > 1 else ID_PARTIDA_PADRAO
    print(AnalisadorPartida().analisar(id_partida))


if __name__ == "__main__":
    main()
