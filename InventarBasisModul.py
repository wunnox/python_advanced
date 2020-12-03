#!/usr/local/bin/python3
##############################################
#
# Name: InventarBasisModul.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Basis Modul mit allen Funktionen
#
##############################################

import platform,os,time,argparse,json,xml.dom.minidom

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
