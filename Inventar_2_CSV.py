#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_2_CSV.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Zusätzlich mit einer CSV-Funktion
#
##############################################

import platform,multiprocessing,os,time,argparse

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
args = parser.parse_args()

###Variabeln
timestamp=time.time()
inventar={}

###Funktionen
def getdata():
   inventar["name"]=platform.node()
   inventar["nrcpu"]=multiprocessing.cpu_count()
   inventar["system"]=platform.system()
   inventar["release"]=platform.release()
   inventar["machine"]=platform.machine()
   inventar["timestamp"]=int(timestamp)

def showdata():
   print ("Server Angaben\n##############")
   print ("Name:",inventar["name"])
   print ("Nr.CPU:",inventar["nrcpu"])
   print ("System:",inventar["system"])
   print ("Release:",inventar["release"])
   print ("Machine:",inventar["machine"])
   print ("Timestamp:",inventar["timestamp"])

def showcsv():
   print (inventar["name"]+","+str(inventar["nrcpu"])+","+inventar["system"]+","+inventar["release"]+","+inventar["machine"]+","+str(inventar["timestamp"]))

###Daten ausgeben
getdata()
if args.c: showcsv()
else:      showdata()
