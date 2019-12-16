#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_OO_4_XML.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Zusätzlich mit einer XML-Funktion
#
##############################################

import platform,os,time,argparse,json,xml.dom.minidom

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
parser.add_argument('-j', action='store_true', help="Daten in Json-Format ausgeben")
parser.add_argument('-J', action='store_true', help="Daten in Json-Datei schreiben")
parser.add_argument('-X', action='store_true', help="Daten in XML-Datei schreiben")
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

  def write_xml_file(self):
      self.make_inventar()
      ###Variabeln
      comment="Server Inventardaten"

      ###Erste Stuffe erstellen
      doc = xml.dom.minidom.Document()
      doc.appendChild(doc.createComment(comment))
      erste_stuffe = doc.createElement("inventar")
      doc.appendChild(erste_stuffe)
 
      for i in self.inventar_liste:
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
elif args.X: server.write_xml_file()
else:      server.showdata()
