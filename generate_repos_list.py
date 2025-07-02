import requests
import json
from pathlib import Path

USER = "PatLittle"
OUTPUT = Path("_data/repos.json")


def fetch_repos(user: str):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    response.raise_for_status()
    return [
        {"name": repo["name"], "html_url": repo["html_url"]}
        for repo in response.json()
    ]


def save_repos(repos, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(repos, f, indent=2)


if __name__ == "__main__":
    repos = fetch_repos(USER)
    save_repos(repos, OUTPUT)
