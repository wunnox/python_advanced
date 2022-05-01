#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:55:57 2022

@author: rene.degen@inodes.ch

Aufgabe:
Die Datei "BEV370OD3700.csv" enthält "Alle nach Geschlecht und Geburtsjahr
aggregierten Vornamen von Neugeborenen mit Wohnsitz in der Stadt Zürich seit 1993.""

Geben Sie die 10 häufigsten Vornamen des Jahres 2020 aus

Hier wird das Modul csv und das Collection Modul verwendet

"""

import collections
import csv

quelle='BEV370OD3700.csv'
limite = 10
auswahljahr = '2020'

anzahl_namen = collections.Counter()

with open(quelle, newline='',encoding='utf-8-sig') as csvdatei:
    reader = csv.DictReader(csvdatei)
    for eintrag in filter(lambda x: auswahljahr==None or auswahljahr == x['StichtagDatJahr'], \
                          reader):
        name = eintrag['Vorname']
        anzahl = int(eintrag['AnzGebuWir'])
        anzahl_namen[name] += anzahl
             
for n in anzahl_namen.most_common(limite):
    print(*n)