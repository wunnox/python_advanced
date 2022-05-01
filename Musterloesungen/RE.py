#!/usr/bin/env python3
"""
Wir verwenden nochmals die Datei "BEV370OD3700.csv" und werten Vornamen aus.
Beachte: Gross-/Kleinschreibung darf keine Rolle spielen
- Wie viele Vornamen enthalten alle Vokale?
- Bei wie vielen Vornamen ist der erste und letzte Buchstabe identisch?
- Wie viele Vornamen beginnen mit einem Vokal?
- Wie viele Vornamen enthalten doppelte Buchstaben (die identischen Buchstaben folgen unmittelbar hintereinander)?
- Wie viele sogar zwei Mal doppelte Buchstaben?

"""

import csv
import re

quelle='BEV370OD3700.csv'
auswahljahr = None #'2020'

alle = []   # nur zum Debuggen
allesVokale = []
anfangEndeIdentisch = []
anfangVokal = []
doppelt = []
ddoppelt = []
sonderzeichen = []

with open(quelle, newline='',encoding='utf-8-sig') as csvdatei:
    reader = csv.DictReader(csvdatei)
    for eintrag in filter(lambda x: auswahljahr==None or auswahljahr == x['StichtagDatJahr'], \
                          reader):
        vorname=eintrag['Vorname']
        alle.append(vorname)
        # Name enthält alle Vokale
	# Hinweis: muss mit lower() normalisiert werden, da sonst z.B. A und a doppelt gezählt werden
        if len(set(re.findall(r"[aeiou]", vorname.lower(), re.IGNORECASE)))==5:
            if vorname not in allesVokale:
                allesVokale.append(vorname)
        # Der erste und letzte Buchstabe sind identisch
        if re.fullmatch(r"(.).*\1", vorname, re.I):
            anfangEndeIdentisch.append(vorname)
        # Der erste Buchstabe ist ein Vokal
        if re.match(r"[aeiou]", vorname, re.I):
            anfangVokal.append(vorname)
        # Doppelter Buchstabe
        if re.search(r"(.)\1", vorname, re.I):
            doppelt.append(vorname)
        # Doppelter doppelter Buchstabe
        if re.search(r"(.)\1.*(.)\2", vorname, re.I):
            ddoppelt.append(vorname)
        # Enthält Sonderzeichen, hier alles was nicht A-Z oder - ist
        if re.search(r"[^a-z-]", vorname, re.I):
            sonderzeichen.append(vorname)


print("Mit allen Vokalen:               {:>4d}".format(len(set(allesVokale))))	# set hier redundant, da Duplikate nicht Eingetragen werden
print("Anfangs- und Endbuchstabe gleich:{:>4d}".format(len(set(anfangEndeIdentisch))))
print("Beginnt mit Vokal:               {:>4d}".format(len(set(anfangVokal))))
print("doppelter Buchstabe:             {:>4d}".format(len(set(doppelt))))
print("doppelt doppelte Buchstaben:     {:>4d}".format(len(set(ddoppelt))))
print("Sonderzeichen                    {:>4d}".format(len(set(sonderzeichen))))

