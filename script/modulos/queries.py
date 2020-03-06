

query_ex1 = """
        query RepositoriosPopulares {
            search(query: "stars:>100", type: REPOSITORY, first:25{after}) {
              pageInfo {
                hasNextPage
                endCursor
              }
              nodes {
                ... on Repository {
                  nameWithOwner
                  createdAt
                  pullRequests (states: MERGED){
                    totalCount
                  }
                  releases {
                    totalCount
                  }
                  updatedAt
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
