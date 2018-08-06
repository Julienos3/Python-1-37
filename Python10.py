import sys

def summiere (summand1, summand2):
    summe = summand1 + summand2
    return summe

def istPalindrom(wort):
    laenge = len(wort)
    istPalindrom = True

    i = 0

    while i < laenge//2:
        if wort[i] != wort[laenge-i-1]:
            istPalindrom = False
        i = i + 1

    return istPalindrom




while 1==1:
    eingabe = input("Bitte das zu pruefende Wort eingeben: ")
    if(istPalindrom(eingabe)):
        print("das wort "+eingabe+" ist ein palindrom")
    else:
        print("das wort "+eingabe+" ist kein palindrom") 

   


#ergebnis = summiere(4,8)
#print(ergebnis)

