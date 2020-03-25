from git import Git
from csv import DictReader


def baixa_repositorios():
    with open('./resultados/resultado1.csv') as dados_repositorios:
        reader = DictReader(dados_repositorios)

        for repo in reader:
            print(f"Baixando repositório {repo['nome']}.")
            Git('./repositorios').clone(repo['url'])
