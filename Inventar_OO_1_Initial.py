#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_1_Initial.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Basis Script
#
##############################################

import platform,os,time

####Klassen
class Server:
  #Klassenvariable
  timestamp=time.time()

  #Konstruktor Methode
  def __init__(self,name):
      #Attribute
      self.name=name
      self.nrcpu=os.cpu_count()
      self.system=platform.system()
      self.release=platform.release()
      self.machine=platform.machine()

  #Weitere Methode
  def showdata(self):
      print ("\nServer Angaben\n##############")
      print ("Name:", self.name)
      print ("Nr.CPU:", self.nrcpu)
      print ("System:", self.system)
      print ("Release:", self.release)
      print ("Machine:", self.machine)
      print ("Timestamp:", int(self.timestamp))

  #Destruktor Methode
  def __del__(self):
      print ("\nLösche", self.name, "wieder")

####Objekt erfassen
server=Server(platform.node())

####Daten ausgeben
server.showdata()

