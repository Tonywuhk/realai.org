---
permalink: /course/git/
title: Course | Git
---
# Git

[Git](https://git-scm.com/) is a [free and open-source](https://git-scm.com/about/free-and-open-source) version control system. [Git How To](https://githowto.com/) offers a simple guided tour that walks through the fundamentals of Git. [Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) allow users to keep a Git repository as a subdirectory of another Git repository.

## GitHub

[GitHub](https://github.com/) is a popular code repository hosting site that uses Git. [GitHub Pages](https://pages.github.com/) allow websites to be hosted directly from a user's repository. A GitHub Pages site can be [created with the Jekyll Theme Chooser](https://help.github.com/articles/creating-a-github-pages-site-with-the-jekyll-theme-chooser/).

A GitHub Pages site can be [set up locally on a Linux machine](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#platform-linux) with Jekyll and Bundler, even if the Linux machine is a [subsystem](http://realai.org/course/windows/#windows-subsystem-for-linux) on *Windows*! Once successfully set up, the Jekyll site can be run locally by the command

```bash
bundle exec jekyll serve
```

## Links

* Documentation: [Reference](https://git-scm.com/docs).

## Examples

* "Undo" the action of commit while leaving everything else unchanged: `git reset --soft HEAD^`
* Skip the staging step to commit all changes: `git commit -a -m "Update files"`
* Show changes in `README.md` since the tip of a commit (or `HEAD`): `git diff <commit hash> README.md`

## Useful Aliases

```bash
alias.st=status
alias.hist=log --pretty=format:'%h %ad | %s%d [%an]' --graph --date=short
```

