#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Collatz-Problem:
Zahlenfolge, die nach einem einfachen Bildungsgesetz konstruiert werden:
- Beginne mit einer natürlichen Zahl (n>0)
- Ist n gerade, fahre mit n/2 weiter
- Ist n ungerade, nimm als nächstes 3n + 1
- Den Vorgang wiederholen mit der erhaltenen Zahl
Collatz-Vermutung: jede so konstruierte Zahlenfolge mündet in den Zyklus 4, 2, 1 unabhängig von der Startzahl n>0
Geben Sie die Zahlenfolge und die Anzahl Schritte aus

"""

def collatz_generator(n):
    if n < 1:
        return
    i = int(n)  # better safe than sorry
    yield i
    while (i != 1):
        if i % 2 == 0:
            i//=2
        else:
            i=3*i+1
        yield i


steps = 0
zahl = int(input('Gib eine Zahl ein: -> '))
for i in collatz_generator(zahl):
    print(i, end=" ")
    steps += 1
print('\n{} Steps'.format(steps))


