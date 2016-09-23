#!coding: utf-8

h1 = 10
m1 = 20
s1 = 5

h2 = 10
m2 = 45
s2 = 20

# Que valent les valeurs de h,m,s au cours du temps ?
# Pensez à tous les cas possible des variables d'entrées
# Avez-vous deviné ce que fait ce code ?

s = s1 + s2
m = m1 + m2
h = h1 + h2

if s >= 60:
    m = m + s // 60 # // = division entière
    s = s - 60

if m >= 60:
    h = h + m // 60
    m = m - 60

if h >= 24:
    h = h - 24
