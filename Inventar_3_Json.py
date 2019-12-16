#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_3_Json.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Zusätzlich mit einer Json-Funktion
#
##############################################

import platform,multiprocessing,os,time,argparse,json

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
parser.add_argument('-j', action='store_true', help="Daten in Json-Format ausgeben")
parser.add_argument('-J', action='store_true', help="Daten in ein Json-File schreiben")
parser.add_argument('-l', action='store_true', help="Daten in Klar-Text  ausgeben(Default)")
args = parser.parse_args()

###Variabeln
timestamp=time.time()
inventar={}
inventar_liste=[]

###Funktionen
def getdata():
   inventar["name"]=platform.node()
   inventar["nrcpu"]=multiprocessing.cpu_count()
   inventar["system"]=platform.system()
   inventar["release"]=platform.release()
   inventar["machine"]=platform.machine()
   inventar["timestamp"]=int(timestamp)
   inventar_liste.append(inventar)

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

def show_json():
   #Json-Ausgabe erstellen
   jsonData = json.dumps(inventar)
   print (jsonData)

def write_json_file():
   with open('inventar.json', 'w') as outfile:
      json.dump(inventar_liste, outfile)

###Daten ausgeben
getdata()
if args.c: showcsv()
elif args.j: show_json()
elif args.J: write_json_file()
else:      showdata()
