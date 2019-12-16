#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_3_Read-Json.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.11.2017
#
# Purpose: Einlesen eines Json Files
#
##############################################

import json

###Funktion
def read_json_file():
   inventar=json.load(open('inventar.json'))
   return inventar

def showdata(inventar):
   print ("Server Angaben\n##############")
   for i in inventar:
      print ("Name:",i["name"])
      print ("Nr.CPU:",i["nrcpu"])
      print ("System:",i["system"])
      print ("Release:",i["release"])
      print ("Machine:",i["machine"])
      print ("Timestamp:",i["timestamp"])
      print ("#")

###Daten ausgeben
inventar=read_json_file()
showdata(inventar)
