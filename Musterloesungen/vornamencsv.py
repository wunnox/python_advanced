#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:55:57 2022

@author: rene.degen@inodes.ch

Aufgabe:
Die Datei "bev370od3700.csv" enthält "Alle nach Geschlecht und Geburtsjahr
aggregierten Vornamen von Neugeborenen mit Wohnsitz in der Stadt Zürich seit 1993.""

Geben Sie die 10 häufigsten Vornamen des Jahres 2023 aus

Hier wird das Modul csv verwendet

"""

import csv

quelle='bev370od3700.csv'
limite = 10
auswahljahr = '2023'

anzahl_namen = {}

with open(quelle, newline='',encoding='utf-8-sig') as csvdatei:
    reader = csv.DictReader(csvdatei)
    for eintrag in reader:
        if auswahljahr == None or auswahljahr == eintrag['StichtagDatJahr']:
            name = eintrag['Vorname']
            anzahl = int(eintrag['AnzGebuWir'])
            if name in anzahl_namen:
                anzahl_namen[name] += anzahl
            else:
                anzahl_namen[name] = anzahl

for n in sorted(anzahl_namen, key=anzahl_namen.get, reverse=True):
    limite-=1
    if limite < 0:
        break
    print(n, anzahl_namen[n])
