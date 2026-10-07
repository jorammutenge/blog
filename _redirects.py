# Runs after `quarto render` (see post-render in _quarto.yml).
# Old /posts/24/MMDD/ addresses whose posts now live on conterval.com.
# Redirects within this site use `aliases:` in each post instead.
import html
import os
from pathlib import Path

CONTERVAL = "https://www.conterval.com/blog/"
REDIRECTS = {
    "0527": "create-dataframe-from-clipboard-content",
    "0613": "my-submission-to-the-posit-table-contest",
    "0618": "read-directly-from-html-with-polars",
    "0620": "native-plotting-with-polars",
    "0621": "my-reading-journey-with-the-libby-app",
    "0630": "making-beautiful-bar-charts-with-matplotlib",
    "0716": "getting-month-and-day-names-from-datetime-with-polars",
    "0723": "the-many-ways-to-rename-columns-in-polars",
    "0730": "advanced-styling-in-pandas",
    "0806": "formatting-the-information-displayed-in-the-tooltip-of-your-plotly-chats",
    "0813": "creating-a-pareto-chart-with-plotly",
    "0814": "why-you-should-learn-polars-for-data-analysis",
    "0820": "effective-table-presentation-with-code",
    "0827": "why-loops-are-frowned-upon-in-data-science",
    "0917": "a-simple-viz-is-all-you-need",
    "0924": "the-scramble-for-ai-domain-names",
    "1001": "using-variance-in-product-development",
    "1008": "on-golf-and-machine-learning",
    "1015": "unicorn-dropout-founders-are-rare",
    "1022": "secret-to-longevity-for-men",
    "1029": "how-to-create-charts-from-the-economist-magazine-using-plotly",
}

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Redirecting…</title>
<link rel="canonical" href="{url}">
<meta http-equiv="refresh" content="0; url={url}">
<script>window.location.replace("{url}");</script>
</head>
<body>This post has moved to <a href="{url}">{url}</a>.</body>
</html>
"""

out_dir = Path(os.environ.get("QUARTO_PROJECT_OUTPUT_DIR", "docs"))
for mmdd, slug in REDIRECTS.items():
    page = out_dir / "posts" / "24" / mmdd / "index.html"
    page.parent.mkdir(parents=True, exist_ok=True)
    page.write_text(PAGE.format(url=html.escape(CONTERVAL + slug + "/")))
