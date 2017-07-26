---
permalink: /tools/vim/
title: Tools | Vim
---
# Vim

[Vim](http://www.vim.org/) is a text editor built for editing efficiency, but is also known for having a steep learning curve. In most UNIX systems, type `vi` to launch the editor, or type `vimtutor` for a brief overview.

## Links

* [A Great Vim Cheat Sheet](http://vimsheet.com/)
* [Basic vi Commands](https://www.cs.colostate.edu/helpdocs/vi.html)
* [Vim Cheat Sheet](https://vim.rtorr.com/)

## Useful Tricks

### Search and Replace

* Type `:%s/old/new/gc` to replace all occurrences of the string "old" with the string "new" in the file, with confirmation prompts
* Use another separator such as `#` if the strings contain the character `/`

### Changing Letter Case

* Type `gUU` to change all letters in the current line to upper case
* Type `guu` to change all letters in the current line to lower case 
* Type `g~~` to switch the case of all letters in the current line

### Multi-Line Insertion

* Use or send key shortcut `Ctrl+V` to start visual block mode
* Hit `j` multiple times to select several lines
* Hit `I` and insert some text at the beginning of the first line
* Hit `Esc` to exit visual block mode, the inserted text will appear shortly

