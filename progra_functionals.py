#!coding: utf-8

## Fonctions pour itérables d'itérables

# comme vu dans list_dict_set, on peut créer des itérables "en une ligne"
# et puis les envoyer à list() pour les convertir en liste par exemple
L = list((i * i) % 5 for i in range(10))
L = [(i * i) % 5 for i in range(10)]

# faire sa propre fonction d'itérable est très simple
def produit(X):
    s = 1
    for x in X:
        s = s * x
    return s

print produit(range(5,10))

# any/all : il existe, pour tout

L = [1,2,4,5,2,9]

print any(x == 4 for x in L)           # il y a t il un 4 dans L ?
print all(x != 3 for x in L)           # sont ils tous différents de 3 ?
print any(x < 10 for x in L if x >= 5) # il y a t il nombre plus petit que 10 dans les éléments de L plus grand que 5 ?
print any(x in (0,5,7) for x in L)

# une longue expression/boucle A or B or C or D devient un any((A,B,C,D))
# une longue expression/boucle A and B and C and D devient un all((A,B,C,D))

Vide = []
print any(x == 2 for x in Vide) # est ce qu'il existe un élement qui satistife x == 2 dans Vide ? Non
print all(x == 2 for x in Vide) # est ce tous les élements de Vide satisfont x == 2 dans Vide ? Oui

# any est un raccourci pour
def to_any(iterable):
    for x in iterable:
        if x:
            return True # stop, on a trouvé un élément, il existe donc un élement
    return False

# all est un raccourci pour
def to_all(iterable):
    for x in iterable:
        if not x:
            return False # stop, on a trouvé un élement qui ne satistifait pas, donc "tous les élément satisfont" est faux
    return True

# max/min/sort
print max(L) # max : le plus grand élément : 9
print min(L) # min : le plus petit élément : 1

def fonction(x):
    return -x * x * (x * x - 10)

print max(fonction(x) for x in L)      # pour tout les élements de L, le maximum de fonction(x) est 24
print max(L, key=fonction)             # 2 est le x qui a le plus grand fonction(x)
print max((fonction(x), x) for x in L) # tuple f_x, x va d'abord comparer f_x, et puis en cas d'égalité, x

print sorted(L)
print sorted([(1,2),(4,5),(1,8),(4,5),(4,2)]) # [(1,2), (1,8), (4,2), (4,5), (4,5)]
print sorted(L, key=fonction)
L.sort() # modifier la liste, ne pas renvoyer une nouvelle

## more bools

# sum of bool
print True + False # == 1, car True est converti en 1 et False en 0
print sum(L) # somme
print sum(x == 2 for x in L) # somme de booléens : comptage d'élements satifaisant une condition

# cast to bool

class Personnage:
    pass

bob = Personnage()

print bool(1)     # True
print bool(2)     # True
print bool(0)     # False
print bool(-1)    # True
print bool([])    # False
print bool({})    # False
print bool(set()) # False
print bool('')    # False
print bool(None)  # False
print bool(bob)   # True

S = []
if S: # cast to bool, shortcut here for len(S) > 0
    pass

if not S: # cast to bool
    pass

# quand transformé en bool, ces valeurs-ci sont False :
# False
# None
# les int/float == 0
# les collections vides (list,tuple,set,dict,range,str tel que len(S) == 0)
# le reste est True

# None représente le Néant, souvent utilisé quand on a besoin de représenter "Rien"
# Par exemple, dans un jeu, un perso peut Avoir une cible, Ou Pas de cible
# on dira donc cible = un_perssonage ou cible = None
# on fera if cible != None:
# ou if cible is not None:
# ou if cible:

## more functions

class Personnage:
    def __init__(self, vie):
        self.vie = vie
    def boire_potion(self, x):
        self.x = min(self.vie + x, 100)

def stuff(perso1, perso2, nombre):
    return perso1.vie + 2*perso2.vie + nombre + 2

alice = Personnage(50)
bob = Personnage(20)

# une variable peut avoir une fonction

f = stuff
print f(alice, bob, 8)

f = Personnage.boire_potion
f(alice, 7)

f = alice.boire_potion
f(10)

from functools import partial
g = partial(stuff, alice, bob) # on donne déjà les 2 premiers arguments
print g(8) # et puis le 3ème
print g(7) # idem

h = partial(nombre=7) # on donne déjà nombre, il reste donc (perso1, perso2)
print h(alice, bob)
print h(bob, alice)

def apply_to(liste_perso, fonction):
    for p in liste_perso:
        fonction(p)
        
L = [alice, bob]
apply_to(L, 
         
# fonction dans fonction

def f(x):
    
    def g(y): # fonction locale
        return y + x + 1 # ré utilise x
    
    return g(8) + g(9) * g(1) + 1

# lambda

# raccourci pour une fonction en une ligne avec un return
def machin(x,y):
    return x + y * 2

# raccourci :
machin = lambda x,y: x + y * 2 # return implicite

# plus utilisé dans les expressions
apply_to(L, lambda p: bob.boire_potion(h(p, bob)))

# fonctions qui return des fonctions

def f(x):
    
    def g(y):
        return y + x + 1 # ré-utilise x
    
    return g

p = f(8)
print p(1) # 10