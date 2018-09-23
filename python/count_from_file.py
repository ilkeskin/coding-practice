#!/usr/bin/env python

name_count = {}
with open("/home/ilkeskin/code/nameslist.txt") as names:
    for name in names:
        if name.strip() in name_count:
            name_count[name.strip()] += 1
        else:
            name_count[name.strip()] = 1

print name_count

cat_count = {}
with open("/home/ilkeskin/code/Training_01.txt") as cats:
    for cat in cats:
        if cat.split('/')[2] in cat_count:
            cat_count[cat.split('/')[2]] += 1
        else:
            cat_count[cat.split('/')[2]] = 1

print cat_count
