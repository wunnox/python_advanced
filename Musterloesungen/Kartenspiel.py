#!/usr/bin/env python3
"""
Wir haben folgende Karten
werte = ['Ass', 'König', 'Dame', 'Bube', '10', '9', '8', '7', '6']
farben = ['Herz', 'Ecke', 'Schaufel', 'Kreuz']
Erstellen Sie ein gesamtes Kartenspiel
- mit einem Generator cards()
- mit einer Generator Expression
- mit Hilfe der itertools-Methode product()
"""

werte = ['Ass', 'König', 'Dame', 'Bube', '10', '9', '8', '7', '6']
farben = ['Herz', 'Ecke', 'Schaufel', 'Kreuz']

# der Generator

def karten_generator():
    for wert in werte:
        for farbe in farben:
            yield wert, farbe

# Generator Ausdruck

karten = ((wert, farbe) for wert in werte for farbe in farben)

# mit den itertools

import itertools as it
karten_it = it.product(werte, farben)

# Anwendung
for k in karten_generator():
    print(k, end=' ')
print('')

for k in karten:
    print(k, end=' ')
print('')
    
for k in karten_it:
    print(k, end=' ')
print('')
    
