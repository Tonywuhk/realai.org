---
permalink: /course/ubuntu/
title: Course | Ubuntu
---
# Ubuntu

[Ubuntu](https://www.ubuntu.com/) is a distribution systems of Linux. It is open source, and based on the Debian architecture. [Canonical Ltd.](https://www.canonical.com/) is the leader of the Ubuntu Project, and maintains the [searchable](https://packages.ubuntu.com/) Ubuntu Package archive. A URL shortcut `http://packages.ubuntu.com/name` can be used to search on package names. The [Official Ubuntu Documentation](https://help.ubuntu.com/) only contains the Server Guide for Long Term Support (LTS) releases. As of August 2017, the [Ubuntu 16.04 Server Guide](https://help.ubuntu.com/lts/serverguide/index.html) is the most recent.

## Bash

[GNU Bash](https://www.gnu.org/software/bash/) is the shell used by default in terminals on Ubuntu. `man` is the system's manual pager. `man man` displays the manual page of `man` itself. In `man` you can type `/<regex>` to jump forward using [regular expressions](http://realai.org/course/text-processing/#regular-expressions), and use `n` and `N` to jump forward and backwards.

A command can start with optional variable assignments such as `DISPLAY=:10.0`. This is part of a [simple command expansion](https://www.gnu.org/software/bash/manual/bashref.html#Simple-Command-Expansion), and is also documented in the "SHELL GRAMMAR" section of the man page of `bash`.

[Shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) (aka hashbang) at the beginning of a script allows it to be run as a program. If a Python script is intended for use as a bash command, it is a good practice to let its first line be `#!/usr/bin/env python`, where `env` makes sure python is found in case it's not in exactly the default location on the current Unix systems.

## Package Management

The [apt](https://help.ubuntu.com/lts/serverguide/apt.html) command is a powerful command-line tool, which works with Ubuntu's Advanced Packaging Tool (APT). [Comparing](https://itsfoss.com/apt-vs-apt-get-difference/) with apt-get and apt-cache, it can be said that apt contains the most commonly used options from the two older tools.

## File System

Ubuntu organizes files in a [hierarchical tree](https://help.ubuntu.com/community/LinuxFilesystemTreeOverview). Some standard directories include:

* `/boot` contains files needed to start up the system.
* `/tmp` is a place for temporary files. It is cleaned automatically, for example, by [tmpreaper](http://manpages.ubuntu.com/manpages/xenial/man8/tmpreaper.8.html).
* `/usr/bin` contains executable (binary) files that are usually part of the operating system and installed by its package manager. For example, on a Ubuntu 16.04 virtual machine created from [Google Cloud Engine](http://realai.org/course/google-cloud-platform/#google-compute-engine), both `python` and `python3` are from `/usr/bin`. Better not touch them without using `apt`.
* `/usr/local/bin` contains the binary files that are usually installed by the local administrator, sometimes built from source. They use a “local” directory in order not to be disrupt system behavior.

## User Management

* `sudo adduser <newuser>` adds a new user from a non-root user with sudo privileges
* `su <username>` switches to the account of "username"

## Useful Commands

*  `ln -s <filename> <linkname>` creates a symbolic link to file ([man page](https://ss64.com/bash/ln.html)). On a new Ubuntu 16.04 instance, `/usr/bin/python` is a link to `/usr/bin/python2.7`. Removing the link then `sudo ln -s /usr/bin/python3.5 /usr/bin/python` changes the default `python` command to Python 3.5. But messing around in `/usr/bin` is not a good idea, as the change also breaks programs that depend on the old links.
* `cat /etc/lsb-release` shows a machine running Ubuntu 16.04 is codenamed “xenial”.

