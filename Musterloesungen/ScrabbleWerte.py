#!/usr/bin/env python3
###################################################################
#
# Uebung:
# Erstellen Sie eine Klasse ScrabbleString. Dabei sollen die
# Vergleichsoperatoren zwischen Instanzen von ScrabbleString deren
# Punktezahl im Scrabble-Spiel vergleichen. Zeigen Sie, dass 
# «Heiligabend» und «Ostermontag» gleich viel wert sind.
#
# Die Werte der einzelnen Buchstaben sind dem Eintrag
# https://de.wikipedia.org/wiki/Scrabble
# entnommen
#
###################################################################

#### Lösung: ####

class ScrabbleString(str):
    werte = {}
    for k,v in {
            'ENSIRTUAD':1,
            'HGLO':2,
            'MBWZ':3,
            'CFKP':4,
            'ÄJÜV': 6,
            'ÖX': 1,
            'QY': 10}.items():
        werte.update(dict.fromkeys(list(k),v))
        # werte |= dict.fromkeys(list(k),v)	# Ab Python 3.9
        
    def wert(self):
        v = 0
        for char in (str(self)).upper():
            if char in self.werte:
                v += self.werte[char]
        return v

    def __lt__(self,other):
        return self.wert() < (ScrabbleString(other)).wert()
    
    def __gt__(self,other):
        return self.wert() > (ScrabbleString(other)).wert()
    
    def __eq__(self,other):
        return self.wert() == (ScrabbleString(other)).wert()
    
    def __ne__(self,other):
        return self.wert() != (ScrabbleString(other)).wert()
        
    def __ge__(self,other):
        return self.wert() >= (ScrabbleString(other)).wert()
    
    def __le__(self,other):
        return self.wert() <= (ScrabbleString(other)).wert()
    

str1=ScrabbleString('Dampfschiff')
str2=ScrabbleString('Kapitänsmütze')

if (str1>str2):
    print(str1, 'ist grösser als', str2, '(', str1.wert(), 'zu', str2.wert(), ')')
    
for zeichenkette in ['Heiligabend', 'Ostermontag']:
    print (zeichenkette, (ScrabbleString(zeichenkette)).wert())
    
print(ScrabbleString('Lokationsstammdatenverzeichnis').wert())
    



