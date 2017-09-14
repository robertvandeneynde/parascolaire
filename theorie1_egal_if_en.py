#!coding: utf-8
from __future__ import print_function, division

##################
# Base ONE : "=" #
##################

# "=" allows you to change the value of a variable
# print() allows you to see on screen the value of a variable
a = 5
print(a) # in python 2, the parenthesis were not mandatory
a = 6
print(a)

# we can do maths
b = a + 1
c = a + b * 2   # priority of operations
d = (a + b) * 2 # parenthesis if needed!
a = a + 1       # calculate "a + 1", then put the result in a, this means "a is incremented by 1"
print(a)
print(b)
print(c)
print(d)

# to print text, one must put in between quotes
print("end")

####################
# Base TWO  : "if" #
####################

a = 7

if a < 10:
    print("Kookoo")
    print("Hello")
    
# here, the program will display "Kookoo", then "Hello" only if a is smaller than 10
# otherwise, the block is jumped and then, nothing is done

# another example, one wants to give 50 life points (hp) to a character, without going over 100...
life = 75
life = life + 50
if life > 100:
    life = 100

# to display more than one thing, one must write a comma
print("your life is", life) # in python 2, the parenthesis were not mandatory

# one can do a "else", the code will go in the else if the condition is false
if life == 100:
    print("Full!")
else:
    print("Drink potions!")

# the comparison operators are "<", ">", "<=", ">=", "==", "!=" (different)
# beware, to compare two values, one must use "=="
# therefore the previous code displays "Full!" if the life is 100, else "Drink potions!"
# try to re-write the previous code by using the "!=" (different) operator

# in a if, one can put any code
# like a "=", a print, or... another if!

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
    
# Try this program with a=5 b=5, a=5 b=2, a=2 b=2 and see what is going on

# do now the exercice number 0 ([trier_deux_nombres.py]())
# look at the correction on [pythontutor](pythontutor.html)

# After you can do exercices 1 to 4 without the need to read the following
# However the following CAN be useful for the next exercices

# One can write combined conditions with "and" and "or", for example:

if a == 1 and b == 2:
    print("Yo")
else:
    print("Da")

# is a program that displays "Yo" if a is equal to 1 and b is equal to 2, Da otherwise
# both conditions must be true
# This one:

if a == 1 or b == 2:
    print("Yo")
else:
    print("Da")

# displays Yo if a is equal to 1 or b is equal to 2
# at least one condtion must be true

# beware, if you mix and and or,
# use parenthesis to be clear on the order you want to use

if a == 2 or b == 2 and c == 2: # Who has the greater priority? The "and" or the "or"?
    print("Yo")

# equivalent to the previous one: or is "like" a +, and is "like" a *
if a == 2 or (b == 2 and c == 2):
    print("Yo")
    
if (a == 2 or b == 2) and c == 2:
    print("Yo")
    
####
# To know more #
################

## =

# some shortcuts for increment/decrement

a = a + 1
a += 1 # shortcut for a = a + 1
a -= 1 # shortcut for a = a - 1
a *= 2 # a = a * 2
# etc.

# floats (floating/decimal numbers)
a = 2.5
a = 2.5e6 # the "e" notation
a = 2e6   # 2000000.0, a float

# power
a = 2 ** 5      # 2 power 5 = 32, int ** int = int
a = 2.1 ** 2    # float ** int = float
a = 10 ** 0.5   # number ** float = float
a = 2 * 10 ** 6 # 2000000, a int, let's notice that power has priority on "*"

# integer division // and modulo %
# when 14 is divided by 4, one obtains 3 with a rest of 2 (remember primary school!)
a = 14 / 4        # 3.5 (beware! In python 2, 14 / 4 = 3)
a = 14 / 4.0      # 3.5
a = 14 / float(4) # 3.5
a = 14 // 4       # 3
a = 14 // 4.0     # 3.0

div = 14 // 4 # 3, the integer part
mod = 14 % 4 # 2, the rest

# (negative modulos, observe the cycle 0 1 2 3 4: (python is cool !)
n = -1 % 5 # 4
n =  0 % 5 # 0
n =  1 % 5 # 1
n =  2 % 5 # 2
n =  3 % 5 # 3
n =  4 % 5 # 4
n =  5 % 5 # 0
n =  6 % 5 # 1

## multiple lines

# if one opens a parenthesis, one can go to the next line until the parenthesis is closed
x = (5 + 2 * 3
       + 7 * 2
       + 1
       - 2)

# write in binary/hexadecimal
print(0b100)    # 4
print(0xa2)     # 162
print(hex(162)) # 0xA2
print(bin(4))   # 0b100

## multiple comparisons

if 2 <= a <= 5: # 2 <= a and a <= 5
    print("a is between 2 and 5")

if a == b == 0: # a == b and b == 0
    print("a and b are equal to 0")

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