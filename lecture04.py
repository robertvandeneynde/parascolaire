#!coding: utf-8

h = 10
m = 50
s = 59

# Que valent les valeurs de h,m,s au cours du temps ?
# Pensez à tous les cas possible de h,m,s
# Avez-vous deviné ce que fait ce code ?

s = s + 1

if s == 60:
    s = 0
    m = m + 1

if m == 60:
    m = 0
    h = h + 1

if h == 24:
    h = 0
