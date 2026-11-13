import json
import math

# Campo da StatsBomb: 120 x 80, gol atacado em x = 120 com as traves em y = 36 e y = 44
GOL_X = 120.0
TRAVE_ESQUERDA_Y = 36.0
TRAVE_DIREITA_Y = 44.0
PERIODO_DISPUTA_PENALTIS = 5


def carregar_json(caminho):
    with open(caminho, encoding="utf-8") as arquivo:
        return json.load(arquivo)


def calcular_distancia(x, y):
    centro_gol_y = (TRAVE_ESQUERDA_Y + TRAVE_DIREITA_Y) / 2
    return math.hypot(GOL_X - x, centro_gol_y - y)


def calcular_angulo(x, y):
    angulo_trave_esquerda = math.atan2(TRAVE_ESQUERDA_Y - y, GOL_X - x)
    angulo_trave_direita = math.atan2(TRAVE_DIREITA_Y - y, GOL_X - x)
    return abs(angulo_trave_direita - angulo_trave_esquerda)


def extrair_finalizacoes(eventos):
    finalizacoes = []
    for evento in eventos:
        if evento["type"]["name"] != "Shot" or evento["period"] == PERIODO_DISPUTA_PENALTIS:
            continue
        x, y = evento["location"]
        finalizacoes.append({
            "equipe": evento["team"]["name"],
            "resultado": evento["shot"]["outcome"]["name"],
            "distancia": calcular_distancia(x, y),
            "angulo": calcular_angulo(x, y),
            "parte_corpo": evento["shot"]["body_part"]["name"]
        })
    return finalizacoes


def extrair_partida(partidas, id_partida):
    for partida in partidas:
        if partida["match_id"] == id_partida:
            mandante = partida["home_team"]["home_team_name"]
            visitante = partida["away_team"]["away_team_name"]
            return {
                "nome": f"{mandante} x {visitante}",
                "data": partida["match_date"],
                "equipes": [mandante, visitante]
            }
    raise ValueError(f"Partida não encontrada: {id_partida}")
