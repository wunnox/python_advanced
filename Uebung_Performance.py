#!/usr/local/bin/python3
##############################################
#
# Name: U7.2_PrimRechner_Single.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.07.2017
#
# Purpose: Errechnet die Primzahlen innerhalb eines definierten Zahlenbereiches
#
##############################################

import argparse

####Parameter auswerten
parser = argparse.ArgumentParser(description='Quersumme berechnen')
parser.add_argument('-p', action='store_true', help="Performance Messung")
args = parser.parse_args()

###Variabeln
pc=[]  #Liste für Primzahlenzähler

###Funkdtionen
def primrechner(ps,pe):
   print("Suche Primzahlen von",ps,"bis",pe)
   for z in range(ps,pe+1):
      pc.append(z)
      for z2 in range(2,z):
         if not z%z2: 
            pc.remove(z)
            break

###Prozess starten
if args.p:
   #Testmodus
   import profile
   profile.run("primrechner(1,30000)")
else:
   primrechner(1,30000)

###Abschluss
print("Es wurden",len(pc), "Primzahlen gefunden")
