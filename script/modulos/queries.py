

query_ex1 = {
    'query': """{
        search(query: "stars: >100", type: REPOSITORY, first: 100) {
            nodes {
            ... on Repository {
                nameWithOwner
                createdAt
                updatedAt
                pullRequests {
                    totalCount
                }
                releases {
                    totalCount
                }
                primaryLanguage {
                    name
                }
                closedIssues: issues(states: CLOSED) {
                    totalCount
                }   
                totalIssues: issues {
                    totalCount
                }
                stargazers {
                    totalCount
                }
            }
        }
    }
}
"""
}
