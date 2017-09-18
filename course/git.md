---
permalink: /course/git/
title: Course | System | Git
---
# Git

[Git](https://git-scm.com/) is a [free and open-source](https://git-scm.com/about/free-and-open-source) version control system. [Git How To](https://githowto.com/) offers a simple guided tour that walks through the fundamentals of Git. [Submodules](https://git-scm.com/book/en/v2/Git-Tools-Submodules) allow users to keep a Git repository as a subdirectory of another Git repository.

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

