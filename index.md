---
layout: home
title: "Pat Little's Blog"
---

Welcome to my personal blog! Here you'll find my latest posts.

{% if site.data.profile %}
![Profile Picture]({{ site.data.profile.avatar_url }}){: style="width:150px;border-radius:50%;" }

**Followers:** {{ site.data.profile.followers }}

{% if site.data.profile.organizations and site.data.profile.organizations | size > 0 %}
### Organizations
<ul>
{% for org in site.data.profile.organizations %}
  <li><a href="{{ org.html_url }}">{{ org.login }}</a></li>
{% endfor %}
</ul>
{% endif %}

{% if site.data.profile.achievements and site.data.profile.achievements | size > 0 %}
### Achievements
<ul>
{% for ach in site.data.profile.achievements %}
  <li>{{ ach }}</li>
{% endfor %}
</ul>
{% endif %}
{% endif %}

[Connect with me on LinkedIn](https://www.linkedin.com/in/patrickjlittle/)


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

