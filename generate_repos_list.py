import json

import re
from pathlib import Path

import requests

USER = "PatLittle"
REPOS_OUTPUT = Path("_data/repos.json")
PROFILE_OUTPUT = Path("_data/profile.json")


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


def fetch_profile(user: str):
    url = f"https://api.github.com/users/{user}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return {
        "avatar_url": data.get("avatar_url"),
        "html_url": data.get("html_url"),
        "followers": data.get("followers"),
    }


def fetch_organizations(user: str):
    url = f"https://api.github.com/users/{user}/orgs"
    response = requests.get(url)
    response.raise_for_status()
    orgs = []
    for org in response.json():
        orgs.append({"login": org.get("login"), "html_url": f"https://github.com/{org.get('login')}"})
    return orgs


def fetch_achievements(user: str):
    url = f"https://github.com/users/{user}/achievements"
    response = requests.get(url)
    response.raise_for_status()
    alts = re.findall(r'alt="([^"]+)"', response.text)
    achievements = []
    for alt in alts:
        if alt and alt not in achievements and "avatar" not in alt.lower():
            achievements.append(alt)
    return achievements


def save_profile_data(profile: dict, orgs, achievements, path: Path):
    data = dict(profile)
    data["organizations"] = orgs
    data["achievements"] = achievements
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


if __name__ == "__main__":
    repos = fetch_repos(USER)
    save_repos(repos, REPOS_OUTPUT)

    profile = fetch_profile(USER)
    orgs = fetch_organizations(USER)
    achievements = fetch_achievements(USER)
    save_profile_data(profile, orgs, achievements, PROFILE_OUTPUT)

