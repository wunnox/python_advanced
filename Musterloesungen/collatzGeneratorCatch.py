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
        return 0
    i = int(n)  # better safe than sorry
    steps = 1
    yield i
    while (i != 1):
        steps += 1
        if i % 2 == 0:
            i//=2
        else:
            i=3*i+1
        yield i
    return steps

zahl = int(input('Gib eine Zahl ein: -> '))
i = collatz_generator(zahl)
while True:
    try:
        print(next(i), end=" ")
    except StopIteration as e:
        print('\n{} Steps'.format(e.value))
        break


