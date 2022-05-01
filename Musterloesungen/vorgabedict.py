#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 28 09:18:52 2022

@author: rene.degen@inodes.ch

Erstellen sie eine Klasse vorgabedict, die von dict erbt und dessen Konstruktor einen Namensparameter vorgabe erlaubt.Hinweis: der Zugriff auf einen nicht existierenden Schlüssel ruft die magic method __missing__() auf.

Hinweis: Dies soll nur als einfaches Beispiel gelten, im Modul collections gibt es das bereits
"""

class vorgabedict(dict):
    
    def __init__(self, vorgabe):
        self.vorgabe = vorgabe
    
    def __missing__(self, key):
        return self.vorgabe
    
    
d=vorgabedict(0)
# d={}

print(d)

d['key'] = 5
d['nochnicht'] += 2


print('key:', d['key'])
print('nochnicht:', d['nochnicht'])
print('nonexists:', d['nonexists'])
