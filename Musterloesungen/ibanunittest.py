#!/usr/bin/env python3
"""
Die Prüfzifferberechnung der IBAN kann noch etwas optimiert werden:
Der Schritt 3 (Umwandlung der Alphazeichen in eine rein numerische Darstellung) kann kürzer gemacht werden.
Tip: map-Funktion, eine kleine anonyme Funktion, die Zeichenkette muss zerteilt und zusammengesetzt werden
Damit wir die bestehende Berechnung nicht verfälschen, binden wir das in einen unittest ein.
Für einen Negativ-Test bauen wir auch eine Exception ein (z.B. bei Kleinbuchstaben oder nicht unterstützten Zeichen)

"""

import unittest
import ibantools2 as ibantools


class MeinTest(unittest.TestCase):   
    
    def testBerechnung(self):
        self.assertEqual(ibantools.validiere("CH82 0900 0000 1001 5000 6"), True)
        self.assertEqual(ibantools.validiere("CH76 0070 0114 8050 8339 3"), True)
        self.assertEqual(ibantools.validiere("CH76 0070 0114 8050 8339 0"), False)
        
        self.assertEqual(ibantools.validiere("IBAN CH10 0023 00A1 0235 0260 1"), True)
        self.assertEqual(ibantools.validiere("IBAN CH93 0076 2011 6238 5295 7"), True)
        self.assertEqual(ibantools.validiere("IBAN DE68 2105 0170 0012 3456 78"), True)
        self.assertEqual(ibantools.validiere("IBAN LI5708801200185100814"), True)
        self.assertEqual(ibantools.validiere("IBAN SC52BAHL01031234567890123456USD"), True)
        self.assertEqual(ibantools.validiere("IBAN QA54QNBA000000000000693123456"), True)
        
        # Erzeugt die generiere-Funktion eine korrekte IBAN?
        self.assertEqual(ibantools.generiere(), "CH680000100A123456789")
        self.assertEqual(ibantools.generiere(bc=99999, kontonummer=123456789), 'CH8399999000123456789')
        self.assertEqual(ibantools.validiere(ibantools.generiere()), True)
        
        # Hier können noch viele Tests folgen, Zeichen der generierten IBAN-Nummer, Länge, ...
        
    # Negativ-Test
    def testAusnahmen(self):
        self.assertRaises(ValueError, ibantools.validiere, "xyz")
        self.assertRaises(ValueError, ibantools.validiere, "CH76_0070 0114 8050 8339 3")
        self.assertRaises(ValueError, ibantools.validiere, "ch760070 0114 8050 8339 3")
        
if __name__ == "__main__":
    unittest.main()
