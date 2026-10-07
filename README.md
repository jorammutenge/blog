# jorammutenge.com

Personal website and blog of Joram Mutenge, built with [Quarto](https://quarto.org).
Live at <https://www.jorammutenge.com>.

## Working on the site

```sh
quarto preview   # local server that reloads as you edit
quarto render    # build the site into _site/
```

## Writing a post

Create a folder under `posts/` with an `index.qmd` inside:

```
posts/my-new-post/index.qmd
```

```yaml
---
title: "My new post"
date: 2026-10-15
---

First paragraph here...
```

The home page lists posts newest first. Each card's excerpt is taken automatically
from the post's opening paragraphs. Posts also appear in the RSS feed (`index.xml`).

The home page shows 30 posts at a time. Past 30, a "See more posts »" button
reveals the next 30. Change the number with `pageSize` at the top of
`_includes/post-cards.ejs`.

## Project layout

| Path | What it is |
|---|---|
| `_quarto.yml` | Site settings (title, URL, theme) |
| `index.qmd` | Home page and post listing settings |
| `posts/` | Blog posts, one folder each |
| `posts/_metadata.yml` | Settings shared by every post (header, about footer) |
| `_includes/masthead.html` | Avatar and name at the top of the home page |
| `_includes/bio.html` | Bio and subscribe form (home page top and bottom of every post) |
| `_includes/about.html` | "About Joram Mutenge" heading above the bio on posts |
| `_includes/title-block.html` | Post header: avatar, name, date, title |
| `_includes/post-cards.ejs` | Template for the post cards on the home page |
| `_includes/site-tools.html` | Top-right corner holder for the toggle and Quarto's search (magnifying glass) |
| `_includes/theme-toggle.html` | Light/dark toggle (top-right). Follows the system until clicked; remembers the choice |
| `styles.scss` | All styling. `$column-width` sets the page width |
| `images/avatar.jpg` | Profile picture and browser-tab icon |
| `fonts/` | Harmonia Sans: Regular (text and block quotes), Bold (titles), SemiBold Condensed (buttons) |

## Email newsletter

The subscribe form in `_includes/bio.html` sends signups to
[Kit](https://kit.com) (formerly ConvertKit), form ID `10012341`:

```html
<form class="subscribe" action="https://app.kit.com/forms/10012341/subscriptions" method="post">
  <input type="email" name="email_address" placeholder="Type your email..." aria-label="Email address" required>
  <button type="submit">Subscribe</button>
</form>
```

- Kit requires the input's name to be `email_address`.
- New subscribers appear in Kit under **Grow → Subscribers**. If double opt-in is
  on (Kit's default), they appear only after confirming by email.
- What visitors see after subscribing (Kit's thank-you page or a redirect) and the
  double opt-in setting are set in Kit, under the form's **Settings**.
- To use a different Kit form, replace the number in `action` with that form's ID.
