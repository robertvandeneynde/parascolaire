#!coding: utf-8

x = 1
y = 2
z = 5

# Que fait ce code ? Que vaut "flag" à la fin de l'exécution ?
# Pensez à tous les cas possible de x,y,z
# Avez-vous deviné ce que fait ce code ? (indice: j'en ai parlé dans les exercices du parascolaire)

flag = 0

if x == 4:
    if y == 2:
        if z == 1:
            flag = 1
    else:
        if y == 1:
            if z == 2:
                flag = 1
elif x == 2:
    if y == 4:
        if z == 1:
            flag = 1
        else:
            if y == 1:
                if z == 4:
                    flag = 1
elif x == 1:
    if y == 4:
        if z == 2:
            flag = 1
    else:
        if y == 2:
            if z == 4:
                flag = 1
                
print flag

