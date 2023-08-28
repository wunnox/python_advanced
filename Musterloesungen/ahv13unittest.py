#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 13:35:44 2023

Die Prüfzifferberechnung der AHV Nummer kann noch etwas optimiert werden:
Wechsel des Faktors, Berechnung der Prüfziffer, Vermeidung von Funktionsaufrufen
Damit wir die bestehende Berechnung nicht verfälschen, binden wir das in einen unittest ein.
Für einen Negativ-Test bauen wir auch eine Exception ein (z.B. bei falschem Prefix oder falschem Format)

@author: rene.degen@inodes.ch
"""

import unittest
import ahv13toolsv2 as ahv13
import random

class MeinTest(unittest.TestCase):   
    
    def testBerechnung(self):
        self.assertEqual(ahv13.validiere("756.9217.0769.85"), True)
        self.assertEqual(ahv13.validiere("756.7060.2095.74"), True)
        self.assertEqual(ahv13.validiere("756.3973.9614.05"), False)
                
        # Erzeugt die generiere-Funktion eine korrekte AHV Nummer?
        self.assertEqual(ahv13.generiere(), '7561234567897')
        # Erzeugt der default eine korrekte AHV Nummer?
        self.assertEqual(ahv13.validiere(ahv13.generiere()), True)
        # Eine Zufallszahl generieren lassen und vergleichen
        rnd_nr=random.randint(10**8, 10**9-1)
        self.assertEqual(ahv13.validiere(ahv13.generiere(nummer = rnd_nr), normalisiert = True), True)
        
        # Hier können noch viele Tests folgen, Länge, ...
        
    # Negativ-Test
    def testAusnahmen(self):
        self.assertRaises(ValueError, ahv13.validiere, "xyz")
        self.assertRaises(ValueError, ahv13.validiere, "123.9217.0769.85")
        
if __name__ == "__main__":
    unittest.main()
