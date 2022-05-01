
import re

# IBAN Prüfzifferberechnung nach http://www.pruefziffernberechnung.de/Originaldokumente/IBAN/Prufziffer_07.00.pdf

def __hilfsmethode__(numiban):
    # 1. Teilschritt
    irest=numiban
    while irest:
        i=numiban[:9]
        rs=str(int(i)%97)
        irest=numiban[9:]
        numiban=rs+irest
    return int(rs)
    
def validiere(iban):
    
    # Schritt 1: IBAN und nicht-alpha-Zeichen entfernen
    iban = re.sub('^IBAN', '', iban)
    iban = re.sub('[^\w]', '', iban)
    # Schritt 2: Erste vier Zeichen an Ende Schieben
    iban = iban[4:] + iban[:4]
    # Schritt 3: Alphazeichen umwandeln
    iban2=''
    for char in iban:
        if char >= 'A':
            iban2 += str(ord(char) - ord('A') + 10)   
        else:
            iban2 += char
    iban = iban2
    # Schritt 4: Durch 97 teilen
    # Da die Nummer u.U. zu gross ist, wird das iterative Verfahren verwendet
    r=__hilfsmethode__(iban)
    return(r == 1)


def generiere(land = 'CH', bc = 1, kontonummer = 'A123456789'):
    # Schritt 1
    *iban_chars, = land + '00' + "{:0>5}".format(bc) + "{:0>12}".format(kontonummer)
    # Schritt 2
    iban_chars = iban_chars[4:] + iban_chars[:4]
    # Schritt 3
    i = 0
    while i < len(iban_chars):
        if iban_chars[i] >= 'A':
            iban_chars[i] = str(ord(iban_chars[i]) - ord('A') + 10) 
        i+=1
    # Scritt 4
    r = __hilfsmethode__(str(''.join(iban_chars)))
    r = 98 - r
    iban_chars[-2]=str(r//10)
    iban_chars[-1]=str(r%10)
    # Schritt 5
    iban_chars = iban_chars[-4:] + iban_chars[:-4]
    # Schritt 6
    i=0
    while i < len(iban_chars):
        if int(iban_chars[i]) > 9:
            iban_chars[i] = chr(int(iban_chars[i]) + ord('A') - 10) 
        i+=1
    iban = "".join(iban_chars)
    return iban
    

if __name__ == "__main__":
    print("Dies ist ein Modul und sollte eingebunden werden")


