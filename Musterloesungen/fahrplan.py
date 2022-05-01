#!/usr/bin/env python3
"""
Die Website search.ch bietet Fahrplanabfragen per API (mit JSON). Wann fährt der nächste öV-Anschluss an Ihren Wohnort?
"""

import urllib.request
import json
import pprint

# Eingabedaten
von = input("Bitte den Startort eingeben: ")

von = urllib.parse.quote(von)
# sendet Daten
u = urllib.request.urlopen("https://fahrplan.search.ch/api/stationboard.json?stop="\
                          + von + '&limit=5' + '&show_delays=1')

#u = urllib.request.urlopen("https://transport.opendata.ch/v1/stationboard?id=" + von + "&limit=10")

# Empfang der Antwort und Ausgabe
lines = u.readlines()
u.close()

jsonline = lines[0].decode('utf-8')
resp = json.loads(jsonline)

pprint.pprint(resp)

if 'stop' in resp:
    if 'name' in resp['stop']:
        print(resp['stop']['name'])

        if 'connections' in resp:
            for conn in resp['connections']:
                if 'dep_delay' in conn:
                    delay = '('+conn['dep_delay']+')'
                else:
                    delay = ''
                print(conn['time']+delay+':', conn['line'], conn['terminal']['name'])
elif 'messages' in resp:
    print(resp['messages'][0])
else:
    print('Unbekannter Fehler')
