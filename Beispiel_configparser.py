#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_configparser.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.11.2017
#
# Purpose: Beispiele mit configparser
#
##############################################

import configparser

###Config-File einlesen
config = configparser.ConfigParser()
config.read('Beispiel.cfg')

###Config-Daten zuordnen
nummer=int(config['DEFAULT']['nummer'])
name=config['PERSONEN']['name']
art=config['ARTIKEL']

print ("Name:", name)
print ("Nummer:", nummer)
print ("Artikel:", art['art1'])


