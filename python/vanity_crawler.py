#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://www.vanityfair.com/style/2017/06/serena-williams-cover-story")
soup = bs(r.text, "html.parser")
sections = soup.find_all("section", class_="content_section")
print sections
pars = []
for section in sections:
    pars.append(section.find_all("p"))
print pars
for par in pars:
    print par.string
