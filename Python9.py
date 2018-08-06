import sys

wort = input("Bitte das zu prüfende Wort hier eingeben: ")

laenge = len(wort)

IstPalindrom = True

#anna
#hans
#lagerregal

i = 0

while i < laenge/2:
    if wort[i] != wort[laenge-i-1]:
        IstPalindrom = False
    i = i + 1

print(IstPalindrom)
