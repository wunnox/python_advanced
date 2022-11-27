#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:30:00 2022

@author: rene.degen@inodes.ch
"""

from time import time

pc=[]  # Liste für Primzahlenzähler
max_probe = 100000

def primrechner(ps,pe):
    # print("Suche Primzahlen von",ps,"bis",pe)
    for z in range(ps,pe+1):    
        for z2 in range(2,z):
            if not z%z2:            
                break
        else:
            pc.append(z)

time0 = time()
primrechner(1,max_probe)                             ### Prozess starten

print("Es wurden",len(pc), "Primzahlen gefunden")    ### Abschluss

print("{:8f} Sekunden".format(time() - time0)) 
