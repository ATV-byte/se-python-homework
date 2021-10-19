"""
    Ex. 4: Mai jos aveti 2 functii:
        - add_prefix --> adauga un prefix primit ca parametru unui string
        primit tot ca parametru
        - generate_random_str --> genereaza un string aleator de dimensiune X,
        X fiind un parametru

        Va trebui sa scrieti o functie care sa adauge un sufix (add_suffix),
        dar acel sufix nu trebuie sa contina nicio litera din prefix.

        Sufixul si prefixul le veti primi ca si input de la tastatura, la fel si
        X, care este lungimea stringului aleator.
        In cazul in care sufixul are vreo litera pe care o are si prefixul,
        veti cere un sufix nou, pana cand este dat unul corect, sau pana cand
        a fost incercat de 3 ori. A 4-a oara veti printa stringul fara sufix.

    Rezultatul ar trebui sa arate asa:
        - pentru prefix = 'bla', sufix = 'cmi', x = 3 si un string aleator 'lol'
            ---> 'blalolcmi'
        - pentru prefix = 'bla', sufix = (pe rand, 'ba', 'la', 'bla') x = 3
        si un string aleator 'lol'
            ---> 'blalol'

    Orice e neclar, ma intrebati pe discord la orice ora, fara probleme.
"""
import random


def add_prefix(pfx, rand_str):
    return pfx + rand_str


def add_prefix_sufix(pfx, rand_str, sfx):
    return pfx + rand_str + sfx


def check(s1, s2):
    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(0, len(s1)):
        for j in range(0, len(s2)):
            if s1[i] == s2[j]:
                return False
    return True


# Nu am spus ca stringul generat aleator trebuie sa contina toate literele
def generate_random_str(str_length):
    rand_str = ''
    while str_length:
        str_length -= 1
        rand_str += random.choice(['a', 'x', 'c', 'm', 'i'])
    print(f"The generated string is {rand_str}")
    return rand_str


prefix = input('Give me an prefix\n')
count = 0
sufix = input('Give me an sufix\n')
c = check(prefix, sufix)

while c == False and count < 2:
    sufix = input('Give me another sufix\n')
    c = check(prefix, sufix)
    count = count + 1

if count < 2:
    x = int(input('Give me a number to generate the random string\n'))
    print(add_prefix_sufix(prefix, generate_random_str(x), sufix))
else:
    x = int(input('Give me a number to generate the random string\n'))
    print(add_prefix(prefix, generate_random_str(x)))
