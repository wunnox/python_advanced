#!/usr/local/bin/python3
##############################################
#
# Name: Beispiel_argparse.py
#
# Author: Peter Christen
#
# Version: 1.0
# 
# Date: 10.11.2017
#
# Purpose: Beispiele mit argparse
#
##############################################

import argparse

###Parameter definieren
parser = argparse.ArgumentParser(description="Zweck des Scripts")
parser.add_argument('-v','--verbose', action='store_true', help="Beschreibung")
parser.add_argument('-f', choices=['blau', 'rot'], help="Auswahl")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument('-k', metavar='Keyword', nargs=1, help="Braucht genau eine Angabe") 
group.add_argument('-n', metavar='Nummern', nargs='+', help="Mehrere Nummern", type=int) 
args = parser.parse_args()

###Parameter auswerten
if args.verbose: print("v")
if args.f: print ("f",args.f)
if args.k: print ("k",args.k)
if args.n: print ("n",args.n)
