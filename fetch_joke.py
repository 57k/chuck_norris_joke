import requests
import os
from github import Github

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("value")
    else:
        return "Failed to retrieve joke"

if __name__ == "__main__":
    joke = get_chuck_norris_joke()
    issue_number = os.environ['GITHUB_EVENT']['issue']['number']
    repo_name = os.environ['GITHUB_REPOSITORY']
    github_token = os.environ['GITHUB_TOKEN']

    g = Github(github_token)
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    issue.create_comment(f"Here's a Chuck Norris joke for you: {joke}")
