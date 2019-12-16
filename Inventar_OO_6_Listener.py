#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_OO_6_Listener.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Mit Listener-Funktion
#
##############################################

import platform,os,time,argparse,socket,InventarBasisModul as ibm

###Variablen
host='localhost'
port=10000

####Objekt erfassen
server=ibm.Server(platform.node())

###TCP/IP Socket erstellen
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

###Socket mit einem Port verbinden
server_address = (host, port)
sock.bind(server_address)

###Auf eingehende Verbindungen warten
sock.listen(1)
print (int(time.time()),": Bereit für Abfragen")

while True:
    connection, client_address = sock.accept()

    while True:
       data = connection.recv(64)
       if data:
          print (int(time.time()),": Eingehende Daten von", client_address, ":", data.decode('utf8'))
          if 'getdata' in data.decode('utf8'):
             data=server.show_json()
             print (data)
             connection.send(bytes(data.encode()))
       else:
          break
connection.close()
