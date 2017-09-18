---
permalink: /course/github/
title: Course | System | GitHub
---
# GitHub

[GitHub](https://github.com/) is a popular code repository hosting site that uses [Git](http://realai.org/course/git/).

## GitHub Organizations

[Organizations](https://help.github.com/articles/about-organizations/) are shared accounts that allow multiple GitHub users to collaborate. [Permission levels for an organization](https://help.github.com/articles/permission-levels-for-an-organization/) include *owner* and *member*. [Repository permission levels for an organization](https://help.github.com/articles/repository-permission-levels-for-an-organization/) include *read*, *write* and *admin*. By default, a repository can only be deleted by members with admin permission to that repository. An owner of the organization, of course, can also delete a repository since owner privileges include complete administrative access to the organization. An owner can also [remove admin's ability to delete repositories](https://help.github.com/articles/repository-permission-levels-for-an-organization/#deleting-and-transferring-repositories) for this organization.

An organization owner is also a GitHub user, who has a primary [email address](https://help.github.com/articles/setting-your-commit-email-address-on-github/) that can be kept private. The following steps might make it extremely difficult to delete a repository:

* 1) Create a GitHub user with a private, temporary email address. Use sufficient [randomness](https://en.wikipedia.org/wiki/Password_strength#Required_bits_of_entropy) for both the email address and the password.
* 2) Create a GitHub repository.
* 3) Grant another GitHub user admin right to that repository, without the ability of deletion.
* 4) Discard the owner's email address and all traces to the owner's password.

The repository should remain operational for all practical purposes under its admin, but cannot be deleted and will retain its entire history of commits.

## GitHub Pages

 [GitHub Pages](https://pages.github.com/) allow websites to be hosted directly from a user's repository. A GitHub Pages site can be [created with the Jekyll Theme Chooser](https://help.github.com/articles/creating-a-github-pages-site-with-the-jekyll-theme-chooser/).

A GitHub Pages site can be [set up locally on a Linux machine](https://help.github.com/articles/setting-up-your-github-pages-site-locally-with-jekyll/#platform-linux) with Jekyll and Bundler, even if the Linux machine is a [subsystem](http://realai.org/course/windows/#windows-subsystem-for-linux) on *Windows*! Installing Ruby and Bundler on [Ubuntu](http://realai.org/course/ubuntu/) is straightforwards:

```bash
sudo apt update
sudo apt install ruby
sudo gem install bundler
```

The main installation step involving Jekyll and other [dependencies](https://pages.github.com/versions/) is hidden behind the line `bundle install`. Depending on the pre-installation state of the system, some libraries may need to be manually installed, such as [ruby-dev](https://packages.ubuntu.com/xenial/ruby-dev), [gcc](https://packages.ubuntu.com/xenial/gcc), [zlib1g-dev](https://packages.ubuntu.com/xenial/zlib1g-dev), etc. Once successfully set up, the Jekyll site can be run locally by the command

```bash
bundle exec jekyll serve
```

### Jekyll

[Jekyll](https://jekyllrb.com/) is a simple software framework that transforms plain text into static websites and blogs. It also powers GitHub Pages.

