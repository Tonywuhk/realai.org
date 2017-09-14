#!/usr/bin/env python

# Standard library imports, sorted alphabetically
import datetime
import urllib.request
import re
import sys

# Third party import
import feedparser

# Constants
BASE_URL = 'http://export.arxiv.org/api/query?id_list='
VALID_INPUT_REGEX = re.compile("^(\d{1,4}\.)?(\d{1,5})$")

def process_id(input):
    """Return the proper paper id to be used in arXiv URL"""
    match = VALID_INPUT_REGEX.match(input)
    if match == None:
        print(r"Paper ID must have (regex) format ^(\d{1,4}\.)?\d{1,5}$")
        exit()

    yymm = format(datetime.date.today(), "%y%m")
    if match.group(1) == None:
        prefix = yymm + "."
    else:
        prefix = yymm[0:(5-len(match.group(1)))] + match.group(1)
    return prefix + match.group(2).rjust(5, '0')

def cite(id):
    """Return full citation from arXiv server based on proper paper id."""
    data = urllib.request.urlopen(BASE_URL + id).read()
    parse = feedparser.parse(data)
    item = parse.entries[0]
    
    dt = datetime.datetime.strptime(item.date[:10], "%Y-%m-%d")
    date = dt.strftime("%Y %B %-d")
    # In Python 3.6 or higher, can also use formatted string literals:
    #
    # date = f'{dt:%Y} {dt:%B} {dt.day}'
    #
    # See https://docs.python.org/3/reference/lexical_analysis.html#f-strings
    
    xauthors = item.authors
    la = len(item.authors)
    
    if la == 2:
        authors = xauthors[0].name + ' and ' + xauthors[1].name
    elif la > 2:
        authors = ''
        for i in range(0, la-1):
            authors = authors + xauthors[i].name + ', '
        authors = authors + 'and ' + xauthors[la-1].name
    else:
        authors = xauthors[0].name

    title = item.title.replace('\n', '')

    # Line breaks before binary operators 
    cite = ('* ' + date + ', ' + authors + '. [' + title + '](https://arxiv.org/abs/'
            + id + '). *arXiv:' + id + '*.')

    return cite
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please supply exactly 1 argument to this script.")
        exit()

    id = process_id(str(sys.argv[1]))
    print(cite(id))
