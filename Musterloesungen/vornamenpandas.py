#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 25 19:31:33 2022

@author: rene
"""

import pandas as pd
import matplotlib.pyplot as plt

quelle='https://data.stadt-zuerich.ch/dataset/bev_vornamen_baby_od3700/download/BEV370OD3700.csv'
limite = 15
auswahljahr = None # 1996 #2022

namen = pd.read_csv(quelle, encoding='utf-8-sig')

# filter if auswahljar is set
if auswahljahr:
    namen = namen[(namen['StichtagDatJahr']==auswahljahr)]

von, bis = namen['StichtagDatJahr'].min(), namen['StichtagDatJahr'].max()

n_grp=namen.groupby('Vorname')[['AnzGebuWir']].sum().nlargest(limite, 'AnzGebuWir').T

# Dataframes werden idR nicht via print ausgegeben, sondern als Plot oder neue Datei
ax = n_grp.T.plot.barh(
    title=f"Vornamen Stadt Zürich ({von}-{bis})",
    xlabel="Anzahl Geburten", ylabel="",
    legend=None)
ax.invert_yaxis()
ax.bar_label(ax.containers[0])
plt.show()

