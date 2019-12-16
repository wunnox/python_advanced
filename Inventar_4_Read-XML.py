#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_4_Read-XML.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.07.2017
#
# Purpose: Einlesen eines XML-Files
#
##############################################

import xml.dom.minidom

####Datei einlesen
doc = xml.dom.minidom.parse("inventar_multi.xml")

####XML-Daten analysieren
servers = doc.getElementsByTagName("server")
for server in servers:
        name = server.getAttribute("name")
        nrcpu = server.getElementsByTagName("nrcpu")[0]
        release = server.getElementsByTagName("release")[0]
        system = server.getElementsByTagName("system")[0]
        machine = server.getElementsByTagName("machine")[0]
        timestamp = server.getElementsByTagName("timestamp")[0]
        print (name)
        print (nrcpu.firstChild.data)
        print (release.firstChild.data)
        print (system.firstChild.data)
        print (machine.firstChild.data)
        print (timestamp.firstChild.data)
