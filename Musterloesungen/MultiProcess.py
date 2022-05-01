#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:30:00 2022

@author: rene
"""

from concurrent import futures
from time import time

prozesse = 16
chunk = 5000

max_probe = 100000
pc=[] # Liste für Primzahlenzähler

def primrechner(ps,pe):
    pc=[]
    # print("Suche Primzahlen von",ps,"bis",pe)
    for z in range(ps,pe+1):    
        for z2 in range(2,z):
            if not z%z2: break
        else: pc.append(z)
    return pc

if __name__ == "__main__":
    time0 = time()
    with futures.ProcessPoolExecutor(prozesse) as e:       ### Anzahl Prozesse
        fs = {e.submit(primrechner, *(n,n+chunk-1)): n for n in range(1,max_probe,chunk)}
        for f in futures.as_completed(fs):
            pc.extend(f.result())
    print("Es wurden",len(pc), "Primzahlen gefunden")    ### Abschluss

    print("{:2d}#proc, chunk: {:5d}:  {:8f} Sekunden".format(prozesse, chunk, time() - time0)) 