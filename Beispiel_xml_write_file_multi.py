#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_xml_write_file_multi.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.07.2017
#
# Purpose: Erstellen eines XML-Files mit mehreren Records
#
##############################################

import xml.dom.minidom

###Erste Stuffe erstellen
doc = xml.dom.minidom.Document()
doc.appendChild(doc.createComment("Inventardaten von Server Andromeda"))
erste_stuffe = doc.createElement("inventar")
doc.appendChild(erste_stuffe)
 
###Zweite Stuffe erstellen
zweite_stuffe = doc.createElement("server")
zweite_stuffe.setAttribute( "name", 'raspberryshake' )
erste_stuffe.appendChild(zweite_stuffe)

###Datenelemente erstellen
data = {'nrcpu':'4','system':'Linux','release':'4.4.26-v7+','machine':'armv7l','timestamp':'1497797877'}
for name,value in data.items():
   # Element erstellen
   element_name = doc.createElement(name)
   zweite_stuffe.appendChild(element_name)
 
   # Element Wert hinzufügen
   element_wert = doc.createTextNode(value)
   element_name.appendChild(element_wert)

###Zweite Stuffe erstellen
zweite_stuffe = doc.createElement("server")
zweite_stuffe.setAttribute( "name", 'UM00365' )
erste_stuffe.appendChild(zweite_stuffe)

###Datenelemente erstellen
data = {'nrcpu':'4','release':'16.5.0','system':'Darwin','machine':'x86_64','timestamp':'1499540600'}
for name,value in data.items():
   # Element erstellen
   element_name = doc.createElement(name)
   zweite_stuffe.appendChild(element_name)
 
   # Element Wert hinzufügen
   element_wert = doc.createTextNode(value)
   element_name.appendChild(element_wert)
 
###Daten in File schreiben
doc.writexml( open('inventar.xml', 'w'),
   indent="  ",
   addindent="  ",
   newl='\n')
doc.unlink()
