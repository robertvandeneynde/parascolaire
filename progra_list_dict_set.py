#!coding: utf-8

## plus sur les LISTES (et tuples) !
# toutes les opérations décrites dessus pevuvent 
# bien sûr être écrites avec les 4 opérations de base

L = [1,2,7,2] # T = (1,2,7,2)

# itérer
for x in L:
    print(x)

# itérer avec l'index
for i,x in enumerate(L):
    print(i, x)

# chercher : est ce que je peux trouver un élément qui est égal à x ?
if 2 in L: # 2 in T
    print("2 est dans la liste")
    b = L.index(2) # savoir l'index
    print("... à la position", b)

# comparer deux listes/deux tuples : == !=

if L == [1,2,7,2]: # T == (1,2,7,2)
    print("L == [1,2,7,2]")

if L != [1,2,2,7]: # T == (1,2,2,7)
    print("L != [1,2,2,2]")
# +, *, slice (comme sur les strings, voir [theorie2_liste_while.py](theorie2_liste_while.py.html))
print([1,2] + [3,4]) # [1,2,3,4]
print([1,2] * 3)     # [1,2,1,2,1,2]
print([1,2,7,2][1:]) # [2,7,2]

# extend : "ajouter tous les éléments d'une autre list
D = [8,6]
L.extend(D) # L = [1,2,7,2,8,6]

# comparer deux listes/deux tuples : < > <= >=

if [1,2,3] < [1,2,4]: # (1,2,3) < (1,2,4)
    print("[1,2,3] < [1,2,4]")

if [1,2,3] >= [1,0,4]:
    print("[1,2,3] >= [1,0,4]")

if [1,2] < [1,2,3]:
    print("[1,2] < [1,2,3]")
    
if [1,5] > [1,2,3]:
    print("[1,2] < [1,2,3]")
    
# python regarde le premier élément et fait la comparaison
# s'ils sont égaux il passe aux deux suivants et refait la comparaison
# c'est de la même manière que l'on compare des mots
# "hello" < "ijkl"
# "hell" < "hello"

## MATRICE

# pour faire des grilles, ou des matrices, on fait des ...

M = [ [1,2,3,4], [5,6,7,8] ] # liste de listes !
print(M[0]) # [1,2,3,4]
print(M[0][0]) # 1
print(M[1][0]) # 5
print(M[0][1]) # 2

a = [8,2,4,3]
M.append(a)
a = [1,2,4,4]
M.append(a)

if M == [ [1,2,3,4], [5,6,7,8], [8,2,4,3], [1,2,4,4] ]:
    print("M est une matrice à 4 lignes et 4 colonnes")

## DICT

D = {} # Un dictionnaire vide

D = {5:2, 3:4} # Un dictionnaire avec deux éléments
# Le premier élément a la CLEF 5 et la VALEUR 2
# Le duxième élément a la clef 3 et la valeur 4

if 5 in D: # tester si il existe un élément avec la clef 5
    y = D[5] # on demande la valeur de la clef 5 → y = 2
    print("5 a la valeur", y)

if 0 not in D:
    print("Pas de zéro")

D[9] = 7 # imposer que la valeur correspondant à 9 vaut 7
print(len(D)) # 3 clef différentes !
D[9] = 4 # ici la clef 9 existe déjà, donc ça va changer sa valeur
print(len(D)) # toujours 3 clef différentes

del D[9] # supprimer l'élément à la clef 9

if D != {2;1, 3:4}: # deux dicts sont égaux s'ils ont les mêmes clefs/valeurs
    print("D != {2:1, 3:4}")

# Vu que les élément sont identifiés par des clefs,
# ils n'ont pas d'ordre 

for x,y in D.items(): # itérer les éléments, dans un certain ordre
    print("clef", x, "valeur", y)
    
for x in D: # itérer les clefs, dans un certain ordre
    print("clef", x)

for x in D.keys(): # itérer les clefs, dans un certain ordre
    print("clef", x)

for x in D.values(): # itérer les valeurs, dans un certain ordre
    print("values", x)

## SET

# un set est un ensemble sans ordre d'éléments uniques (pas de doublons)
# si vous voulez un ordre et des doublons, choisissez une LISTE

X = set() # un ensemble vide
S = {1,4,8} # un ensemble avec des valeurs

S.add(2) # S = {1,4,8,2}
print(len(S)) # 4
S.add(4) # déjà dedans...
print(len(S)) # 4

S = {1,4,8,2}

# tester l'appartenance

if 2 in S: # très rapide, même pour les grands set
    print("2 !")
    
if 0 not in S:
    print("not 0 !")

# il n'y a pas d'ordre

if S == {1,2,4,8}:
    print("S == {1,2,4,8}")

if S == {1,4,8,1}:
    print("S == {1,4,8,1}")

for x in S: # x va valoir 1,4,8,2 dans un certain ordre
    print("élément", x)
    
S.remove(4) # enlève 4 et lance une erreur s'il n'est pas dedans
S.discard(4) # enlève 4 et ne fait rien s'il n'est pas dedans

