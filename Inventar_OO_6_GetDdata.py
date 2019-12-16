#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_OO_6_GetDdata.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Holt Daten von einem anderen Server ab
#
##############################################

import socket,json,InventarBasisModul as ibm

###Variablen
host='localhost'
port=10000

###TCP/IP Socket erstellen
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###Auf remote Port verbinden
server_address = (host, port)
print ("Erstelle Verbindung mit", server_address)
sock.connect(server_address)

###Daten senden/empfangen
message='getdata'
sock.sendall(bytes(message, 'utf-8'))
data = sock.recv(512)

###Daten in Datenbank einlesen
jsonData=data.decode("utf-8")
pdict = json.loads(jsonData)
print (pdict)
