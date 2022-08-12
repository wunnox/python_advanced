#!/usr/bin/python3
##############################################
#
# Name: Beispiel_Logger_OO.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 11.08.2022
#
# Purpose: Logging wahlweise auf stdout oder in ein File
#
##############################################  
import logging,sys

class Logger:
   '''Logger, der Meldung wahlweise in ein File oder auf stdout schreiben kann.'''

   #Konstruktor Methode
   def __init__(self):
      self.logger = logging.getLogger()
      self.logger.setLevel(logging.DEBUG)
      self.frm = logging.Formatter("{asctime} {levelname}: {message}", "%d.%m.%Y %H:%M:%S", style="{")

   def file_logger(self, severity,message):
      '''Schreibt Logging Meldung in ein File'''

      self.handler = logging.FileHandler('Error.log')
      self.handler.setFormatter(self.frm)
      self.logger.addHandler(self.handler)
      meldung="self.logger."+severity+"('"+message+"')"
      eval(meldung)
      self.logger.removeHandler(self.handler)

   def screen_logger(self, severity,message):
      '''Schreibt Logging Meldung auf stdout'''

      self.handler = logging.StreamHandler(sys.stdout)
      self.handler.setFormatter(self.frm)
      self.logger.addHandler(self.handler)
      meldung="self.logger."+severity+"('"+message+"')"
      eval(meldung)
      self.logger.removeHandler(self.handler)

#Logger Objekt erfassen
log=Logger()

if __name__=='__main__':
   log.screen_logger('critical',"Sehr kritische Meldung")
   log.file_logger('critical',"Sehr kritische Meldung")
   log.screen_logger("warning","Und eine Warnung hinterher")
   log.file_logger("debug","Dies ist nur eine Debug Meldung")

