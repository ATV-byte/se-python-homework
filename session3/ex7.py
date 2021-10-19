"""
    Ex. 7: Scrieti o functie care sa primeasca trei parametri
        - prefix (string)
        - word (string)
        - suffix (string)
    Si trebuie sa intoarca cuvantul cu prefixul si sufixul adaugate.

    Raspuns:
        - pentru prefix = 'a', suffix = 'b' si word = 'x'
            ---> 'axb'

    Observatii:
        - functia trebuie sa aiba MAXIM 1 linie de cod ca si body
"""
def add_prefix_sufix(pfx, word, sfx):
    return pfx + word + sfx

print(add_prefix_sufix('a','x','b'))