"""
    Veti primi un string de la tastatura.
    Va trebui sa spuneti cate vocale are acest string.

    exemplu:
        Veti primi: 'cmi'
        Veti printa: 1
"""

x = input()
x = x.lower()
vocals = 0
for el in x:
    if el == 'a' or el == 'e' or el == 'i' or el == 'o' or el == 'u':
        vocals = vocals + 1

print(vocals)