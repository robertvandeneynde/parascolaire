#!coding: utf-8

# Vous connaissez déjà plusieurs manière de lancer une exception

L = [1,2,7,2]
a = L[4] # IndexError : list index out of range

D = {'a': 5}
a = D['b'] # KeyError : 'b'

print(x) # NameError : name 'x' is not defined

def f(x):
    print(x)
    
f()    # TypeError, f() takes 1 positional arguments but 2 were given
f(1,2) # TypeError, f() takes 1 positional arguments but 3 were given

a = int('')      # ValueError : invalid
a = int('hello') # idem

L.index(3)       # ValueError chercher un 3 dans la liste L

## try : except

try:
    d = D['a']
    i = L.index(3)
except ValueError: # si le code du try lance une ValueError
    i = -1
except KeyError:   # si le code du try lance une KeyError
    i = -1
else: # si aucune erreur n'a été lancée
    print("Yep") 

# on peut également atrapper Toutes les exceptions
try:
    d = D['a']
    i = L.index(3)
except:
    i = -1

## raise ses propres exceptions

def f(x):
    if x < 0:
        raise ValueError('x must be positive or 0')
    return x * x

try:
    print(f(-5))
except ValueError:
    print("Erreur")

class MyException(Exception): # C'est une génériques
    def __init__(self, val):
        self.val = val
    
try:
    raise MyException(8)
except MyException as e: # as pour avoir l'objet lancé
    print("erreur :", e.val)