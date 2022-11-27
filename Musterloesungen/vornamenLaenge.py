#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:55:57 2022

@author: rene.degen@inodes.ch

Die Datei "BEV370OD3700.csv" enthält "Alle nach Geschlecht und Geburtsjahr
aggregierten Vornamen von Neugeborenen mit Wohnsitz in der Stadt Zürich seit 1993.""

Vermutung: Die Namen werden immer kürzer. Zeigen wir das mit einer kleinen Grafik

"""

import csv
import collections
import matplotlib.pyplot as plt

quelle='BEV370OD3700.csv'

laengen = collections.defaultdict(lambda: {'anzN':0, 'sumNL':0})

with open(quelle, newline='',encoding='utf-8-sig') as csvdatei:
    reader = csv.DictReader(csvdatei)
    for eintrag in reader:
        jahr = int(eintrag['StichtagDatJahr'])
        anzahl = int(eintrag['AnzGebuWir'])
        laenge = len(eintrag['Vorname'])
        
        laengen[jahr]['anzN'] += anzahl
        laengen[jahr]['sumNL']+= (anzahl*laenge)

# Plot
jahre = sorted(laengen.keys())
l_avg = list(map(lambda j: laengen[j]['sumNL']/laengen[j]['anzN'], jahre))

plt.plot(jahre,l_avg)
plt.xlabel("Jahr")
plt.ylabel("Länge (Durchschnitt)")
plt.xticks([min(jahre), max(jahre)])
plt.show()
