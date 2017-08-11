---
permalink: /course/text-processing/
title: Text Processing
---
# Text Processing

[Grep](https://www.gnu.org/software/grep/) is a command-line utility that searches input files for lines containing a match to a specified pattern. Its name comes from "**g**lobally search a **r**egular **e**xpression and **p**rint".

* [Manual](https://www.gnu.org/software/grep/manual/grep.html) for GNU Grep 3.0

[sed](https://www.gnu.org/software/sed/) (*s*tream *ed*itor) is a non-interactive command-line text editor. It has a one-page [HTML manual](https://www.gnu.org/software/sed/manual/sed.html).

## Regular Expressions

A [regular expression](https://en.wikipedia.org/wiki/Regular_expression), regex or regexp is a sequence of characters that define a search pattern. [Learn Regex The Easy Way](https://github.com/zeeshanu/learn-regex) is a one-page guide. As an example, the regex `^(\d{1,4}\.)?(\d{1,5})$` ([test it](https://regex101.com/r/BIzVtN/1) on [regex101.com](https://regex101.com)) defines a pattern that optionally has a prefix of 1-4 digits followed by a dot, then followed by a mandatory string of 1-5 digits.

## Useful Tricks

* `grep -r --include=*.md "^AGI"`: search all markdown files in all directories to find lines that start with "AGI"
* `sed -i "s#/tools/#/#g" course/*.md`: replace all occurrences of `/tools/` by `/` in all markdown files contained in director `course/`

