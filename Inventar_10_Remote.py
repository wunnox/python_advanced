#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_10_Remote.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Kann Daten von Remote Servern laden
#
##############################################

import platform,multiprocessing,os,time,argparse,json
from Inventar_10_ssh import remote_daten_laden

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
parser.add_argument('-j', action='store_true', help="Daten in Json-Format ausgeben")
parser.add_argument('-l', action='store_true', help="Daten in Klar-Text  ausgeben(Default)")
parser.add_argument('-r', action='store_true', help="Daten von Remote Server abholen")
parser.add_argument('-J', action='store_true', help="Daten in ein Json-File schreiben")
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
   jsonData = json.dumps(inventar_liste)
   print (jsonData)

def getdata_remote():
   adressen=[["kurs0","172.16.18.15","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"],["kurs0","172.16.18.12","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"],["kurs0","172.16.18.10","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"],["kurs0","172.16.18.16","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"],["kurs0","172.16.18.17","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"],["kurs0","172.16.18.18","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"],["kurs0","172.16.18.19","/home/kurs0/Beispiele_Kurs/Inventar_3_Json.py -j"]]
   for adr in adressen:
      inventar_remote=remote_daten_laden(adr[0],adr[1],adr[2])
      inventar_liste.append(json.loads(inventar_remote))

def write_json_file():
   with open('inventar.json', 'w') as outfile:
      json.dump(inventar_liste, outfile)

###Daten ausgeben
getdata()
if args.r: getdata_remote()
if args.c: showcsv()
elif args.j: show_json()
else:      showdata()
if args.J: write_json_file()
