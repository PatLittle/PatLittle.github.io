# Pat Little Blog (Jekyll)

A professional, Jekyll-based blog designed for GitHub Pages. The site includes a custom theme, home page hero, blog archive, resume page, and structured data in `_data/site.yml`.

## Local development

1. Install Ruby (recommended: 3.x) and Bundler.
2. Install dependencies:
   ```bash
   bundle install
   ```
3. Run the site locally:
   ```bash
   bundle exec jekyll serve
   ```
4. Visit `http://localhost:4000`.

## Adding a blog post

Posts live in the `_posts/` folder and must use the format `YYYY-MM-DD-title.md`.

Example:
```markdown
---
title: "Your Post Title"
category: "Product"
---

Your post content goes here.
```

The `category` field shows up as the tag on the home page cards.

## Adding a new page (resume, about, etc.)

Pages live in the `pages/` folder. Add front matter with a `permalink` so the URL is predictable.

Example for a resume page:
```markdown
---
layout: page
title: "Resume"
permalink: /resume/
---

Content goes here.
```

## Adding images or other assets

- Place images in `assets/images/`.
- Reference them with absolute paths, for example: `![Alt text](/assets/images/your-image.png)`.
- Store other files (like PDFs) in `assets/` and link to them directly (e.g., `/assets/resume.pdf`).

## Customizing the theme

Theme content and labels are stored in `_data/site.yml`.

- **Hero content:** `_data/site.yml` → `hero`
- **Profile details:** `_data/site.yml` → `profile`
- **Highlights and topics:** `_data/site.yml` → `sections`
- **Styling:** `assets/css/style.css`
