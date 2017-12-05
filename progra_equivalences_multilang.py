"""
{{Vous avez un code qui marche, et vous voulez le rendre plus joli, plus lisible.|You have a working code, and you want it to be more clean, more pretty, more readable.}}
{{C'est ce qu'on appelle du refactoring.|This is what we call, refactoring.}}
{{Voici une liste de transformations disponibles pour vous aider dans cette tâche.|Here is a list of transformation to help you in this task.}}
{{Vous pouvez bien sûr choisir de faire la transformation ou non.|You can of course choose to apply the transformation or not.}}
{{Un "→" indique que ce code sera probablement plus clair (selon moi).|A "→" means the code will probably be more readable (according to me).}}
{{Un "↔" indique que la clarté dépendra du contexte (il n'y en n'a pas un qui soit à priori plus clair).|A "↔" means the clarity will depend on the context (neither code is a priori more readable).}}
"""

##
# if/else
##
if condition:
    a
else:
    b
# ↔
if not(condition):
    b
else:
    a

## ex{{e|a}}mple 1
if a == 5:
    print("hello")
else:
    print("world")
# ↔
if not(a == 5):
    print("world")
else:
    print("hello")
# ↔
if a != 5:
    print("world")
else:
    print("hello")

## ex{{e|a}}mple 2
if a == 5:
    pass # {{ne rien faire|do nothing}}
else:
    print("hello")
# →
if a != 5:
    print("hello")
else:
    pass # {{ne rien faire|do nothing}}
# →
if a != 5:
    print("hello")

###
# if variable 
###
if condition:
    x = a
else:
    x = b
# →
x = a if condition else b
# →
x = (a if condition else b)
# →
x = (a if condition else
     b)

##
# if elif cascade on variable
##
if condition:
    x = a
elif condition2:
    x = b
elif condition3:
    x = c
else:
    x = d
# →
x = (a if condition else
     b if condition2 else
     c if condition3 else
     d)

## 
# inline variable
##
x = ...
operation(x)
# → ({{à condition que x n'est utilisé qu'une fois|only possible if x is used only once}})
operation(...)

##
# boolean return
##
def f(...):
    ...
    if condition:
        return True
    else:
        return False
# →
def f(...):
    ...
    return condition

## ex{{e|a}}mple
def {{est_pair|is_even}}(x):
    if x % 2 == 0: # {{si le reste de la division par deux vaut 0|if the rest of division by 2 is 0}}
        return True
    else:
        return False
if {{est_pair|is_even}}(4):
    print("launch the secret code !")
# →
def {{est_pair|is_even}}(x):
    return x % 2 == 0 # {{x est pair ssi le reste de la division par deux vaut 0|x is even iff the rest of division by 2 is 0}}
if {{est_pair|is_even}}(4):
    print("launch the secret code !")
# 

##
# == True 
##
# {{avec|with}}
def {{est_pair|is_even}}(x):
    if x % 2 == 0: # {{si le reste de la division par deux vaut 0|if the rest of division by 2 is 0}}
        return True
    else:
        return False
# :
if {{est_pair|is_even}}(4) == True: # {{si la fonction est_pair renvoie True|si the is_even function returns True}}
    ...
# →
if {{est_pair|is_even}}(4): # {{si 4 est pair|if 4 is even}}
    ...

##
# or
##
if condition:
    a
elif condition2:
    a # {{même a|same a}}
# →
if condition or condition2:
    a
    
##
# or else
##
if condition:
    a
elif condition2:
    a # {{même a|same a}}
else:
    b
# →
if condition or condition2:
    a
else:
    b

##
# or return
##
def f(...):
    ...
    if condition:
        return True
    if condition2:
        return True
    return False
# →
def f(...):
    ...
    return condition or condition2
# ↔
def f(...):
    ...
    return (condition
            or condition2)

##
# and
##
if condition:
    if condition2:
        a
# →
if condition and condition2:
    a

##
# and else
##
if condition:
    if condition2:
        a
    else:
        b
else:
    b # {{même b|same b}}
# →
if condition and condition2:
    a
else:
    b

##
# if return
##
def f(...):
    ...
    if condition:
        return x
    ...
    return y
# ↔
def f(...):
    ...
    if condition:
        return x
    else:
        ...
        return y

##
# for if return True
##
def f(...):
    ...
    for x in L:
        if condition:
            return True
    return False
# →
def f(...):
    return any(condition for x in L)
# ↔
def f(...):
    return any(condition
               for x in L)

## ex{{e|a}}mple
def {{contient_un_negatif|contains_negative}}(L):
    for x in L:
        if x < 0:
            return True
    return False
# →
def {{contient_un_negatif|contains_negative}}(L):
    return any(x < 0 for x in L) # {{L contient un négatif si il y a un élément x < 0|L contains a negative if there is a x < 0}}
    # {{L contient un négatif ssi il existe un x in L tel que x < 0|L contains a negative if there exists any x such that x < 0}}

##
# for if return False
##
def f(...):
    ...
    for x in L:
        if condition:
            return False
    return True
# →
def f(...):
    return all(not condition for x in L)
# ↔
def f(...):
    return all(not condition
               for x in L)

## ex{{e|a}}mple
def {{tous_positif|totally_positive}}(L):
    for x in L:
        if x < 0:
            return False
    return True
# →
def tous_positif(L):
    return any(x >= 0 for x in L) # {{L est totalement positive si tous ses éléments x sont >= 0|L is totally positive if all its elements x are >= 0}}
    # {{L est totalement positive ssi pour tout les éléments x ∈ L on a x >= 0|L is totally positive if for all its elements x one have x >= 0}}
    # {{L est totalement positive ssi quelque soit l'élément x ∈ L on a x >= 0|L is totally positive if any element x ∈ L satisfies x >= 0}}

##
# for if return else return 
##
def f(...):
    for x in L:
        if condition:
            return a
    return b
# → (python)
def f(...):
    return next((a for x in L if condition), b)
# ↔
def f(...):
    return next((a for x in L if condition),
                b)
##
# for append
##
L = []
for x in I:
    L.append(e)
# →
L = [e for x in I]

##
# for append f(x)
##
L = []
for x in I:
    L.append(f(x))
# →
L = list(map(f, I))
# ↔
L = [f(x) for x in I]

##
# for if append
##
L = []
for x in I:
    if cond:
        L.append(e)
# →
L = [e for x in I if cond]

##
# for if f(x) append x
##
L = []
for x in I:
    if f(x):
        L.append(x)
# →
L = list(filter(f, I))
# ↔
L = [x for x in I if f(x)]

##
# Itérer un générateur (python)
##
for x in list(generat{{eu|o}}r):
    ...
# →
for x in generat{{eu|o}}r:
    ...

## ex{{e|a}}mple 1
for x in list(map(f L)): # map, filter...
    ...
# →
for x in map(f, L):
    ...

## ex{{e|a}}mple 2
# {{avec|with}}
def operation(x):
    return (x + 1) * 2 - x
# :
for x in list(map(operation, [1,2,3])):
    print(x)
# →
for x in map(operation, [1,2,3]):
    print(x)

##
# sum
##
s = 0
for x in L:
    s += a
# →
s = sum(a for x in L)



    
    
        



