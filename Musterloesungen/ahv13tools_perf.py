#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funktion zur Validierung einer 13-stelligen AHV-Nummer
(schweizerische Sozialversicherungsnummer) 

Definition: https://www.bsv.admin.ch/bsv/de/home/sozialversicherungen/ahv/grundlagen-gesetze/ahv-nummer.html
Prüfziffer-Berechnung: https://www.gs1.org/services/how-calculate-check-digit-manually

Für Performance optimierte Versionen.
Zur besseren Vergleichbarkeit für das Timing alle Aufrufe mit normalisiert aufrufen.

@author: rene.degen@inodes.ch
"""

import re
    
def validiere1(ahv13, normalisiert=False):
    if not normalisiert:
        # entferne white space
        ahv13 = ahv13.strip()
        # validiere korrektes Fomat
        if re.match(r'^756\.?\d{4}\.?\d{4}\.?\d{2}$', ahv13):
            pass
        else:
            raise ValueError
        # normalisiere
        ahv13 = re.sub(r'\.', '', ahv13)
    
    # prüfziffer abtrennen
    pruefziffer = int(ahv13[-1])
        
    faktor = 1
    summe = 0
    for ziffer in ahv13[:-1]:
        summe = summe + faktor * int(ziffer)
        faktor = 4 - faktor
    if (rest := summe % 10) == 0:
        errechnete_pz = 0
    else: 
        errechnete_pz = 10 - rest
    return errechnete_pz == pruefziffer


def validiere2(ahv13, normalisiert=False):
    if not normalisiert:
        # entferne white space
        ahv13 = ahv13.strip()
        # validiere korrektes Fomat
        if re.match(r'^756\.?\d{4}\.?\d{4}\.?\d{2}$', ahv13):
            pass
        else:
            raise ValueError
        # normalisiere
        ahv13 = re.sub(r'\.', '', ahv13)
    
    # prüfziffer abtrennen
    pruefziffer = int(ahv13[-1])
        
    faktor = 1
    summe = 0
    for ziffer in ahv13[:-1]:
        summe = summe + faktor * int(ziffer)
        faktor = 4 - faktor
    return ((10 - (summe % 10)) % 10) == pruefziffer


def validiere3(ahv13, normalisiert=False):
    if not normalisiert:
        # entferne white space
        ahv13 = ahv13.strip()
        # validiere korrektes Fomat
        if re.match(r'^756\.?\d{4}\.?\d{4}\.?\d{2}$', ahv13):
            pass
        else:
            raise ValueError
        # normalisiere
        ahv13 = re.sub(r'\.', '', ahv13)
    
    # umwandeln
    ahv13nr = int(ahv13)
    # prüfziffer abtrennen
    pruefziffer = ahv13nr % 10
    ahv13nr //= 10
   
    summe = 0
    faktor = 3
    while ahv13nr > 0:
        summe += (ahv13nr % 10) * faktor
        ahv13nr //= 10
        faktor = 4 - faktor 
    return ((10 - (summe % 10)) % 10) == pruefziffer

if __name__ == "__main__":
    print("Dies ist ein Modul und sollte eingebunden werden")

