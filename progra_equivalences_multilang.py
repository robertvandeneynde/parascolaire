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
# inverser if/else 
##
if CONDITION:
    A
else:
    B
# ↔
if not(CONDITION):
    B
else:
    A

## ex{{e|a}}mple 1
if a == 5:
    print("hello")
else:
    waw = 2
# ↔ ({{inverser if/else|invert if/else}})
if not(a == 5):
    waw = 2
else:
    print("hello")
# ↔ (not == ↔ !=)
if a != 5:
    waw = 2
else:
    print("hello")

###
# {{sinon ne rien faire|else do nothing}}
###
if CONDITION:
    A
else:
    pass  # {{ne rien faire|do nothing}}
# → 
if CONDITION:
    A

## ex{{e|a}}mple 1
if a != 5:
    print("hello")
else:
    pass  # {{ne rien faire|do nothing}}
# → ({{"sinon ne rien faire" est inutile|"else do nothing" is useless}})
if a != 5:
    print("hello")

## ex{{e|a}}mple 2
if a == 5:
    pass  # {{ne rien faire|do nothing}}
else:
    print("hello")
# → ({{inverser if/else|invert if/else}})
if a != 5:
    print("hello")
else:
    pass  # {{ne rien faire|do nothing}}
# → ({{"sinon ne rien faire" est inutile|"else do nothing" is useless}})
if a != 5:
    print("hello")
    
###
# {{simplifier not|simplify not}} ({{lois de De Morgan|De Morgan's laws}})
###
# De Morgan {{sur|on}} "{{et|and}}"
if not(A and B):
    ...
# ↔
if (not A) or (not B):
    ...

# De Morgan {{sur|on}} "{{ou|or}}"
if not(A or B):
    ...
# ↔
if (not A) and (not B):
    ...

## ex{{e|a}}mple 1
if not(a > 10 or a == 5):
    print('hello')
# → (De Morgan)
if a <= 10 and a != 5:
    print('hello')
    
## ex{{e|a}}mple 2
if a > 10 or a == 5:
    pass
else:
    print('hello')
# → ({{inverser if/else|invert if/else}})
if not(a > 10 or a == 5):
    print('hello')
else:
    pass
# → ({{"sinon ne rien faire" est inutile|"else do nothing" is useless}})
if not(a > 10 or a == 5):
    print('hello')
# → (De Morgan)
if a <= 10 and a != 5:
    print('hello')

###
# if variable 
###
if CONDITION:
    x = A
else:
    x = B
# →
x = A if CONDITION else B
# →
x = (A if CONDITION else B)
# →
x = (A if CONDITION else
     B)

## ex{{e|a}}mple
if a == 5:
    c = 2
else:
    c = 0
# → ({{"if en une ligne" aussi appelé "l'opérateur ternaire" ou le "if fonctionnel"|"one-line if" also called "ternary operator" or "functional if"}})
c = (5 if a == 5 else 0)
# ↔ ({{parenthèses non nécessaires|parenthesis are useless}})
c = 5 if a == 5 else 0

##
# if elif cascade on variable
##
if CONDITION:
    x = A
elif CONDITION_2:
    x = B
elif CONDITION_3:
    x = C
else:
    x = D
# → 
x = (A if CONDITION else
     B if CONDITION_2 else
     C if CONDITION_3 else
     D)

## ex{{e|a}}mple
if a == 5:
    c = 8
elif a == 2:
    c = 4
elif a < 0:
    c = 1
else:
    c = 0
# → ({{if fonctionnel|functional if}})
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
# {{Généralement les noms de variables de quelques lettres sont <strong>trop court</strong>|Generally variable names of few letters are <strong>too short</strong>}}
# ({{sauf dans des expressions mathématiques ou des noms de variables connues comme le <code>"i"</code> dans une boucle|except in mathematical expressions or well known variable names like the <code>"i"</code> in a loop}})
# {{et des variables avec plus de trois vrais mots ont un nom <strong>trop long</strong>|and variable names with more than three real words are <strong>too long</strong>}}
# ({{un commentaire à la création de la variable sera sûrement plus clair|a comment next to the variable creation will be probably better}}).

## 
# inline variable
##
x = ...
operation(x)
# → ({{à condition que x n'est utilisé qu'une fois|only possible if x is used only once}})
operation(...)
## ex{{e|a}}mple
x = {{taille|size}} + 1  # x {{dépend de la taille|depends on the size}}
y = {{taille|size}} - 1  # y {{dépend de la taille|depends on the size}}
{{le_coefficent|the_coefficent}} = x + 2 * y  # {{on calcule le coefficent avec la formule linéaire|let's compute the coefficent using the linear formula}}
print({{le_coefficent|the_coefficent}})       # {{on l'affiche|let's print it}}

