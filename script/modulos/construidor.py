from csv import DictWriter
from configuracao import colunas_node

def constroi_dicionario_node(node: dict) -> dict:

    return {
        'nome': node['nameWithOwner'],
        'data_criacao': node['createdAt'],
        'data_atualizacao': node['updatedAt'],
        'pull_requests': node['pullRequests']['totalCount'],
        'releases': node['releases']['totalCount'],
        'linguagem': node['primaryLanguage']['name'] if node['primaryLanguage'] else '',
        'issues_fechadas': node['closedIssues']['totalCount'],
        'issues_totais': node['totalIssues']['totalCount'],
        'stargazes': node['stargazers']['totalCount']
    }


def escreve_repositorios_csv(repositorios: list) -> None:

    with open('resultados/resultado1.csv', 'w') as resultado_1:
        writer = DictWriter(resultado_1, fieldnames=colunas_node)
        writer.writeheader()

        for repo in repositorios:
            node_dict = constroi_dicionario_node(repo)
            writer.writerow(node_dict)
