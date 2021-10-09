"""
    Veti primi un numar intreg de la tastatura.
    Va trebui sa printati un strign aleator cu numarul de caractere egal
    cu numarul intreg primit.

    exemplu:
        Veti primi: 5
        Veti printa: 'ashdj' (poate fi orice alt string)
"""
import string
import random
letters = string.ascii_letters
x = int(input())
y = ''
for i in range(x):
    y = y + random.choice(letters)
print(y)