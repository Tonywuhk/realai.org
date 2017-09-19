---
permalink: /about/style-guide/
redirect_from: /about/style/
---
# Style Guide

This page describes the conventions used on [realai.org](http://realai.org/) site regarding its structure, the visual appearance of its pages, and its usage of natural and programming languages.

## Site Structure

There are three navigation links on top of all HTML pages of this site: Home, Sources and About. Main contents are accessed from [Home](http://realai.org/). The [Sources](http://realai.org/sources/) page is a collection of relevant links and can be used as a portal. Company and site-specific pages are under [About](http://realai.org/about/) and their URLs start with `.../about/`.

### URL Path

In general, a page's URL path is consistent with its logical place on this site. The final segment of a page's URL path is the same as its title, where spaces are replaced by `-`, letters are lower-case except acronyms such as AI, RNN, etc. An **exception** is that when different pages would share the same title based on their URL paths, the titles would then be customized to reflect their differences.

For convenience, some pages allow [redirects](https://help.github.com/articles/redirects-on-github-pages/), where one or more segments of a page's URL are replaced by a commonly accepted acronym or a shorter description of its title.

### Logical Path

When the logical path of a page differs from its URL path, it is specified in the page’s [front matter](https://jekyllrb.com/docs/frontmatter/):

```yaml
title: <level-1 page> | <level-2 page> | … | <level-n page> | <current page>
```

When a page has more than one logical structures, the most compelling one is specified as the above, and the remaining ones are recorded before the top-level heading of the page as normal text that contains links to higher-level pages. When necessary, an unordered list is used to record multiple logical structures.

## Visual Style

The visual style of the pages on this site is specified by an [HTML template](https://github.com/real-ai/realai.org/blob/master/_layouts/default.html) and a [cascading style sheet](https://github.com/real-ai/realai.org/blob/master/assets/css/style.scss).

### Heading
All headings have a bottom margin of 10px, use font color `#222222` and weight `700`.

On any page, *Heading 1* should be used at most once near the top of a page. This top-level heading will be the default title when it’s placed right after the page’s front matter. Heading 1 can be followed by one or more optional paragraphs. Its font size is 36px.

## Language

### English

#### Citation

A full citation includes the following pieces of information, commonly in this order:

* Date Published, List of Authors. Title and Link. *Publication Venue*. (optional) additional resources.

Details are specified in a [Python script](https://github.com/real-ai/realai.org/blob/master/about/cite-arxiv.py) (requires [feedparser](https://pypi.python.org/pypi/feedparser)) that outputs a full citation based on arXiv information.

#### Punctuation

A string that must be typed exactly such as a URL should be quoted as inline code, which has backticks around it in Markdown.

#### Capitalization

We use the default rules at [Capitalize My Title](https://capitalizemytitle.com/) for title and headings.

