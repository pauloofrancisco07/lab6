# v2.0.0

from modulos.construidor import escreve_repositorios_csv
from logging import basicConfig, ERROR
from modulos.requisicoes import obtem_repositorios


basicConfig(format='%(asctime)s - %(message)s', level=ERROR)


def script() -> None:

    repositorios = obtem_repositorios()

    if not repositorios:
        exit()

    escreve_repositorios_csv(repositorios)


script()