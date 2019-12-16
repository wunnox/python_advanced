#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_2_Transmit.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Zusätzlich mit einer CSV-Funktion
#
##############################################

import platform,os,time,argparse

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
args = parser.parse_args()

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

####Objekt erfassen
server=Server(platform.node())

####Basis Daten erfassen
server.nrcpu=os.cpu_count()
server.system=platform.system()
server.release=platform.release()
server.machine=platform.machine()

####Daten ausgeben
if args.c: print(server.showcsv())
else:      server.showdata()
