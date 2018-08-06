from random import randint

liste = []

anzahlelemente = 100

while anzahlelemente > 0:
    hinzu = randint(1, 100)
    liste.append(hinzu)
    anzahlelemente = anzahlelemente - 1

print(liste)

bishergroesstezahl = liste[0]

for zahl in liste:
    if zahl > bishergroesstezahl:
        bishergroesstezahl = zahl

print(bishergroesstezahl)
