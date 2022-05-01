#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 22 16:55:57 2022

@author: rene.degen@inodes.ch

Aufgabe:
Die Datei "BEV370OD3700.csv" enthält "Alle nach Geschlecht und Geburtsjahr
aggregierten Vornamen von Neugeborenen mit Wohnsitz in der Stadt Zürich seit 1993.""

Geben Sie die 10 häufigsten Vornamen des Jahres 2020 aus

Hier wird das Modul csv verwendet

"""

import csv
import sqlite3

quelle='BEV370OD3700.csv'

# Verbindung und Cursor erzeugen
connection = sqlite3.connect("vornamenZH.db")
cursor = connection.cursor()

with open(quelle, newline='',encoding='utf-8-sig') as csvdatei:
    reader = csv.DictReader(csvdatei)
    for eintrag in reader:
        jahr,name,geschlecht,anzahl = \
            int(eintrag['StichtagDatJahr']), \
            eintrag['Vorname'], \
            eintrag['SexLang'], \
            int(eintrag['AnzGebuWir'])
        
        cursor.execute("""
                       INSERT INTO vorname VALUES
                       (?, ?, ?, ?)
                       """, (jahr, name, geschlecht, anzahl))
   
# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()         
