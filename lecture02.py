#!coding: utf-8

a = 1
b = 2

# Qu'affiche ce code ?
# Pensez à tous les cas possible de a,b
# Remarquez que print b est écrit deux fois,
# comment faire un code plus court faisant la même chose ?
# Parfois, plusieurs codes peuvent faire le même résultat.

if a > 0:
    if b > 1:
        print a
    else:
        print b
else:
    if b > 1:
        print a + b
    else:
        print b
        