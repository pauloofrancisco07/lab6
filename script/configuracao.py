from token_daniel import token


cabecalho_api_github = {
    'Content-Type': 'application/json',
    'Authorization': f"Bearer {token}"
}

colunas_node = ['nome', 'data_criacao', 'data_atualizacao', 'pull_requests', 'releases', 'linguagem', 'issues_fechadas',
                'issues_totais', 'stargazes']
