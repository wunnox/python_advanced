#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_OO_5_Properties.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: OO Beispiel mit Properties
#
##############################################

import platform,os,time

####Variablen
server=''

####Classes
class Server:

  #Konstruktor Methode
  def __init__(self,name):
      #Attribute
      self.name=name
      self.nrcpu=0
      self.system=''
      self.release=''
      self.machine=''

  #Weitere Methode
  def showdata(self):
      print ("\nServer Angaben\n##############")
      print ("Name:", self.name)
      print ("Nr.CPU:", self.nrcpu)
      print ("System:", self.system)
      print ("Release:", self.release)
      print ("Machine:", self.machine)
      print ("Timestamp:", int(self.timestamp))

  def getTimestamp(self):
      __timestamp=time.time()
      return __timestamp

  #Destruktor Methode
  def __del__(self):
      print ("\nLösche", self.name, "wieder")

  timestamp=property(getTimestamp)

####Objekt erfassen
server=Server(platform.node())

####Basis Daten erfassen
server.nrcpu=os.cpu_count()
server.system=platform.system()
server.release=platform.release()
server.machine=platform.machine()

####Daten ausgeben
server.showdata()
print (server.timestamp)
server.timestamp=1000000
print (server.timestamp)
server.showdata()
