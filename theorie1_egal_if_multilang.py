#!coding: utf-8
from __future__ import print_function, division

##################
# Base {{UNE|ONE}} : "=" #
##################

# "=" {{permet de changer la valeur d'une variable|allows you to change the value of a variable}}
# print() {{permet de voir à l'écran la valeur d'une variable|allows you to see on screen the value of a variable}}
a = 5
print(a) # {{en python 2, les parenthèses n'étaient pas nécessaires|in python 2, the parenthesis were not mandatory}}
a = 6
print(a)

# {{on peut faire des maths|we can do maths}}
b = a + 1
c = a + b * 2   # {{priorité des opérations|priority of operations}}
d = (a + b) * 2 # {{mettre des parenthèses si nécessaire !|put parenthesis if needed!}}
a = a + 1       # {{on calcule "a + 1", puis on met le résultat dans a, ce qui veut dire "a est augmenté de 1"|calculate "a + 1", then put the result in a, this means "a is incremented by 1"}}
print(a)
print(b)
print(c)
print(d)

# {{pour afficher du texte, il faut le mettre entre guillemets|to print text, one must put in between quotes}}
print("{{fin|end}}")

####################
# Base {{DEUX|TWO }} : "if" #
####################

a = 7

if a < 10:
    print("{{Coucou|Kookoo}}")
    print("Hello")
    
# {{ici le programme va afficher "Coucou", puis "Hello" seulement si a est plus petit que 10|here, the program will display "Kookoo", then "Hello" only if a is smaller than 10}}
# {{sinon, il saute le bloc et donc, ne fait rien|otherwise, the block is jumped and then, nothing is done}}

# {{un autre exemple, on veut donner 50 points de vie à un personnage, sans dépasser 100...|another example, one wants to give 50 life points (hp) to a character, without going over 100...}}
{{vie|life}} = 75
{{vie|life}} = {{vie|life}} + 50
if {{vie|life}} > 100:
    {{vie|life}} = 100

# {{pour afficher plusieurs choses on écrit une virgule|to display more than one thing, one must write a comma}}
print("{{Votre vie est|your life is}}", {{vie|life}}) # {{en python 2, les parenthèses n'étaient pas obligatoires|in python 2, the parenthesis were not mandatory}}

# {{on peut faire un else, le code ira dans le else si la condition est fausse|one can do a "else", the code will go in the else if the condition is false}}
if {{vie|life}} == 100:
    print("Full!")
else:
    print("Drink potions!")

# {{les opérateurs de comparaison sont|the comparison operators are}} "<", ">", "<=", ">=", "==", "!=" ({{différent|different}})
# {{attention, pour comparer deux valeurs il faut utiliser|beware, to compare two values, one must use}} "=="
# {{ainsi le code précédent affiche "Full!" si vie vaut 100, sinon "Drink potions!"|therefore the previous code displays "Full!" if the life is 100, else "Drink potions!"}}
# {{essaie de réécrire le code précédent en utilisant l'opérateur "!=" (différent)|try to re-write the previous code by using the "!=" (different) operator}}

# {{Dans un if, on peut mettre n'importe quel code|in a if, one can put any code}}
# {{Comme un "=", un print, ou... un autre if !|like a "=", a print, or... another if!}}

if a == 5:
    a = 2
    print("Yo")
    if b == 5:
        print("Hello")
    else:
        print("Tada")
else:
    print("Hum")
   
print(a)
    
# {{Essaie ce programme avec|Try this program with}} a=5 b=5, a=5 b=2, a=2 b=2 {{et voit ce qu'il se passe|and see what is going on}}

# {{Fais maintenant l'exercice 0 ([trier_deux_nombres.py]())|do now the exercice number 0 ([trier_deux_nombres.py]())}}
# {{regarde la correction sur|look at the correction on}} [pythontutor](pythontutor.html)

# J'ai également fait une [vidéo](https://robertvandeneynde.be/clipedia/structure-variables-conditions.mp4) sur la théorie 1.

# {{Ensuite tu peux faire les exercices 1 à 4 sans lire la suite|After you can do exercices 1 to 4 without the need to read the following}}
# {{Cependant la suite PEUT être utile pour les exercices suivants|However the following CAN be useful for the next exercices}}

