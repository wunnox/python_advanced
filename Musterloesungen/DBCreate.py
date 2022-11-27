#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 29 12:50:50 2022

@author: rene.degen@inodes.ch
"""
import sqlite3
# Verbindung und Cursor erzeugen
connection = sqlite3.connect("vornamenZH.db")
cursor = connection.cursor()
# Tabelle erzeugen
cursor.execute("""
               CREATE TABLE vorname(jahr INTEGER,vorname TEXT,
                                    geschlecht TEXT,anzahl INTEGER)
""")
# Transaktion bestätigen und Verbindung schliessen
connection.commit()
connection.close()
