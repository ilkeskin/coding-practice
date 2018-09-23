#!/usr/bin/env python

import requests
from bs4 import BeautifulSoup as bs

r = requests.get("http://www.faz.net")
soup = bs(r.text, "html.parser")

headlines = [el.string.strip() for el in soup.find_all("span", class_="tsr-Base_HeadlineText")]
headlines = list(set(headlines))

for headline in headlines:
    print headline
