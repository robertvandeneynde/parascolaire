"""
{{Équivalences|Equivalences}}

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
    waw = True
# ↔
if not(a == 5):
    waw = True
else:
    print("hello")
# ↔
if a != 5:
    waw = True
else:
    print("hello")

## ex{{e|a}}mple 2
if a == 5:
    pass  # {{ne rien faire|do nothing}}
else:
    print("hello")
# →
if a != 5:
    print("hello")
else:
    pass  # {{ne rien faire|do nothing}}
# →
if a != 5:
    print("hello")
    
###
# {{simplifier not|simplify not}} (De Morgan)
###
if not(A and B):
    ...
# ↔
if (not A) or (not B):
    ...

if not(A or B):
    ...
# ↔
if (not A) and (not B):
    ...

## ex{{e|a}}mple
if a > 10 or a == 5:
    pass
else:
    print('hello')
# →
if not(a > 10 or a == 5):
    print('hello')
else:
    pass
# →
if not(a > 10 or a == 5):
    print('hello')
# →
if a <= 10 and a != 5:
    print('hello')

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

### ex{{e|a}}mple
if a == 5:
    c = 2
else:
    c = 0
# →
c = (5 if a == 5 else 0)
# ↔
c = 5 if a == 5 else 0

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

### ex{{e|a}}mple
if a == 5:
    c = 8
elif a == 2:
    c = 4
elif a < 0:
    c = 1
else:
    c = 0
# →
c = (8 if a == 5 else
     4 if a == 2 else
     1 if a < 0 else
     0)

##
# renaming
##
#
# {{Vous pouvez renommer une variable pour lui donner un nom plus explicite|You can rename a variable to give it a name more explicit}} :
e = v * t
i = e / 2.56
# →
distance = {{vitesse|velocity}} * {{temps|time}}
distance_{{pouces|inch}} = distance / 2.56
# {{Cependant, ne tombez pas dans le piège inverse !|However, don't fall in the reverse trap!}}
# {{Dans certains cas, des variables courtes sont plus compréhensibles|Sometimes short names are more understandable}}
# {{comme par exemple dans une expression mathématique complexe|for instance in a complex mathematical expression}}

## 
# inline variable
##
x = ...
operation(x)
# → ({{à condition que x n'est utilisé qu'une fois|only possible if x is used only once}})
operation(...)
## ex{{e|a}}mple
{{le_coefficent|the_coefficent}} = x + 2 * y  # {{on calcule le coefficent avec la formule linéaire|let's compute the coefficent using the linear formula}}
print({{le_coefficent|the_coefficent}})       # {{on l'affiche|let's print it}}
# ↔
print(x + 2 * y)  # {{on affiche le résultat de la formule linéaire|let's print the result of the linear formula}}

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

## ex{{e|a}}mple 1
def {{est_pair|is_even}}(x):
    if x % 2 == 0:  # {{si le reste de la division par deux vaut 0|if the rest of division by 2 is 0}}
        return True
    else:
        return False
# →
def {{est_pair|is_even}}(x):
    return x % 2 == 0  # {{x est pair ssi le reste de la division par deux vaut 0|x is even iff the rest of division by 2 is 0}}
# :
if {{est_pair|is_even}}(4):
    ...
    
## ex{{e|a}}mple 2
def {{voyelle|vowel}}(x):
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        return True
    else:
        return False
# →
def {{voyelle|vowel}}(x):
    return x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u'  # {{x est une voyelle ssi x vaut 'a', 'e', 'i', 'o', ou 'u'|x is a vowel iff x is 'a', 'e', 'i', 'o', 'u'}}
# :
if {{voyelle|vowel}}('a'):  # {{si 'a' est une voyelle|if 'a' is a vowel}}
    ...

##
# == True 
##
# {{avec|given}}
def {{est_pair|is_even}}(x):
    if x % 2 == 0:  # {{si le reste de la division par deux vaut 0|if the rest of division by 2 is 0}}
        return True
    else:
        return False
# :
if {{est_pair|is_even}}(4) == True:  # {{si la fonction est_pair renvoie True|si the is_even function returns True}}
    ...
# →
if {{est_pair|is_even}}(4):  # {{si 4 est pair|if 4 is even}}
    ...

##
# or
##
if condition:
    a
elif condition2:
    a  # {{même a|same a}}
# →
if condition or condition2:
    a
    
## ex{{e|a}}mple
if a == 5:
    x = 2
elif a > 10:
    x = 2
# →
if a == 5 or a > 10:
    x = 2
    
##
# or else
##
if condition:
    a
elif condition2:
    a  # {{même a|same a}}
else:
    b
# →
if condition or condition2:
    a
else:
    b

## ex{{e|a}}mple
if a == 5:
    x = 2
elif a > 10:
    x = 2
else:
    print('error')
# →
if a == 5 or a > 10:
    x = 2
else:
    print('error')

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

## ex{{e|a}}mple
def {{interessant|interesting}}(x):
    if x > 10:  # {{si x > 10|if x > 10}}
        return True  # {{il est intéressant|it's interesting}}
    if x == 5:  # {{si x == 5|if x == 5}}
        return True  # {{il est intéressant|it's interesting}}
    return False  # {{sinon, il n'est pas intéressant|otherwise, it's not}}
# →
def {{interessant|interesting}}(x):
    return x > 10 or x == 5  # {{x est intéressant si il est > 10 ou == 5|x is interesting if it's > 10 or 5}}

##
# and
##
if condition:
    if condition2:
        a
# →
if condition and condition2:
    a

## ex{{e|a}}mple
if a == 5:
    if a > 10:
        print('waw')
# →
if a == 5 and a > 10:
    print('waw')

##
# and else
##
if condition:
    if condition2:
        a
    else:
        b
else:
    b  # {{même b|same b}}
# →
if condition and condition2:
    a
else:
    b

## ex{{e|a}}mple
if a == 5:
    if b > 10:
        waw = True 
    else:
        print('error')
else:
    print('error')
# →
if a == 5 and b > 10:
    waw = True
else:
    print('error')

##
# if return
##
def f(...):
    ...
    if condition:
        return x
    ...
# ↔
def f(...):
    ...
    if condition:
        return x
    else:
        ...

## ex{{e|a}}mple
def f(x):
    if x < 0:
        return -1
    else:
        y = x + 2
        z = y ** 2
        return z
# →
def f(x):
    if x < 0:
        return -1
    y = x + 2
    z = y ** 2
    return z

# Je fais généralement ça quand le if est tout court comme un simple return.
#

##
# for if return True (∃)
## for-if-return-True
def f(...):
    ...
    for x in L:
        if condition:
            return True
    return False
# →
def f(...):
    ...
    return any(condition for x in L)
# ↔
def f(...):
    ...
    return any(condition
               for x in L)

## ex{{e|a}}mple
def {{contient_un_negatif|contains_a_negative}}(L):
    for x in L:  # {{pour tous les élements de la liste|for each element in the list}}
        if x < 0:  # {{s'il est < 0|if it's < 0}}
            return True  # {{la liste contient_un_negatif|the list contains_a_negative}}
    return False  # {{au final, c'est qu'elle n'en contient pas|in the end, it means it doesn't contain one}}
# →
def {{contient_un_negatif|contains_a_negative}}(L):
    return any(x < 0 for x in L)
# {{Qui se lira <em>Une liste L contient un négatif si</em>...|We'll read it as <em>A list L contains_a_negative if...</em>}}
# <ul>
# <li> {{il y a un élément x < 0|there is a x < 0}}
# <li> {{il existe un x de L tel que x < 0|there exists any x such that x < 0}}
# <li> ∃ x ∈ L: x < 0
# </ul>

##
# for if return False (∀)
## ## for-if-return-False
def f(...):
    ...
    for x in L:
        if condition:
            return False
    return True
# → (python)
def f(...):
    return all(not condition for x in L)
# ↔
def f(...):
    return all(not condition
               for x in L)

## ex{{e|a}}mple
def {{totalement_positive|totally_positive}}(L):
    for x in L:  # {{pour tous les élements de la liste|for each element in the list}}
        if x < 0:  # {{s'il est < 0|if it's < 0}}
            return False  # {{la liste n'est pas totalement_positive|the list is not totally_positive}}
    return True  # {{au final, c'est que la liste est totalement_positive|in the end, the list is totally_positive}}
# → (python)
def {{totalement_positive|totally_positive}}(L):
    return all(x >= 0 for x in L)
# {{Qui se lira <em>Une liste L est totalement_positive si</em>|We'll read it as <em>A list L is totalement_positive if</em>}}...
# <ul>
# <li> {{tous ses éléments x sont >= 0|A list is totally positive if all its elements x are >= 0}}
# <li> {{pour tous les éléments x ∈ L on a x >= 0|for all its elements x one have x >= 0}}
# <li> {{quelque soit l'élément x ∈ L on a x >= 0|any element x ∈ L satisfies x >= 0}}
# <li> ∀ x ∈ L : x >= 0
# </ul>

##
# not ∀/∃ (De Morgan)
##
not all(condition for x in L)
# →
any(not condition for x in L)

not any(condition for x in L)
# →
all(not condition for x in L)

## ex{{e|a}}mple
if not all(x >= 0 for x in L):  # si on n'a pas tous les nombres >= 0
    ...
# → (if non empty)
if any(x < 0 for x in L):  # c'est qu'il existe un nombre < 0
    ...
# <strong>Attention</strong>: cette transformation ne marche pas si L est vide !
#

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

## ex{{e|a}}mple
#
# <em>Le super_nombre d'une liste est le <strong>premier</strong> x dans la liste tel que x > 10</em> :
def {{super_nombre|super_number}}(L):
    for x in L:  # {{pour tous les élements de la liste|for each element in the list}}
        if x > 10:  # {{s'il est > 10|if it's > 10}}
            return x  # {{c'est le super nombre de cette liste|it's the super_number of that list}}
    return 0
# →
def {{super_nombre|super_number}}(L):
    return next((x for x in L if x > 10), 0)

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
    if condition:
        L.append(e)
# →
L = [e for x in I if condition]

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
# {{itérer un générateur|iterate a generator}} (python)
##
for x in list(generat{{eu|o}}r):
    ...
# →
for x in generat{{eu|o}}r:
    ...

## ex{{e|a}}mple 1
for x in list(map(f, L)):  # map, filter, zip...
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

##
# in tuple (python)
##
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    ...
# →
if x in ('a', 'e', 'i', 'o', 'u'):
    ...




    
    
        



