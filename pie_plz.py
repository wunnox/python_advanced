import urllib.request
import json
import numpy as np
import matplotlib.pyplot as plt

# sendet Daten
u = urllib.request.urlopen("https://swisspost.opendatasoft.com/api/v2/catalog/datasets/bevoelkerung_proplz/exports/json")

lines = u.readlines()
u.close()

jsonline = lines[0].decode('utf-8')
resp = json.loads(jsonline)

labels=[]
data=[]
explode=[]
explode_plz = '6003'

i=-1
for entry in resp:
    if entry['ortbez18'] == 'Luzern':
        plz = entry['plz']
        anzahl = int(entry['anzahl'])
        # print(entry)
        if plz in labels:
            data[i]=+anzahl
        else:
            i+=1
            labels.append(plz)
            data.append(anzahl)
            if plz == explode_plz:
                explode.append(0.1)
            else:
                explode.append(0)

plt.pie(data, labels=labels, explode=explode, autopct='%1.1f%%', startangle=90)
plt.axis('equal')
plt.show()




