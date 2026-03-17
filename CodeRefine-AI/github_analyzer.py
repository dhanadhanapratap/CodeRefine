import requests

def analyze_repo(repo):

    api = repo.replace("github.com","api.github.com/repos")

    r = requests.get(api)

    data = r.json()

    return {
        "Stars":data.get("stargazers_count"),
        "Forks":data.get("forks_count"),
        "Open Issues":data.get("open_issues_count")
    }