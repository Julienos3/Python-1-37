import sys

i = int(input("Zahl eingeben (nicht über 4999): "))

while i < 5000:
    print(i)
    i = i + 1

print("dann...")

liste = [7,6,5,4,3,5432,3,6,8,34]

summe = 0

for element in liste:
    print(element)
    summe = summe + element

print(summe)
