#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 13:39:04 2024

Das Bundesamt für Statistik veröffentlicht jedes Jahr die Vornamen der aktuellen
Wohnbevölkerung. Die aktuelle Datei befindet sich unter
https://www.bfs.admin.ch/bfs/de/home/statistiken/bevoelkerung/geburten-todesfaelle/namen-schweiz.html
(weiterführende Informationen)

Die entsprechende Datei heisst dann ts-x-01.04.00.10.csv oder ts-x-01.04.00.11.csv
abhängig davon, ob weibliche oder männliche Vornamen ausgewählt werden.

Wir erstellen eine Grafik, welche die Anzahl der Geburten mit einem Namen visualisiert.

@author: rene.degen@inodes.ch
"""

import csv
import matplotlib.pyplot as plt

eingabe_datei = {
    'f': 'ts-x-01.04.00.10.csv',
    'm': 'ts-x-01.04.00.11.csv'
    }

sex='m'
pruef_name='Alain'

x = []
y = []
maxlength=0

with open(eingabe_datei[sex], encoding='utf-8-sig') as datasource:
    data=csv.reader(datasource, delimiter=',', quotechar='"')
    next(data)
    for year,name,by,anzahl,obs in data:
        anzahl=int(anzahl)
        by=int(by)
        if name == pruef_name:
            x.append(by)
            y.append(anzahl)

plt.bar(x,y)
plt.xlabel('Jahr')
plt.ylabel('Anzahl')
plt.title(f'Häufigkeit "{pruef_name}" nach Geburtsjahr')
plt.savefig(f'{pruef_name}.png')
plt.show()
