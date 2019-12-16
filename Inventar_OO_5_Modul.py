#!/usr/local/bin/python3
##############################################
#
# Name: Inventar_OO_5_Modul.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.06.2017
#
# Purpose: Server Inventar Script
#          Braucht Modul InventarBasisModul.py
#
##############################################

import platform,os,argparse, InventarBasisModul as ibm

####Parameter auswerten
parser = argparse.ArgumentParser(description='Liest die Inventardaten des aktuellen Servers aus')
parser.add_argument('-c', action='store_true', help="Daten in CSV-Format ausgeben")
parser.add_argument('-j', action='store_true', help="Daten in Json-Format ausgeben")
parser.add_argument('-J', action='store_true', help="Daten in Json-Datei schreiben")
parser.add_argument('-X', action='store_true', help="Daten in XML-Datei schreiben")
args = parser.parse_args()

####Objekt erfassen
server=ibm.Server(platform.node())

####Basis Daten erfassen
server.nrcpu=os.cpu_count()
server.system=platform.system()
server.release=platform.release()
server.machine=platform.machine()

####Daten ausgeben
if args.c: print (server.showcsv())
elif args.j: print (server.show_json())
elif args.J: server.write_json_file()
elif args.X: server.write_xml_file()
else:      server.showdata()
