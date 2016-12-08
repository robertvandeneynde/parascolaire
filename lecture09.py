#!coding: utf-8

# Que valent les valeurs de L, S, C, i, j au cours du temps ?
# Qu'affiche ce code ?

L = []
S = []
i = 0
while i < 10:
    S.append(i + 1)
    
    C = []
    j = 0
    while j < len(S):
        C.append(S[j])
        j = j + 1
        
    L.append(C) # une liste peut contenir une liste !
    

print(L[2])
print(L[2][0])
