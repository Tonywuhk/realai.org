---
permalink: /course/ubuntu/
title: Course | Ubuntu
---
# Ubuntu

[Ubuntu](https://www.ubuntu.com/) is a distribution systems of Linux. It is open source, and based on the Debian architecture. [Canonical Ltd.](https://www.canonical.com/) is the leader of the Ubuntu Project, and maintains the [searchable](https://packages.ubuntu.com/) Ubuntu Package archive. A URL shortcut `http://packages.ubuntu.com/name` can be used to search on package names. The [Official Ubuntu Documentation](https://help.ubuntu.com/) only contains the Server Guide for Long Term Support (LTS) releases. As of August 2017, the [Ubuntu 16.04 Server Guide](https://help.ubuntu.com/lts/serverguide/index.html) is the most recent.

## Package Management

The [apt](https://help.ubuntu.com/lts/serverguide/apt.html) command is a powerful command-line tool, which works with Ubuntu's Advanced Packaging Tool (APT). [Comparing](https://itsfoss.com/apt-vs-apt-get-difference/) with apt-get and apt-cache, it can be said that apt contains the most commonly used options from the two older tools.

## File System

Ubuntu organizes files in a [hierarchical tree](https://help.ubuntu.com/community/LinuxFilesystemTreeOverview). Some standard directories include:

* `/boot` contains files needed to start up the system.
* `/usr/bin` contains executable (binary) files that are usually part of the operating system and installed by its package manager. For example, on a Ubuntu 16.04 virtual machine created from [Google Cloud Engine](http://realai.org/course/google-compute-engine/), both `python` and `python3` are from `/usr/bin`. Better not touch them without using `apt`.
* `/usr/local/bin` contains the binary files that are usually installed by the local administrator, sometimes built from source. They use a “local” directory in order not to be disrupt system behavior.

## Useful Commands

*  [ln -s](https://ss64.com/bash/ln.html) <filename> <linkname> creates a symbolic link to file. On a newly created Ubuntu 16.04 instance, `/usr/bin/python` is a link to `/usr/bin/python2.7`. Removing the link then `sudo ln -s /usr/bin/python3.5 /usr/bin/python` changes the default `python` command to Python 3.5. But messing around in `/usr/bin` is not a good idea, as the change also breaks programs that depend on the old links.
* `cat /etc/lsb-release` shows a machine running Ubuntu 16.04 is codenamed “xenial”.

