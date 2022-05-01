#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:07:27 2022

@author: rene.degen@inodes.ch
"""

from concurrent import futures
import urllib.parse, urllib.request
from time import time

response=[]
wiki = 'https://de.wikipedia.org/wiki/'
laender = ['Schweiz', 'Deutschland', 'Frankreich', 'Italien', 'Österreich']
urls = [wiki + urllib.parse.quote(l) for l in laender]

def get_url(url):                                          ### Funktion
    try: 
        l = len(urllib.request.urlopen(url).read())
        response.append(f"{url:45}{l:>10d}")
    except: response.append(f"{url:45}Fehler")

time0 = time()
with futures.ThreadPoolExecutor() as e:
    res = e.map(get_url, urls)

for r in response:print (r)                               ### Resultat auslesen 
 
print("{:8f} Sekunden".format(time() - time0)) 
