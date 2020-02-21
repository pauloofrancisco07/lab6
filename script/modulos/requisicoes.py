from modulos.queries import query_ex1
from configuracao import cabecalho_api_github
from requests import post, HTTPError
from json import dumps
from logging import error


def obtem_repositorios() -> dict:
    try:
        resposta = post("https://api.github.com/graphql",
                       headers=cabecalho_api_github,
                       data=dumps(query_ex1))

        resposta.raise_for_status()

        return resposta.json()

    except HTTPError as e:
        error(e)
