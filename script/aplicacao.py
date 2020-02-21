# v1.0.0

from logging import basicConfig, ERROR
from modulos.requisicoes import obtem_repositorios
from json import dump

basicConfig(format='%(asctime)s - %(message)s', level=ERROR)


def exercicio_01() -> None:

    repositorios = obtem_repositorios()

    with open('resultados/resultado1.json', 'w') as resultado_1:
        dump(repositorios, resultado_1)


exercicio_01()
