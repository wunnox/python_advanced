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

bev={}

i=-1
for entry in resp:
    ort=entry['ortbez18']
    anzahl = int(entry['anzahl'])
    if anzahl > 10000:
        continue
    if ort in bev:
        bev[ort]+=anzahl
    else:
        bev[ort]=anzahl

print(bev['Basel'])

a=np.array(list(bev.values()))
bins=list(range(0, 10000, 1000))

plt.hist(a, bins)
plt.show()




