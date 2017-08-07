---
permalink: /course/tools/git/
title: Tools | Git
---
# Git

[Git](https://git-scm.com/) is a [free and open-source](https://git-scm.com/about/free-and-open-source) version control system. [Git How To](https://githowto.com/) offers a simple guided tour that walks through the fundamentals of Git.

## GitHub

[GitHub](https://github.com/) is a popular code repository hosting site that uses Git. [GitHub Pages](https://pages.github.com/) allow websites to be hosted directly from a user's repository. A GitHub Pages site can be [created with the Jekyll Theme Chooser](https://help.github.com/articles/creating-a-github-pages-site-with-the-jekyll-theme-chooser/).

## Links

* Documentation: [Reference](https://git-scm.com/docs).

## Examples

* "Undo" the action of commit while leaving everything eles unchanged: `git reset --soft HEAD^`
* Skip the staging step to commit all changes: `git commit -a -m "Update files"`
* Show changes in `README.md` since the tip of `HEAD`: `git diff HEAD README.md`

