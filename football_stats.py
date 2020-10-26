#!/usr/bin/env python
# coding: utf-8

#Lang Tuang Assignment9
#10/25/2020 ..It seems easy but was really not easy as you have to know HTML 
# and how to use "Browser's Developer Tools" to find out what you want.
#(e.g tr, the player name was anchor, the table body class name, etc....)

import urllib
import urllib.request
from bs4 import BeautifulSoup
link = "https://www.cbssports.com/nfl/stats/player/passing/nfl/regular/qualifiers/?sortcol=td&sortdir=descending"
view = urllib.request.urlopen(link)
Soup = BeautifulSoup(view.read(), features="lxml")

best_players = []
table_rows = Soup.findAll ("tr", class_="TableBase-bodyTr")
counter = 1

for row in table_rows:
    td = row.find_all("td")
    name = td[0].find('a').text.strip()
    touchdowns = td[8].text.strip()
    print(f"Name = {name} | TDs = {touchdowns}")
    counter = counter + 1
    if counter == 20:
      break

print ("You printed the top 20 best players")