# ↔ (inline variable "{{le_coefficent|the_coefficent}}")
x = {{taille|size}} + 1  # x {{dépend de la taille|depends on the size}}
y = {{taille|size}} - 1  # y {{dépend de la taille|depends on the size}}
print(x + 2 * y)  # {{on affiche le résultat de la formule linéaire|let's print the result of the linear formula}}

# ↔ (inline variables "x" and "y")
print(({{taille|size}} + 1) + 2 * ({{taille|size}} - 1))  # {{on affiche le résultat de la formule linéaire en fonction de la taille|let's print the result of the linear formula depending on the size}}

##
# boolean return
##
def f(...):
    ...
    if CONDITION:
        return True
    else:
        return False
# →
def f(...):
    ...
    return CONDITION

## ex{{e|a}}mple 1
def {{est_pair|is_even}}(x):
    if x % 2 == 0:    # {{si le reste de la division par deux vaut 0|if the rest of division by 2 is 0}}
        return True   # Vrai, le nombre est pair
    else:             # sinon
        return False  # Faux, le nombre n'est pas pair
# → (boolean return)
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
# → (boolean return)
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
if CONDITION:
    A
elif CONDITION_2:
    A  # {{même A|same A}}
# →
if CONDITION or CONDITION_2:
    A
    
## ex{{e|a}}mple
if a == 5:
    x = 2
elif a > 10:
    x = 2
# → (or)
if a == 5 or a > 10:
    x = 2
    
##
# or else
##
if CONDITION:
    A
elif CONDITION_2:
    A  # {{même A|same A}}
else:
    B
# →
if CONDITION or CONDITION_2:
    A
else:
    B

## ex{{e|a}}mple
if a == 5:
    x = 2
elif a > 10:
    x = 2
else:
    print('error')
# → (or)
if a == 5 or a > 10:
    x = 2
else:
    print('error')

##
# or return
##
def f(...):
    ...
    if CONDITION:
        return True
    if CONDITION_2:
        return True
    return False
# →
def f(...):
    ...
    return CONDITION or CONDITION_2
# ↔
def f(...):
    ...
    return (CONDITION
            or CONDITION_2)

## ex{{e|a}}mple
def {{interessant|interesting}}(x):
    if x > 10:  # {{si x > 10|if x > 10}}
        return True  # {{il est intéressant|it's interesting}}
    if x == 5:  # {{si x == 5|if x == 5}}
        return True  # {{il est intéressant|it's interesting}}
    return False  # {{sinon, il n'est pas intéressant|otherwise, it's not interesting}}
# → (or return)
def {{interessant|interesting}}(x):
    return x > 10 or x == 5  # {{x est intéressant si il est > 10 ou == 5|x is interesting if it's > 10 or 5}}

##
# and
##
if CONDITION:
    if CONDITION_2:
        A
# →
if CONDITION and CONDITION_2:
    A

## ex{{e|a}}mple
if a == 5:
    if a > 10:
        print('waw')
# → (and)
if a == 5 and a > 10:
    print('waw')

##
# and else
##
if CONDITION:
    if CONDITION_2:
        A
    else:
        B
else:
    B  # {{même b|same b}}
# →
if CONDITION and CONDITION_2:
    A
else:
    B

## ex{{e|a}}mple
if a == 5:
    if b > 10:
        waw = 2 
    else:
        print('error')
else:
    print('error')
# → (and)
if a == 5 and b > 10:
    waw = 2
else:
    print('error')

##
# if return
##
def f(...):
    ...
    if CONDITION:
        return X
    ...
# ↔
def f(...):
    ...
    if CONDITION:
        return X
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
# → (if return)
def f(x):
    if x < 0:
        return -1
    y = x + 2
    z = y ** 2
    return z

# {{Je fais généralement ça quand le <code>"if"</code> est vraiment court comme un simple <code>"return"</code>|I generally do that when the <code>"if"</code> is really short like a simple <code>"return"</code>}}.
# Souvent, ce sont des cas particuliers ou des cas de base, le code du bas est plus intéressant.

##
# for if return True (∃)
## for-if-return-True, any, exists, ∃ 
# {{Voici comment on code un "∃"|Here is how we code a "∃"}}
def f(...):
    ...
    for x in L:
        if condition:  # {{ce "if" n'a PAS de "else"|this "if" DOESN'T have a "else"}}
            return True
    return False
