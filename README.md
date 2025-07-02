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

## Updating GitHub data

Run `python generate_repos_list.py` to fetch information about my GitHub profile and repositories. The script saves repository links to `_data/repos.json` and profile details to `_data/profile.json`. The homepage uses these files to show profile stats and links.

## License

Unless otherwise noted, content on this site is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).