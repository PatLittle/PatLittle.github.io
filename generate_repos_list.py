import requests
import json

def fetch_repos(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    return response.json()

def generate_html(repos):
        
    html_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pat Little's Blog</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Pat Little's Blog</h1>
        <nav>
            <ul>
                <li><a href="#about">About</a></li>
                <li><a href="#repos">Repositories</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="about">
            <h2>About Me</h2>
            <p>Hi, I'm Pat Little. Welcome to my personal blog where I share my projects and ideas.</p>
        </section>
    """
    html_content += "<h2>Repositories owned by User:PatLittle</h2>\n"
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
