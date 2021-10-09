"""
    Veti primi un string de la tastatura, care reprezinta o succesiune de
    paranteze rotunde, drepte si acolade. Va trebui sa spuneti daca parantezele
    sunt inchise corect, sau nu. (boolean - True|False)

    exemplu:
        Veti primi: '(([])){}'
        Veti printa: True

        Veti primi: '(()]'
        Veti printa: False
"""
x = input()
nb_round_open = 0
nb_round_close = 0
nb_square_open = 0
nb_square_close = 0
nb_curly_open = 0
nb_curly_close = 0
for el in x:
    if el == '(':
        nb_round_open = nb_round_open + 1
    if el == ')':
        nb_round_close = nb_round_close + 1
    if el == '[':
        nb_square_open = nb_square_open + 1
    if el == ']':
        nb_square_close = nb_square_close + 1
    if el == '{':
        nb_curly_open = nb_curly_open + 1
    if el == '}':
        nb_curly_close = nb_curly_close + 1

if(nb_round_open == nb_round_close and nb_square_open == nb_square_open and nb_curly_open == nb_curly_close):
    vf = True
else:
    vf = False

print(vf)



