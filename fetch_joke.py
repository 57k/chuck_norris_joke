import requests
import os
import json
from github import Github

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("value")
    else:
        return "Failed to retrieve joke"

def close_issue(repo, issue_number):
    issue = repo.get_issue(number=issue_number)
    issue.edit(state='closed')

if __name__ == "__main__":
    joke = get_chuck_norris_joke()

    with open(os.environ['GITHUB_EVENT_PATH']) as f:
        event = json.load(f)
    
    issue_number = event['issue']['number']
    repo_name = os.environ['GITHUB_REPOSITORY']
    github_token = os.environ['GITHUB_TOKEN']

    g = Github(github_token)
    repo = g.get_repo(repo_name)
    issue = repo.get_issue(number=issue_number)
    
    # Post the joke as a comment
    issue.create_comment(f"Here's a Chuck Norris joke for you: {joke}")
    
    # Close the issue
    close_issue(repo, issue_number)
