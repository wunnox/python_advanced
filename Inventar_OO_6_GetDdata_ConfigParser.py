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

import socket,json,configparser,InventarBasisModul as ibm

####Konfigdaten einlesen
config = configparser.ConfigParser()
config.read('Inventar.cfg')

####Variablen
port=int(config['DEFAULT']['port'])
host=config['LISTENER']['host']

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
