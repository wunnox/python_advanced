#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_1_Initial.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.11.2017
#
# Purpose: Server Inventar Script
#          Basis Script
#
##############################################

import platform,multiprocessing,os,sys,time

###Variabeln
timestamp=time.time()
inventar={}

###Funktionen
def getdata():
   inventar["name"]=platform.node()
   inventar["nrcpu"]=multiprocessing.cpu_count()
   inventar["system"]=platform.system()
   inventar["release"]=platform.release()
   inventar["machine"]=platform.machine()
   inventar["timestamp"]=int(timestamp)

def showdata():
   print ("Server Angaben\n##############")
   print ("Name:",inventar["name"])
   print ("Nr.CPU:",inventar["nrcpu"])
   print ("System:",inventar["system"])
   print ("Release:",inventar["release"])
   print ("Machine:",inventar["machine"])
   print ("Timestamp:",inventar["timestamp"])

###Daten ausgeben
getdata()
showdata()
sys.exit(0)
