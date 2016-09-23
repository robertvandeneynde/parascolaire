#!coding: utf-8

# Que valent les valeurs de L, p, i au cours du temps ?
# Que se passe-t-il si on remplace "10" par un autre nombre ?

L = []
p = 1
i = 0
while i < 10:
    L.append(p)
    p = p * 2
    i = i + 1

