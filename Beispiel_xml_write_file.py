#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_xml_write_file.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.07.2017
#
# Purpose: Schreiben eines XML-Files
#
##############################################

import xml.dom.minidom

###Erste Stufe erstellen
doc = xml.dom.minidom.Document()
doc.appendChild(doc.createComment("Inventardaten von Server Andromeda"))
erste_stuffe = doc.createElement("inventar")
doc.appendChild(erste_stuffe)
 
###Zweite Stufe erstellen
zweite_stuffe = doc.createElement("server")
zweite_stuffe.setAttribute( "name", 'Andromeda' )
erste_stuffe.appendChild(zweite_stuffe)

###Datenelemente erstellen
data = {'nrcpu':'8','release':'16.6.0','system':'Darwin','machine':'x86_64','timestamp':'1499540757'}
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
