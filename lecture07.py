#!coding: utf-8

a = 5
b = 10
c = 1

# Que valent les valeurs de L,a,b,c au cours du temps ?
# imaginez toutes les valeurs possibles de a,b,c
# Essayez avec a,b,c valant 10,5,-1 ou 10,5,1 ou 5,10,0
# Avez vous devinez ce que fais ce code ?

L = []

if a < b and c > 0:
    while a < b:
        L.append(a)
        a = a + c

elif a > b and c < 0:
    while a > b:
        L.append(a)
        a = a + c


