# Pat Little's Blog

This repository hosts my personal blog built with [Jekyll](https://jekyllrb.com/) and the `minima` theme.

## Writing posts

Add new markdown files to the `_posts` directory. Filenames must follow the pattern `YYYY-MM-DD-title.md` and include YAML front matter like:

```markdown
---
layout: post
title: "My Post Title"
---
```

The content under the front matter is written in regular Markdown.

## Updating the repository list

Run `python generate_repos_list.py` to fetch a list of my public GitHub repositories and save them to `_data/repos.json`. The index page uses this file to display links to each repo.
