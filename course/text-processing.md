---
permalink: /course/text-processing/
title: Text Processing
---
# Text Processing

[Grep](https://www.gnu.org/software/grep/) is a command-line utility that searches input files for lines containing a match to a specified pattern. Its name comes from "**g**lobally search a **r**egular **e**xpression and **p**rint".

* [Manual](https://www.gnu.org/software/grep/manual/grep.html) for GNU Grep 3.0

[sed](https://www.gnu.org/software/sed/) (*s*tream *ed*itor) is a non-interactive command-line text editor. It has a one-page [HTML manual](https://www.gnu.org/software/sed/manual/sed.html).

## Useful Tricks

* `grep -r --include=*.md "^AGI"`: search all markdown files in all directories to find lines that start with "AGI"
* `sed -i "s#/tools/#/#g" course/*.md`: replace all occurrences of `/tools/` by `/` in all markdown files contained in director `course/`

