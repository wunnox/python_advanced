#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: Inventar_10_ssh.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 01.10.2016 1.0
#
# Purpose: Uebertragen von json Daten via ssh Kommando auf einem Remote-Server
#
##############################################

import subprocess,argparse

###Argparse Eingabe prüfen
if __name__=='__main__':
   parser = argparse.ArgumentParser(description='Führt Kommandos auf einem Remote Servers aus')
   parser.add_argument('-k', metavar='Kommando', nargs=1, help="Auszuführendes Kommando", required=True)
   parser.add_argument('-s', metavar='Server', nargs=1, help="Hostname Remote Server", required=True)
   parser.add_argument('-u', metavar='User', nargs=1, help="Login User", required=True)
   args = parser.parse_args()

   ###Variabeln
   kommando=args.k[0]
   server=args.s[0]
   user=args.u[0]

###Funktionen
def remote_daten_laden(user,server,kommando):
   #SH-Verbindung
   serverstring=user+"@"+server
   ssh = subprocess.Popen(["ssh", serverstring, kommando],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

   ###Auswerten des Resultates
   result = ssh.stdout.readlines()
   for r in result: return r[:-1].decode('utf8')

   error = ssh.stderr.readlines()
   if error:
       print ('\033[0;31m')
       for e in error: return "ERROR:", e[:-1].decode('utf8')
       print('\033[0;30m')

if __name__=='__main__':
   ###Daten ausgeben
   inventar=remote_daten_laden(user,server,kommando)
   print (inventar)
