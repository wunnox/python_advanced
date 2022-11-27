#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 30 14:20:39 2021

@author: rene.degen@inodes.ch
"""

import urllib.request

seite = "https://de.wikipedia.org/wiki/Schweiz"
staedte = ('Bern', 'Basel', 'Freiburg', 'Zürich', 'St. Gallen')
anzahl=dict.fromkeys(staedte,0)

u = urllib.request.urlopen(seite)
zeilen = u.readlines()
u.close()

for zeile in zeilen: 
    zeile=zeile.decode('utf-8')
    for s in staedte:
        anz = zeile.count(s)
        anzahl[s] += anz

for stadt in sorted(anzahl, key=anzahl.get, reverse=True):
    print("{0:<14}{1:>5d}".format(stadt, anzahl[stadt]))
