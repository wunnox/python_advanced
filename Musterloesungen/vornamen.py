#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:55:57 2022

@author: rene.degen@inodes.ch

Aufgabe:
Die Datei "bev370od3700.csv" enthält "Alle nach Geschlecht und Geburtsjahr
aggregierten Vornamen von Neugeborenen mit Wohnsitz in der Stadt Zürich seit 1993.""

Geben Sie die 10 häufigsten Vornamen des Jahres 2023 aus

Lösung mit einfachem Einlesen

"""

quelle='bev370od3700.csv'
kopfzeile = True
limite = 10
auswahljahr = 2023

anzahl_namen = {}

with open(quelle) as datei:
    for eintrag in datei:
        if kopfzeile:
            kopfzeile = False
            continue
        jahr, name, geschlecht, anzahl = eintrag.strip().split(',')
        jahr = int(jahr)
        if auswahljahr == None or auswahljahr == jahr:
            name=name[1:-1]
            geschlecht=geschlecht[1:1]
            anzahl = int(anzahl)
            if name in anzahl_namen:
                anzahl_namen[name] += anzahl
            else:
                anzahl_namen[name] = anzahl

for n in sorted(anzahl_namen, key=anzahl_namen.get, reverse=True):
    limite-=1
    if limite < 0:
        break
    print(n, anzahl_namen[n])
