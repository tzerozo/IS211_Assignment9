#!/usr/bin/env python
# coding: utf-8

#Lang Tuang Assignment9 AppleStock
#10/25/2020 ..
#Nasdas link came up empty.
#Had to use try | except for one row with empty data.continue
#will load up to June 8,2019 (the full page browser load before scrolling)

import urllib
import urllib.request
from bs4 import BeautifulSoup
link = "https://finance.yahoo.com/quote/AAPL/history?p=AAPL"
view = urllib.request.urlopen(link)
Soup = BeautifulSoup(view.read(), features="html5lib")


table_rows = Soup.findAll ("tr", class_="BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)")
counter = 0
for row in table_rows:
  try:
    td = row.find_all("td")
    dates = td[0].text.strip()
    closeprice = td[4].text.strip()
    print(f"Date = {dates} | Close Price = {closeprice}")
    counter += 1
  except:
    continue

print("Total Row", counter)

      
