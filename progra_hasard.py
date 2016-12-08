#!coding: utf-8
import random

x = random.randrange(3) # x est un entier au hasard entre 0 et 3 NON COMPRIS

# les print suivants peuvent 3 valeurs différentes : 0 ou 1 ou 2
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))
print(random.randrange(3))

#######################
# Pour en savoir plus #
#######################

a = 5
b = 10
liste = [1,2,7,2]

# à partir de randrange, on peut faire plein de fonctions
# voici une liste de fonctions qui existent mais qu'il est facile de refaire :
print(random.randrange(a,b)) # un nombre au hasard x entre a et b non compris 
print(random.randint(a,b)) # un nombre au hasard x entre a et b compris 
print(random.choice(liste)) # un élément au hasard dans la liste

# Pour ceux qui ne veulent pas chercher deux minutes comment les refaire à partir, voici la correction :
# randrange(a,b) = a + randrange(b - a)
# randint(a,b) = randrange(a, b+1)
# choice(liste) = liste[ randrange( len(liste) ) ]

# et voici une fonction qui mélange une liste (exercice)
random.shuffle(liste)
print(liste)

################################
# Pour en savoir VRAIMENT plus #
################################

# random.seed permet de mettre un nombre inital qui fait que les prochaines valeurs renvoyées sont connues
random.seed(89)
random.randrange(5) # toujours 0 (python 2.7)
random.randrange(5) # toujours 3
random.randrange(5) # toujours 4
random.randrange(5) # toujours 0
