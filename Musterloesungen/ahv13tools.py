#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Funktion zur Validierung einer 13-stelligen AHV-Nummer
(schweizerische Sozialversicherungsnummer) 

Definition: https://www.bsv.admin.ch/bsv/de/home/sozialversicherungen/ahv/grundlagen-gesetze/ahv-nummer.html
Prüfziffer-Berechnung: https://www.gs1.org/services/how-calculate-check-digit-manually

@author: rene.degen@inodes.ch
"""

import re
    
def validiere(ahv13, normalisiert=False):
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
        if faktor == 1:
            faktor = 3
        else:
            faktor = 1
    rest = summe % 10
    if rest == 0:
        errechnete_pz = 0
    else: 
        errechnete_pz = 10 - rest
    return errechnete_pz == pruefziffer


def generiere(prefix = 756, nummer = 123456789):
    faktor = 1
    summe = 0
    prefix=str(prefix)
    nummer=str(nummer)
    for ziffer in ''.join((prefix, nummer)):
        summe = summe + faktor * int(ziffer)
        if faktor == 1:
            faktor = 3
        else:
            faktor = 1
    rest = summe % 10
    if rest == 0:
        pz = 0
    else: 
        pz = 10 - rest
    return ''.join((prefix, nummer, str(pz)))
    

if __name__ == "__main__":
    print("Dies ist ein Modul und sollte eingebunden werden")

