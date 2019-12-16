#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
##############################################
#
# Name: Beispiel_subprocess.py
#
# Author: Peter Christen
#
# Version: 1.0
#
# Date: 01.10.2016 1.0
#
# Purpose: Ausführen eines Kommandos mit subprocess
#
##############################################

import subprocess

kommando = ['ls', '-l', 'Beispiel_subprocess.py', 'Beispiel.sonstwas.py']
ssh = subprocess.Popen(kommando,
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

#Ausgabe standard output
result = ssh.stdout.readlines()
for r in result:
    print(r[:-1].decode('utf8'))

#Ausgabe standard error output
error = ssh.stderr.readlines()
if error:
    print('\033[0;31m')   #rot
    for e in error:
        print(e[:-1].decode('utf8'))
    print('\033[0;30m')   #schwarz
