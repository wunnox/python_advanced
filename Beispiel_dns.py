#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: Beispiel_dns.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Abfragen eines DNS
#
##############################################

import socket

###Variabeln
ipadressen=['172.16.18.15','172.16.18.14','172.16.18.12']

###Funktion DNS Abfrage
def node(adr):
   try:
      ns=socket.gethostbyaddr(adr)
      name=ns[0]
      ip=ns[2][0]
   except:
      name="Adresse nicht gefunden"
      ip=''
   return name,ip

###Abfrage starten
for adresse in ipadressen:
   nodename,ip=node(adresse)
   print (adresse+": "+nodename+": "+ip)
