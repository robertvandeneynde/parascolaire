#!coding: utf-8

L = [1,2,7,2,1,6]

# Que vaut L au fil du temps ?
# Qu'affiche ce code ?
# Avez-vous remarqué ce que fait ce code ?

i = 0

n = len(L) - 1

while i < len(L):
    j = 0
    
    while j < n:
        
        if L[j+1] > L[j]:
            s = L[j]
            L[j] = L[j+1]
            L[j+1] = s
            
        j = j + 1
    
    i = i + 1
    n = n - 1 
    
print L
