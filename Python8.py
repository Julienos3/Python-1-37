import sys

Eingabe = int(input("Bitte Zahl eingeben: "))

fakultaet = 1

while Eingabe > 0:
    fakultaet = fakultaet * Eingabe
    Eingabe = Eingabe - 1

print(fakultaet)
