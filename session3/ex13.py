"""
    Ex. 13: Scrieti un decorator care sa modifice modul de functionare
    al functiei f. Puteti alege voi cum. Momentan, f intoarce 'cmi', un exemplu
    ar fi sa intoarca 'CmI' dupa aplicarea decoratorului.

"""


def dec(func):
    def wrapper():
        var = func()
        var2 = ''
        for i in range(0, len(var)):
            if i % 2 == 0:
                var2 = var2 + var[i].upper()
            else:
                var2 = var2 + var[i]
        return var2
    return wrapper

# decoarate me


@dec
def f():
    return 'cmi'


print(f())
