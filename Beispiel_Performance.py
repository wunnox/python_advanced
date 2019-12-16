#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_Performance.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Script mit Performance-Messung
#
##############################################

import argparse,random

####Parameter auswerten
parser = argparse.ArgumentParser(description='Quersumme berechnen')
parser.add_argument('-p', action='store_true', help="Performance Messung")
args = parser.parse_args()

###Funktionen
def rechner(n):
   a=0
   while n>9: 
      for b in [int(i) for i in str(n)]: a+=b
      n=a
      a=0
   return n
   
###Prozess starten
if args.p:
   #Testmodus
   import profile
   profile.run("rechner(int(1.9891+30))")
else:
   #Normale Funktion
   print ("Die Basiszahl der Sonnenmasse ist:",rechner(int(1.9891+30)))

