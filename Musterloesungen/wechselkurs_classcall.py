#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 09:16:54 2022

@author: rene.degen@inodes.ch

Erstellen Sie einige Funktionen inEuro, inUSD, etc. mit der der Preis eines Frankenbetrags in der entsprechenden Währung ausgedrückt werden kann. Verwenden Sie dafür eine Klasse Wechselkurs, dessen Konstruktor den gültigen Wechselkurs als Parameter erhält.
Verwendung:
inEuro = Wechselkurs(0.9584)
print(100,"CHF in Euro sind:" inEuro(100)

Hinweis: Verwenden Sie die magic method __call__()

"""

class Wechselkurs:
    def __init__(self, kurs):
        self.kurs = kurs
        
    def __call__(self, betrag):
        return betrag * self.kurs
    
inEuro = Wechselkurs(0.9584)
inUSD = Wechselkurs(1.0798)


print ('{0:>8}{1:>8}{2:>8}'.format('CHF', '€', '$'))

for betrag in [1,50, 200]:
    print('{0:8d}{1:8.2f}{2:8.2f}'.format(betrag, inEuro(betrag), inUSD(betrag)) )
