liste = [-9,-10,-23,-40]

bishergroesstezahl = 0

for zahl in liste:
    if zahl > bishergroesstezahl:
        bishergroesstezahl = zahl
    elif zahl < bishergroesstezahl:
        bishergroesstezahl = zahl

print(bishergroesstezahl)
