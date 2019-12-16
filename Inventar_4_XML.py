#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_4_XML.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Kann Daten als XML Datei sichern
#
##############################################

import platform,multiprocessing,os,time,argparse,json,xml.dom.minidom

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
parser.add_argument('-j', action='store_true', help="Daten in Json-Format ausgeben")
parser.add_argument('-l', action='store_true', help="Daten in Klar-Text  ausgeben(Default)")
parser.add_argument('-J', action='store_true', help="Daten in ein Json-File schreiben")
parser.add_argument('-X', action='store_true', help="Daten in ein XML-File schreiben")
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

def write_json_file():
   with open('inventar.json', 'w') as outfile:
      json.dump(inventar_liste, outfile)

def write_xml_file():
   ###Variabeln
   comment="Server Inventardaten"

   ###Erste Stuffe erstellen
   doc = xml.dom.minidom.Document()
   doc.appendChild(doc.createComment(comment))
   erste_stuffe = doc.createElement("inventar")
   doc.appendChild(erste_stuffe)
 
   for i in inventar_liste:
      ###Zweite Stuffe erstellen
      zweite_stuffe = doc.createElement("server")
      zweite_stuffe.setAttribute( "name", i["name"])
      erste_stuffe.appendChild(zweite_stuffe)

      ###Datenelemente erstellen
      for name,value in i.items():
         # Element erstellen
         element_name = doc.createElement(name)
         zweite_stuffe.appendChild(element_name)
 
         # Element Wert hinzufügen
         element_wert = doc.createTextNode(str(value))
         element_name.appendChild(element_wert)
 
   ###Daten in File schreiben
   doc.writexml( open('inventar.xml', 'w'),
      indent="  ",
      addindent="  ",
      newl='\n')
   doc.unlink()

###Daten ausgeben
getdata()
if args.c: showcsv()
elif args.j: show_json()
else:      showdata()
if args.J: write_json_file()
if args.X: write_xml_file()

