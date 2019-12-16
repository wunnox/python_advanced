#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_OO_3_Json.py
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

import platform,os,time,argparse,json

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
parser.add_argument('-j', action='store_true', help="Daten in Json-Format ausgeben")
parser.add_argument('-J', action='store_true', help="Daten in Json-Datei schreiben")
args = parser.parse_args()

####Variablen
server=''

####Classes
class Server:
  #Class variable
  timestamp=time.time()

  #Constructor Methode
  def __init__(self,name):
      #Attribute
      self.name=name
      self.nrcpu=0
      self.system=''
      self.release=''
      self.machine=''

  #Weitere Methode
  def showdata(self):
      print ("Name:", self.name)
      print ("Nr.CPU:", self.nrcpu)
      print ("System:", self.system)
      print ("Release:", self.release)
      print ("Machine:", self.machine)
      print ("Timestamp:", int(self.timestamp))

  #Weitere Methode
  def showcsv(self):
      return (self.name+","+str(self.nrcpu)+","+self.system+","+self.release+","+self.machine+","+str(int(self.timestamp)))

  def make_inventar(self):
     self.inventar={}
     self.inventar_liste=[]
     self.inventar["name"]=self.name
     self.inventar["nrcpu"]=self.nrcpu
     self.inventar["system"]=self.system
     self.inventar["release"]=self.release
     self.inventar["machine"]=self.machine
     self.inventar["timestamp"]=int(self.timestamp)
     self.inventar_liste.append(self.inventar)

  def show_json(self):
      #Json-Ausgabe erstellen
      self.make_inventar()
      jsonData = json.dumps(self.inventar)
      return (jsonData)

  def write_json_file(self):
      self.make_inventar()
      with open('inventar.json', 'w') as outfile:
         json.dump(self.inventar_liste, outfile)

####Objekt erfassen
server=Server(platform.node())

####Basis Daten erfassen
server.nrcpu=os.cpu_count()
server.system=platform.system()
server.release=platform.release()
server.machine=platform.machine()

####Daten ausgeben
if args.c: print(server.showcsv())
elif args.j: print(server.show_json())
elif args.J: server.write_json_file()
else:      server.showdata()
