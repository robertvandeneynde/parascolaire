#!coding: utf-8

L = [1,2,7,2]
c = 7

# Que valent les valeurs de i au cours du temps ?
# Qu'affiche ce code ?
# Essayez aussi avec c = 5

i = 0
while i < len(L) and L[i] != c:
    i = i + 1

if i == len(L):
    i = -1

print i