# → (en python, il y a "all")
def f(...):
    ...
    return any(condition for x in L)
# ↔
def f(...):
    ...
    return any(condition
               for x in L)

# {{Note: en python, il y a aussi le [for...else](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops#9980752) mais peu de gens l'utilisent|Note: in python there is also the [for...else](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops#9980752) but not so much people use it}}

## ex{{e|a}}mple
def {{contient_un_negatif|contains_a_negative}}(L):
    for x in L:  # {{pour tous les élements de la liste|for each element in the list}}
        if x < 0:  # {{s'il est < 0|if it's < 0}}
            return True  # {{la liste contient_un_negatif|the list contains_a_negative}}
    return False  # {{au final, c'est qu'elle n'en contient pas|in the end, it means it doesn't contain one}}
# → (any)
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
## for-if-return-False, all, forall, ∀
# {{Voici comment on code un "∀"|Here is how we code a "∀"}}
def f(...):
    ...
    for x in L:
        if condition:  # {{ce if n'a PAS de "else"|this "if" DOESN'T have a "else"}}
            return False
    return True
# → (en python, il y a "all")
def f(...):
    return all(not condition for x in L)
# ↔
def f(...):
    return all(not condition
               for x in L)

# {{Note: en python, il y a aussi le [for...else](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops#9980752) mais peu de gens l'utilisent|Note: in python there is also the [for...else](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops#9980752) but not so much people use it}}

## ex{{e|a}}mple
def {{totalement_positive|totally_positive}}(L):
    for x in L:  # {{pour tous les élements de la liste|for each element in the list}}
        if x < 0:  # {{s'il est < 0|if it's < 0}}
            return False  # {{la liste n'est pas totalement_positive|the list is not totally_positive}}
    return True  # {{au final, c'est que la liste est totalement_positive|in the end, the list is totally_positive}}
# → (all)
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
# not ∀/∃ ({{lois de De Morgan|De Morgan's laws}})
## not-any, not-all
# De Morgan {{sur|on}} "∀"
not all(condition for x in L)
# →
any(not condition for x in L)

# De Morgan {{sur|on}} "∃"
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
# {{Voici comment on code une recherche linéaire|Here is how one code a linear search}}
def f(...):
    for x in L:
        if condition:
            return a
    return b
# → ({{en python, il y a "next"|in python, one can use "next"}})
def f(...):
    return next((a for x in L if condition), b)
# ↔
def f(...):
    return next((a for x in L if condition),
                b)

# {{Note: en python, il y a aussi le [for...else](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops#9980752) mais peu de gens l'utilisent|Note: in python there is also the [for...else](https://stackoverflow.com/questions/9979970/why-does-python-use-else-after-for-and-while-loops#9980752) but not so much people use it}}

## ex{{e|a}}mple
#
# <em>Le super_nombre d'une liste est le <strong>premier</strong> x dans la liste tel que x > 10</em> :
def {{super_nombre|super_number}}(L):
    for x in L:  # {{pour tous les élements de la liste|for each element in the list}}
        if x > 10:  # {{s'il est > 10|if it's > 10}}
            return x  # {{c'est le super nombre de cette liste|it's the super_number of that list}}
    return 0  # il n'y a pas de super nombre, on renvoie 0
# →
def {{super_nombre|super_number}}(L):
    return next((x for x in L if x > 10), 0)

##
# for append
##
L = []
for x in iterable:
    L.append(e)
# →
L = [e for x in iterable]

##
# for append f(x)
## +, map
L = []
for x in iterable:
    L.append(f(x))
# →
L = list(map(f, iterable))
# ↔
L = [f(x) for x in iterable]

##
# for if append
## 
L = []
for x in iterable:
    if condition:
        L.append(e)
# →
L = [e for x in iterable if condition]

##
# for if f(x) append x
## +, filter
L = []
for x in iterable:
    if f(x):
        L.append(x)
# →
L = list(filter(f, iterable))
# ↔
L = [x for x in iterable if f(x)]

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

## ex{{e|a}}mple
s = 0
for x in L:
    s += a
# → (sum)
s = sum(a for x in L)

# {{techniquement, "sum" est un cas particulier de "reduce" mais "reduce" est peu utile en python|technically, "sum" is a particular case of "reduce" but "reduce" is a bit useless in python}}

##
# in tuple (python)
##

## ex{{e|a}}mple
if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
    ...
# → (in)
if x in ('a', 'e', 'i', 'o', 'u'):
    ...

# {{c'est un cas particulier de recherche linéaire dans une liste|it's a particular case of linear search in a list}}



    
    
        



