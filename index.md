---
layout: home
title: "Pat Little's Blog"
---

Welcome to my personal blog! Here you'll find my latest posts.

## My GitHub Repositories

{% if site.data.repos and site.data.repos | size > 0 %}
<ul>
{% for repo in site.data.repos %}
  <li><a href="{{ repo.html_url }}">{{ repo.name }}</a></li>
{% endfor %}
</ul>
{% else %}
<p>No repository data available. Run <code>generate_repos_list.py</code> to update.</p>
{% endif %}

