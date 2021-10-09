"""
    Veti primi un string de la tastatura.
    Va trebui sa printati numarul de vocale si numarul de consoane din
    acel string.

    exemplu:
        Veti primi: 'center'
        Veti printa:
        2 (pentru vocale)
        4 (pentru consoane)
"""
x = input()
x = x.lower()
vocals = 0
consonant = 0
for el in x:
    if el == 'a' or el == 'e' or el == 'i' or el == 'o' or el == 'u':
        vocals = vocals + 1
    else:
        consonant = consonant + 1

print(vocals)
print(consonant)