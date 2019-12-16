#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_OO_3_privat.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Beispielscript mit privaten Variabeln
#
##############################################

import platform,os,time

####Variablen
server=''

####Classes
class Server:
  #Class variable
  timestamp=time.time()
  anschaffungskosten=10000
  _abschreibung=5
  __supportbasis=.1

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
      print ("Release:", self.release)
      print ("System:", self.system)
      print ("Machine:", self.machine)
      print ("Timestamp:", int(self.timestamp))

  def add(self,anz):
      self.nrcpu+=anz

  def kosten(self):
      abschreibung=self.anschaffungskosten/self._abschreibung
      support=self.anschaffungskosten*self.__supportbasis
      print ("\nServerkosten\n##############")
      print ("Abschreibung:  Fr. %6.2f/Jahr" % abschreibung)
      print ("Supportkosten: Fr. %6.2f/Jahr" % support)

####Objekt erfassen
server=Server(platform.node())

####Basis Daten erfassen
server.nrcpu=os.cpu_count()
server.system=platform.system()
server.release=platform.release()
server.machine=platform.machine()

####Daten ausgeben
server.showdata()
server.kosten()
server.add(4)
server.showdata()
server.kosten()

print ("\nKlassenvariable timestamp:",int(Server.timestamp))
print ("Variable anschaffungskosten:",Server.anschaffungskosten)
print ("Variable _abschreibung:",Server._abschreibung)
#print ("Variable __supportbasis:",Server.__supportbasis) # Kann nicht angezeigt werden