# {{On peut écrire des conditions combinées avec "and" et "or", par exemple :|One can write combined conditions with "and" and "or", for example:}}

if a == 1 and b == 2:
    print("Yo")
else:
    print("Da")

# {{est un programme qui affiche "Yo" si a est égal à 1 et b est égal à 2, sinon Da|is a program that displays "Yo" if a is equal to 1 and b is equal to 2, Da otherwise}}
# {{les Deux conditions doivent être vraies|both conditions must be true}}
# {{Celui ci :|This one:}}

if a == 1 or b == 2:
    print("Yo")
else:
    print("Da")

# {{affiche Yo si a est égal à 1 ou b est égal à 2|displays Yo if a is equal to 1 or b is equal to 2}}
# {{ou moins une des deux conditions doit être vraie|at least one condtion must be true}}

# {{attention, si tu mélanges des and et des or,|beware, if you mix and and or,}}
# {{utilise des parenthèses pour bien préciser l'ordre des opérations|use parenthesis to be clear on the order you want to use}}

if a == 2 or b == 2 and c == 2: # {{qui du "or" ou du "and" a la priorité ?|Who has the greater priority? The "and" or the "or"?}}
    print("Yo")

# {{équivalent au précédent : or est "comme" un +, and est "comme" un *|equivalent to the previous one: or is "like" a +, and is "like" a *}}
if a == 2 or (b == 2 and c == 2):
    print("Yo")
    
if (a == 2 or b == 2) and c == 2:
    print("Yo")
    
##{{###################|############}}##
# {{Pour en savoir plus|To know more}} #
##{{###################|############}}##

## =

# {{des raccourcis pour incrémenter/décrémenter !|some shortcuts for increment/decrement}}

a = a + 1
a += 1 # {{raccourci pour|shortcut for}} a = a + 1
a -= 1 # {{raccourci pour|shortcut for}} a = a - 1
a *= 2 # a = a * 2
# etc.

# floats ({{nombre à virgule, notez que "entier" se dit "integer" en anglais, souvent abbrégé en "int"|floating/decimal numbers}})
a = 2.5
a = 2.5e6 # {{la notation "e" crée toujours un float, ici 2.5 * 10^6 = 2.5 millions|the "e" notation}}
a = 2e6   # 2000000.0, {{un float|a float}}

# {{exposant|power}}
a = 2 ** 5      # 2 {{exposant|power}} 5 = 32, int ** int = int
a = 2.1 ** 2    # float ** int = float
a = 10 ** 0.5   # number ** float = float
a = 2 * 10 ** 6 # 2000000, {{un|a}} int, {{remarquez que l'exposant a priorité sur le|let's notice that power has priority on}} "*"

# {{division entière|integer division}} // {{et|and}} modulo %
# {{si on divise 14 par 4 on a 3 avec un reste de 2 (comme en primaire !)|when 14 is divided by 4, one obtains 3 with a rest of 2 (remember primary school!)}}
a = 14 / 4        # 3.5 ({{attention ! En python 2|beware! In python 2}}, 14 / 4 = 3)
a = 14 / 4.0      # 3.5
a = 14 / float(4) # 3.5
a = 14 // 4       # 3
a = 14 // 4.0     # 3.0

div = 14 // 4 # 3, {{la partie entière|the integer part}}
mod = 14 % 4 # 2, {{le reste|the rest}}

# {{modulo négatifs, observez le cycle 0 1 2 3 4 :|(negative modulos, observe the cycle 0 1 2 3 4:}} (python is cool !)
n = -1 % 5 # 4
n =  0 % 5 # 0
n =  1 % 5 # 1
n =  2 % 5 # 2
n =  3 % 5 # 3
n =  4 % 5 # 4
n =  5 % 5 # 0
n =  6 % 5 # 1

## {{plusieurs lignes|multiple lines}}

# {{si on ouvre une parenthèse, on peut passer à la ligne autant que l'ont veut|if one opens a parenthesis, one can go to the next line until the parenthesis is closed}}
x = (5 + 2 * 3
       + 7 * 2
       + 1
       - 2)

