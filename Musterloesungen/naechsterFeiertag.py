#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Die Website date.nager.at bietet ein einfaches REST-API um die Feiertage eines Lands und Jahres zu erhalten.
Wann ist der nächste Feiertag bei uns? 
"""
import urllib.request
import json
import datetime


land='CH'
heute=datetime.date.today()
jahr=heute.year
url = f'https://date.nager.at/api/v3/PublicHolidays/{jahr}/{land}'

with urllib.request.urlopen(url) as u:
    body = u.read().decode('utf-8')

resp = json.loads(body)
for holiday in resp:
    if holiday['date'] > str(heute):
        print('Nächster Feiertag ist', holiday['localName'], 'am', holiday['date'])
        # Falls der Feiertag nur kantonal ist, ist im Schlüssel "counties" eine Liste
        # der Kantone enthalten, im Format 'CH-XY', wobei XY für das Kantonskürzel steht
        kantone = holiday['counties']
        if kantone:
            print('Nur in den Kantonen', ', '.join(sorted(map(lambda k: k[3:], kantone))))
        break;

