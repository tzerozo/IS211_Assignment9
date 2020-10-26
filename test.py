#!/usr/bin/env python
# coding: utf-8

#Lang Tuang Assignment9
#10/25/2020 ..It seems easy but was really not easy as you have to know HTML 
# and how to use "Browser's Developer Tools" to find out what you want.

import urllib
import urllib.request
from bs4 import BeautifulSoup
#link = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"

def main():
  link = 'https://www.nasdaq.com/market-activity/stocks/aapl/historical'
  view = urllib.request.urlopen(link)
  print("test")
  Soup = BeautifulSoup(view.read(), features='lxml')


  table = Soup.find("tbody", class_='historical-data__table-body')
  rows  = table.findAll('tr')

  
  for row in rows:
    th = row.find("th")
    td = row.find("td")
    dates = th[0].text.strip()
    closeprice = td[0].text.strip()
    print(dates, closeprice)

main()
