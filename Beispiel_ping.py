#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_ping.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Sendet pings an definierte IP-Adressen
#
##############################################

from os import system

###Variabeln
hosts=["192.168.1.80","192.168.1.50","192.168.1.95"]

###Ping starten
for host in hosts:
   response = system("ping -c 1 -t 2 " + host + ">/dev/null 2>&1")
   if response == 0:
      print ("Host", host, "is alive")
   else:
      print ("Host", host, "is not reachable")

