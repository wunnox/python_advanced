#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:59:49 2022

@author: rene.degen@inodes.ch

Collatz-Problem: Zahlenfolge, die nach einem einfachen Bildungsgesetz konstruiert werden:
- Beginne mit einer natürlichen Zahl (n>0)
- Ist n gerade, fahre mit n/2 weiter
- Ist n ungerade, nimm als nächstes 3n + 1
- Den Vorgang wiederholen mit der erhaltenen Zahl
Collatz-Vermutung: jede so konstruierte Zahlenfolge mündet in den Zyklus 4, 2, 1 unabhängig von der Startzahl n>0
Geben Sie die Zahlenfolge und die Anzahl Schritte aus
"""

zahl = int(input('Gib eine Zahl ein: -> '))

folge = [zahl]

if zahl > 0:
    while zahl != 1:
        if zahl % 2 == 0:
            zahl //= 2
        else:
            zahl = zahl * 3 + 1
        folge.append(zahl)
        
print(str(folge)[1:-1])
print(len(folge), 'Schritte')



