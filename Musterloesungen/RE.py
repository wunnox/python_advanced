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
allesVokale = set()
anfangEndeIdentisch = set()
anfangVokal = set()
doppelt = set()
ddoppelt = set()
sonderzeichen = set()

with open(quelle, newline='',encoding='utf-8-sig') as csvdatei:
    reader = csv.DictReader(csvdatei)
    for eintrag in filter(lambda x: auswahljahr==None or auswahljahr == x['StichtagDatJahr'], \
                          reader):
        vorname=eintrag['Vorname']
        alle.append(vorname)
        # Name enthält alle Vokale
	    # Hinweis: muss mit lower() normalisiert werden,
        # da sonst z.B. A und a doppelt gezählt werden
        if len(set(re.findall(r"[aeiou]", vorname.lower(), re.IGNORECASE)))==5:
            if vorname not in allesVokale:
                allesVokale.add(vorname)
        # Der erste und letzte Buchstabe sind identisch
        if re.fullmatch(r"(.).*\1", vorname, re.IGNORECASE):
            anfangEndeIdentisch.add(vorname)
        # Der erste Buchstabe ist ein Vokal
        if re.match(r"[aeiou]", vorname, re.IGNORECASE):
            anfangVokal.add(vorname)
        # Doppelter Buchstabe
        if re.search(r"(.)\1", vorname, re.IGNORECASE):
            doppelt.add(vorname)
        # Doppelter doppelter Buchstabe
        if re.search(r"(.)\1.*(.)\2", vorname, re.IGNORECASE):
            ddoppelt.add(vorname)
        # Enthält Sonderzeichen, hier alles was nicht A-Z oder - ist
        if re.search(r"[^a-z -]", vorname, re.IGNORECASE):
            sonderzeichen.add(vorname)


print(f"Mit allen Vokalen:               {len(allesVokale):>4d}")
print(f"Anfangs- und Endbuchstabe gleich:{len(anfangEndeIdentisch):>4d}")
print(f"Beginnt mit Vokal:               {len(anfangVokal):>4d}")
print(f"doppelter Buchstabe:             {len(doppelt):>4d}")
print(f"doppelt doppelte Buchstaben:     {len(ddoppelt):>4d}")
print(f"Sonderzeichen                    {len(sonderzeichen):>4d}")

