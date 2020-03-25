from modulos.queries import query
from configuracao import cabecalho_api_github
from requests import post, HTTPError
from json import dumps
from logging import error
from time import sleep


def _executa_query(json: dict) -> dict:

    try:
        resposta = post("https://api.github.com/graphql",
                        headers=cabecalho_api_github,
                        data=json)

        resposta.raise_for_status()

        return resposta.json()

    except HTTPError as e:
        error(e)


def obtem_repositorios() -> list:

    primeira_query = query.replace("{after}", "")

    json = {
        'query': primeira_query,
        'variables': {}
    }

    resposta = _executa_query(dumps(json))

    if not resposta:
        print('Não foi possível obter os repositórios.')
        exit()

    nodes = resposta["data"]["user"]["repositories"]["nodes"]

    return nodes