# {{écrire en binaire/hexadécimal|write in binary/hexadecimal}}
print(0b100)    # 4
print(0xa2)     # 162
print(hex(162)) # 0xA2
print(bin(4))   # 0b100

## multiple {{comparaisons|comparisons}}

if 2 <= a <= 5: # 2 <= a and a <= 5
    print("{{a est entre 2 et 5|a is between 2 and 5}}")

if a == b == 0: # a == b and b == 0
    print("{{a et b valent 0|a and b are equal to 0}}")

## not "inverser" une condition

if a == 5: # si a == 5...
    pass # ne rien faire
else:
    print("a n'est pas égal à 5")

# équivalent à

if not(a == 5):
    print("a n'est pas égal à 5")
else:
    pass # ne rien faire

# équivalent à 

if not(a == 5):
    print("a n'est pas égal à 5")
# "sinon ne rien faire" est une opération inutile, on peut donc l'enlever

# équivalent à 
if a != 5:
    print("a n'est pas égal à 5")
    
# en effect, au choix du programmeur, le not peut être simplifié :
# not(a == b)  ↔ a != b
# not(a < b)   ↔ a >= b (ATTENTION : plus grand ou ÉGAL)
# not(X and Y) ↔ (not X) or (not Y) (ATTENTION : OR)
# not(X or Y)  ↔ (not X) and (not Y)
# les deux dernières lois sont souvent appelées "lois de De Morgan"

if not(a == 5 and b < 7):
    print("not(a == 5 and b < 7)")
    
if a != 5 or b >= 7: # équivalent au précédent
    print("a != 5 or b >= 7")
    
# en règle générale, quand on a un if / else quelconque
# on peut, au choix, inverser la condition en mettant un "not"
# conseil: quand vous avez un long if et un court "else", c'est souvent plus clair d'inverser

if a != 5 and a > 0:
    print("yoyo")
    print("tada")
    print("truc")
    
    if a == 4:
        print("da")
    else:
        print("yo")
        
else: # ce "else" est court et oublié :(
    print("coucou")

# on peut (au choix) l'inverser en "not(X)" sa condition :
if not(a != 5 and a > 0): # appliquez les lois de De Morgan si vous voulez
    print("coucou") # aaah, l'ancien else est mis en avant :) 
else:
    print("yoyo")
    print("tada")
    print("truc")
    if a == 4:
        print("da")
    else:
        print("yo")

## elif : parfois, on a un "else" qui ne contient qu'une seule instruction, qui est un "if"

if a < 5:
    print("petit")
else:
    if a < 10:
        print("moyen")
    else:
        if a < 15:
            print("grand")
        else:
            print("graaaand")

# raccourci : elif (else if)

if a < 5: # si a < 5
    print("petit")
elif a < 10: # sinon... si a < 10
    print("moyen")
elif a < 15:
    print("grand")
else:
    print("graaaand")

## bool: les conditions peuvent être mises dans des variables
# un (booléen) vaut Vrai ou Faux (True / False)

condition = (a < 5)
if condition == True:
    print("Plus petit !")
else:
    print("Plus grand ou egal")
    
# le "if" attend un bool, on peut donc enlever "== True"

condition = a < 5 # parenthèse non nécessaires
if condition: # == True enlevé
    print("Plus petit")
else:
    print("Plus grand ou egal")

# on peut donc faire des "opérations" sur les bool

x = True
y = False
z = x or y # z = True or False = True
n = not x # n = not True = False
g = a < 5 and z

## if fonctionnel : parfois, on a un "if/else" qui ne fait qu'assigner une variable (et rien d'autre !)

if a == 5:
    b = 8
else:
    b = 3

# raccourci: le "if/else" "en une ligne"
b = (8 if a == 5 else 3) # même code qu'au dessus

b = 8 if a == 5 else 3 # parenthèses non nécessaires

b = (8 if a == 5 else
     3) # deux lignes c'est plus clair !

c = (8 if a == 5 else
     4 if a == 2 else
     1 if a < 0 else
     0) # longue chaine !
