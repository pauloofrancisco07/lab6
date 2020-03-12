from time import strptime
from datetime import datetime
from csv import reader

def _obtem_repositorios():
    with open('../resultados/resultado1.csv') as repositorios:
        leitor = list(reader(repositorios))

    return leitor


repositorios = _obtem_repositorios()
repositorios.pop(0)


def questao_01():
    global repositorios
    qtd_repositorios_maduros = 0
    qtd_repositorios_novos = 0

    ano_atual = datetime.now().year

    for repositorio in repositorios:
        data_criacao = repositorio[1]
        ano_repositorio = strptime(data_criacao, "%Y-%m-%dT%H:%M:%SZ").tm_year

        idade = ano_atual - ano_repositorio

        if idade > 3:
            qtd_repositorios_maduros += 1
        else:
            qtd_repositorios_novos += 1

    print("--------------------------------QUESTÃO 01-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios novos é: {qtd_repositorios_novos} "
          f"e a de maduros é: {qtd_repositorios_maduros}")

    if qtd_repositorios_maduros > qtd_repositorios_novos:
        print("Repositorios populares são maduros!")
    else:
        print("Repositorios populares não são maduros!")

    print("-----------------------------------------------------------------------------------------")


def questao_02():
    global repositorios
    pull_requests_totais = 0

    muita_contribuicao = 0
    pouca_contribuicao = 0

    for repositorio in repositorios:
        pull_requests_aceitas = int(repositorio[3])
        pull_requests_totais += pull_requests_aceitas

    media = pull_requests_totais/1000

    for repositorio in repositorios:
        pull_requests_aceitas = int(repositorio[3])

        if pull_requests_aceitas > media:
            muita_contribuicao += 1
        else:
            pouca_contribuicao += 1

    print("--------------------------------QUESTÃO 02-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios com muita contribuição externa é: {muita_contribuicao} "
          f"e com pouca contribuição externa é: {pouca_contribuicao}")

    if muita_contribuicao > pouca_contribuicao:
        print("Repositorios populares tem muita contribuição externa!")
    else:
        print("Repositorios populares tem pouca contribuição externa!")

    print("-----------------------------------------------------------------------------------------")


def questao_03():
    global repositorios
    releases_totais = 0
    releases = []

    muita_release = 0
    pouca_release = 0

    for repositorio in repositorios:
        qtd_releases = int(repositorio[4])
        releases_totais += qtd_releases
        releases.append(qtd_releases)

    media = releases_totais/1000

    for release in releases:
        if release > media:
            muita_release += 1
        else:
            pouca_release += 1


    print("--------------------------------QUESTÃO 03-----------------------------------------------")

    print(f"Tendo em vista que a quantidade de repositórios com muitas releases é: {muita_release} "
          f"e com poucas releases é: {pouca_release}")

    if muita_release > pouca_release:
        print("Repositorios populares tem muitas releases!")
    else:
        print("Repositorios populares tem poucas releases!")

    print("-----------------------------------------------------------------------------------------")


questao_03()