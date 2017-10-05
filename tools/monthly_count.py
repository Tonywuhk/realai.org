#!/usr/bin/env python

import sys
from datetime import datetime
from pathlib import Path

YEARS = ['2017', '2016', '2015', '2014']
MONTHS = ['December', 'November', 'October', 'September',
          'August', 'July', 'June', 'May',
          'April', 'March', 'February', 'January']

def monthly_count(text):
    """Summarizes occurrences of year-month strings

    Args:
      text: input text

    Output:
      A summary table where each numerical entry is the
      number of occurrences of a particular string in
      the form of "YYYY Month"
    """
    totals = {}

    print()
    print('Month     2017 2016 2015 2014')
    print('-----------------------------')

    for month in MONTHS:
        print(month.ljust(9), end='')
        for year in YEARS:
            yy_mm = year + ' ' + month
            count = text.count(yy_mm)
            if year in totals:
                totals[year] += count
            else:
                totals[year] = 0
 
            if datetime.today() < datetime.strptime(yy_mm, "%Y %B"):
                count = '--'
            print("{:>5}".format(count), end='')
        print()
    print('-----------------------------')
    print('Total    ', end='')
    for year in YEARS:
        print("{:>5}".format(totals[year]), end='')
    print('\n')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Please supply exactly 1 argument to this script.")
        exit()

    my_file = Path(sys.argv[1])
    if my_file.is_file():
        text = my_file.read_text()
        monthly_count(text)
    else:
        print("Cannot find file: '{}'".format(sys.argv[1]))

