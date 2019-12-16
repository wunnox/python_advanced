#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_Testing.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Script mit Testing-Funktion
#
##############################################

import platform,os,time,argparse

####Parameter auswerten
parser = argparse.ArgumentParser(description='Quersumme berechnen')
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument('-s', metavar='Nummern', nargs='+', type=int, help="Zahlen zur Berechnung der Quadratsumme eingeben")
group.add_argument('-t', action='store_true', help="Testmodus")
args = parser.parse_args()

###Funktion
def quersumme(s):
     """ Errechnet die Quersumme einer Liste

     >>> quersumme ([1, 2, 3])      # 1 + 2 + 3
     6
     >>> quersumme ([10,20,30])     # 10+20+30
     60
     """
     return sum(s)

if args.t:
   #Testmodus
   import doctest
   doctest.testmod(verbose=True)
   quersumme([1,2,3])
   quersumme([10,20,30])
else:
   #Normale Funktion
   print(quersumme(args.s))