# opérations : intersection, union, différence

A = {1,2,3}
B = {2,3,4}

print(A & B) # intersection : {2,3} les éléments qui sont dans A ET dans B
print(A | B) # union : {1,2,3,4} # les élements qui sont dans A OU dans B
print(A - B) # différence : {1} (les éléments de A sans les éléments de B) # les éléments qui sont dans A ET NON B
print(A ^ B) # différence symétrique = (A - B) | (B - A) : {1,4} # les élements qui sont dans A OU B mais pas les deux

# A & B : les éléments qui sont dans A ET dans B
# A | B : les élements qui sont dans A OU dans B
# A - B : les éléments qui sont dans A ET NON B
# A ^ B : les élements qui sont dans A OU B mais pas les deux

# être un sous ensemble : ⊆ ⊇ ⊂ ⊃, en python : <= >= < > 

if {1,2} <= {1,2,3}: # {1,2} ⊆ {1,2,3}
    print("{1,2} ⊆ {1,2,3}")
    
# A <= B signifie "tous les éléments de A sont dans B"
# A < B signifie "A <= B" ET A != B
# A >= B signifie "B <= A"
# A > B signifie "B < A"

## Que mettre dans un set ou en clef d'un dict ?

# int
D = {5:2, 9:1}
S = {8,1,2}

# string
D = {"hello": 5, "world": 1}
S = {"hello", "world"}

# tuple
D = {(1,2): 5, (8,1): 1}
S = {(8,2), (7,1)}

print(D[(1,2)])
print(D[1,2]) # pas besoin de parenthèses ici

# objets
class Personnage:
    pass

alice = Personnage()
bob = Personnage()

D = {alice: 5, bob: 1}
print D[alice]

L = [alice, bob]

for perso in L:
    print D[perso]

vivants = {alice, bob}

vivants.add(bob) # vu que bob est dedans, ça ne fait rien !

# frozenset
F = frozenset([1,2,4])
F.add(1) # error : ne peut être modifié (immutable)
# grâce à l'immutabilité, peut-être mis dans un set/clef d'un dict !

S = {
    frozenset([1,2,4]),
    frozenset([1,2]),
    frozenset([2,1]),
}

print S == {frozenset([1,2,4]), frozenset([1,2])} # True

print frozenset((1,4,2)) in S # True !

# les 

# CONVERSIONS / ITÉRABLES
# list()/tuple() / set()/frozenset() / enumerate() acceptent n'importe quel itérable

L = [1,2,7,2]
S = set(L) # {1,7,2}
T = tuple(L)
Lb = list(S) # attention, on ne sait pas l'ordre d'itération
a,b,c = S # le unpacking marche avec n'importe quel itérable
D = {'hello':2, 'world':3}
Lc = list(D) # Lc == ['hello', 'world'] dans un certain ordre car un dict est un itérable de clef
Ld = list(D.items()) # Lc == [('hello', 2), ('world', 3)] dans un certain ordre car dict.items() est un itérable de tuple de taille 2

# list(X), est donc un raccourci pour :
def to_list(X):
    L = []
    for x in X:
        L.append(x)
    return L

# set(X), est donc un raccourci pour :
def to_set(X):
    S = set()
    for x in X:
        S.add(x)
    return S

# generator expressions

S = set([(i * i) % 5 for i in range(10)]) # pratique avec les list comprehesion
S = set((i * i) % 5 for i in range(10))   # sans les [], ça crée un "itérable", parfait pour donner à set()

# dict() accepte soit un autre dict, soit un itérable de tuple de taille 2
L = [["hello",2],["world",3],["hello",8]]
D = dict(L) # D == {'hello':8, 'world':3}, le dernier est pris
D2 = dict(D)
D2['world'] = 1

# dict(X) est donc un raccourci pour
def to_dict(X):
    D = {}
    if isinstance(X, dict):
        for x,y in X.items():
            D[x] = y
    else:
        for x,y in X:
            D[x] = y
    return D

# un petit mix ?
print(dict(
    (y,x)
    for x,y in enumerate(
        n * 2
        for n in range(5,10)
        if n % 3 != 0
    )
))

# explication :

# range(5,10)
# -> 5,6,7,8,9

# (n * 2 for n in _ if n % 3 != 0)
#  > 5 ? 5 % 3 != 0, OK ! (5 * 2) = 10
#  > 6 ? 5 % 3 == 0, PAS OK
#  > 7 ? 5 % 3 != 0, OK ! (5 * 2) = 14
#  > 8 ? 5 % 3 != 0, OK ! (5 * 2) = 16
#  > 9 ? 5 % 3 == 0, PAS OK
# -> 10, 14, 16

# enumerate(_) ?
# -> (0,10),(1,14),(2,16)

# (y,x) for x,y in _ ?
#  > x,y = 0,10 -> (10,0)
#  > x,y = 1,14 -> (14,1)
#  > x,y = 2,16 -> (16,2)
# -> (10,0), (14,1), (16,2)

# dict(_) ?
# {10:0, 14:1, 16:2}

    
