
import re

# IBAN Prüfzifferberechnung nach http://www.pruefziffernberechnung.de/Originaldokumente/IBAN/Prufziffer_07.00.pdf

def validierung_iban_hilfsmethode(numiban):
    # 1. Teilschritt
    irest=numiban
    while irest:
        i=numiban[:9]
        rs=str(int(i)%97)
        irest=numiban[9:]
        numiban=rs+irest
    return int(rs)==1

def validierung_iban(iban):
    # Schritt 1: IBAN und nicht-alpha-Zeichen entfernen
    iban = re.sub('^IBAN', '', iban)
    iban = re.sub('[^\w]', '', iban)
    save = iban
    # Schritt 2: Erste vier Zeichen an Ende Schieben
    iban = iban[4:] + iban[:4]
    # Schritt 3: Alphazeichen umwandeln
    iban2=''
    for c in list(iban):
      iban2 += str(int(c, base=36))
    iban = iban2
    # Schritt 4: Durch 97 teilen
    # Da die Nummer u.U. zu gross ist, wird das iterative Verfahren verwendet
    r=validierung_iban_hilfsmethode(iban)

    return(save, r)

print(validierung_iban('IBAN CH10 0023 00A1 0235 0260 1'))

print(validierung_iban('IBAN CH93 0076 2011 6238 5295 7'))

print(validierung_iban('IBAN CH30 0070 0111 5001 8305 9'))

print(validierung_iban('IBAN DE68 2105 0170 0012 3456 78'))

print(validierung_iban('IBAN LI5708801200185100814'))

print(validierung_iban('IBAN SC52BAHL01031234567890123456USD'))

print(validierung_iban('IBAN QA54QNBA000000000000693123456'))




