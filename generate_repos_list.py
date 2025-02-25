import requests
import json

def fetch_repos(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    return response.json()

def generate_html(repos):
    html_content = "<h2>Repositories owned by User:PatLittle</h2>\n"
    html_content += "<ul>\n"
    for repo in repos:
        html_content += f"<li><a href='{repo['html_url']}'>{repo['name']}</a></li>\n"
    html_content += "</ul>\n"
    return html_content

def save_html(content, filename):
    with open(filename, "w") as file:
        file.write(content)

if __name__ == "__main__":
    user = "PatLittle"
    repos = fetch_repos(user)
    html_content = generate_html(repos)
    save_html(html_content, "index.html")
