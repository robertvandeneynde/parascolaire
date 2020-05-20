#!coding: utf-8
from __future__ import print_function, division

###
# Base {{UNE|ONE}} : "="
### {{egal|equal}}

# <nav class="external">
# <a class="video" href="https://www.youtube.com/watch?v=zJ-w2izNvg4">Programmation — Théorie 1 : Structure, variables et conditions</a>
# </nav>
# <br/>
# <nav class="external">
# <a class="video" href="https://youtu.be/fForqjCBVeY">Théorie 1, prise en main et <code>exercice0</code></a>
# </nav>

#
# <span span>Allez sur [repl.it python3](https://repl.it/site/languages/python3) ou bien ouvrez Wing 101 (téléchargeable sur [le site de Wing](https://wingware.com/downloads/wingide-101)). </i>

# {{Les variables permettent de stocker une valeur dans la mémoire de l'ordinateur |Variables are useful to store a value in the memory of the computer}}:
# <ul><li> <code>"="</code> {{permet de changer la valeur d'une variable|allows you to change the value of a variable}}
# <li> <code>print()</code> {{permet d'afficher à l'écran la valeur d'une variable|allows you to see on screen the value of a variable}} </ul>
a = 5
print(a)
a = 6
print(a)

# <span class="comment">{{en python 2, les parenthèses n'étaient pas nécessaires|in python 2, the parenthesis were not mandatory}}

#
# {{On peut faire des maths |We can do maths}}:
b = a + 1        # {{b vaut maintenant a + 1 = 7|b is now a + 1 = 7}}
c = a + b * 2    # {{priorité des opérations|priority of operations}}
d = (a + b) * 2  # {{mettre des parenthèses si nécessaire !|put parenthesis if needed!}}
print(b)         # {{b n'a pas changé depuis qu'on a fait "b ="|b didn't change since the time we did "b ="}}
print(c)
print(d)

#
# {{On peut modifier une variable existante |We can modify an existing variable}}:
a = a + 1        # {{on calcule "a + 1", puis on met le résultat dans a|calculate "a + 1", then put the result in a}}
print(a)         # {{La variable "a" a donc été augmentée de 1"|The variable "a" is then incremented by 1.}}

#
# {{Pour afficher du texte, il faut le mettre entre guillemets |To print text, one must put in between quotes}}:
print("{{fin|end}}")

#
# {{Pour afficher plusieurs choses on écrit une virgule|To display more than one thing, one must write a comma}}:
print("{{J'ai|I have}}", a, "{{patates|potatoes}}")  # {{en python 2, les parenthèses n'étaient pas obligatoires|in python 2, the parenthesis were not mandatory}}

# Essayez ce code sur [pythontutor](http://pythontutor.com/visualize.html#code=a%20%3D%205%0Aprint%28a%29%20%20%23%20en%20python%202,%20les%20parenth%C3%A8ses%20n'%C3%A9taient%20pas%20n%C3%A9cessaires%0Aa%20%3D%206%0Aprint%28a%29%0A%0Ab%20%3D%20a%20%2B%201%20%20%20%20%20%20%20%20%23%20b%20vaut%20maintenant%20a%20%2B%201%20%3D%207%0Ac%20%3D%20a%20%2B%20b%20*%202%20%20%20%20%23%20priorit%C3%A9%20des%20op%C3%A9rations%0Ad%20%3D%20%28a%20%2B%20b%29%20*%202%20%20%23%20mettre%20des%20parenth%C3%A8ses%20si%20n%C3%A9cessaire%20!%0Aa%20%3D%20a%20%2B%201%20%20%20%20%20%20%20%20%23%20on%20calcule%20%22a%20%2B%201%22,%20puis%20on%20met%20le%20r%C3%A9sultat%20dans%20a%0Aprint%28a%29%20%20%20%20%20%20%20%20%20%23%20La%20variable%20%22a%22%20a%20donc%20%C3%A9t%C3%A9%20augment%C3%A9e%20de%201%22%0Aprint%28b%29%20%20%20%20%20%20%20%20%20%23%20b%20n'a%20pas%20chang%C3%A9%20depuis%20qu'on%20a%20fait%20%22b%20%3D%22%0Aprint%28c%29%0Aprint%28d%29%0A%0Aprint%28%22{{fin|end}}%22%29&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false) !
# Cliquez sur <strong>Visualize execution</strong> puis cliquez sur <strong>Forward</strong> pour exécuter chaque ligne ou sur <strong>Last</strong> pour voir uniquement le résultat final.
# Le résultat imprimé en raison de <code>"print"</code> est affiché dans le cadre <em>Print output</em>.

# {{Petite, question, quelle est la différence entre|A little question, what's the difference between}}
# <code>print(a)</code> {{et|and}} <code>print("a")</code>{{ |}}?

###
# Base {{DEUX|TWO }} : "if" 
### if
#
# {{Qu'affiche ce programme |What does this program print}}?

a = 7

if a < 10:
    print("{{Coucou|Kookoo}}")
    print("Hello")
    
# Le code se dit <em>est-ce que a < 10 ? Oui!</em>
# et donc il affiche <em>Coucou</em>, puis <em>Hello</em>.

# [Remplace](http://pythontutor.com/visualize.html#code=a%20%3D%207%0A%0Aif%20a%20%3C%2010%3A%0A%20%20%20%20print%28%22%7B%7BCoucou%7CKookoo%7D%7D%22%29%0A%20%20%20%20print%28%22Hello%22%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# maintenant <code>a = 7</code> par <code>a = 12</code> et relance le programme,
# quelle va être la difference ?

a = 12  # DIFF

if a < 10:
    print("{{Coucou|Kookoo}}")
    print("Hello")
    
# Quand <code>a = 12</code>, le code se dit <em>est-ce que a < 10 ? Non!</em>
# il saute le <code>if</code> et ne fait rien.

#
# Et celui là ? 

a = 7  # DIFF

if a < 10:
    print("{{Coucou|Kookoo}}")
print("Hello")  # DIFF
    
# Correction: 
#

# Et celui-là ?
#

a = 12  # DIFF

if a < 10:
    print("{{Coucou|Kookoo}}")
print("Hello")  # DIFF
    
# Correction: ...
#

# {{Le bloc if de ce programme va afficher <em>Coucou</em> puis <em>Hello</em> seulement si a est plus petit que 10|The if-block in this program will display "Kookoo" then "Hello" only if a is smaller than 10}},
# {{sinon, il saute le bloc et donc, ne fait rien|otherwise, the block is jumped and then, nothing is done}}.
# [{{Essayez|Try}}](http://pythontutor.com/visualize.html#code=a%20%3D%207%0A%0Aif%20a%20%3C%2010%3A%0A%20%20%20%20print%28%22Coucou%22%29%0A%20%20%20%20print%28%22Hello%22%29&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# {{avec d'autres valeurs de <code>a</code>, comme|with other values of <code>a</code>, like}} <code>a = 12</code> ou <code>a = 10</code> {{par exemple|for example}}.

# Mais si on veut quand même faire quelque chose quand la condition est fausse ?
# C'est là que vient le <code>else</code> :

if a < 10:
    print("{{Coucou|Kookoo}}")
    print("Hello")
else:               # NEW
    print("Tadaa")  # NEW

# Si a < 10: le programme affiche <em>{{Coucou|Kookoo}}</em> puis <em>Hello</em>,
# sinon il affiche <em>Tadaa</em>.

## Diagrammes et exemple réels !

#
# {{Un autre exemple, on veut donner 50 points de vie à un personnage, sans dépasser 100...|Another example, one wants to give 50 life points (hp) to a character, without going over 100...}}
{{vie|life}} = 75
{{vie|life}} = {{vie|life}} + 50
if {{vie|life}} > 100:
    {{vie|life}} = 100

#
# {{Pour afficher plusieurs choses on écrit une virgule|To display more than one thing, one must write a comma}}:
print("{{Votre vie est de|your life is}}", {{vie|life}})  # {{en python 2, les parenthèses n'étaient pas obligatoires|in python 2, the parenthesis were not mandatory}}

# {{Voici une représentation en diagramme de|Here is a diagram representation of}} [{{ce|that}} if]({{http://pythontutor.com/visualize.html#code=vie%20%3D%2080%0A%0Avie%20%3D%20vie%20%2B%2050%0Aif%20vie%20%3E%20100%3A%0A%20%20%20%20print%28%22Max%20!%22%29%0A%20%20%20%20vie%20%3D%20100%0A%0Aprint%28vie%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false|http://pythontutor.com/visualize.html#code=life%20%3D%2080%0A%0Alife%20%3D%20life%20%2B%2050%0Aif%20life%20%3E%20100%3A%0A%20%20%20%20print%28%22Max!%22%29%0A%20%20%20%20life%20%3D%20100%0A%0Aprint%28life%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false}}) :
# <figure><img height=400 src="if_as_diagram.{{fr|en}}.svg"/></figure>

#
# {{On peut faire un <code>else</code>, le code ira dans le <code>else</code> si la condition est fausse|One can do a <code>else</code>, the code will go in the <code>else</code> if the condition is false}}:
if {{vie|life}} == 100:
    print("{{Rempli|Full}}!")
else:
    print("Potions!")

#
# {{Ainsi le code précédent affiche <code>"Rempli!"</code> si vie vaut 100, sinon il affiche <code>"Potions!"</code>|Therefore the previous code displays <code>"Full!"</code> if the life is 100, else it displays <code>"Potions!"</code>}}.

# {{Voici un diagramme de|Here is a diagram of}} [{{ce|this}} if/else]({{http://pythontutor.com/visualize.html#code=if%20vie%20%3D%3D%20100%3A%0A%20%20%20%20print%28%22Rempli!%22%29%0Aelse%3A%0A%20%20%20%20print%28%22Potions!%22%29%0A%0Aprint%28%22Fin%22%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false|http://pythontutor.com/visualize.html#code=if%20life%20%3D%3D%20100%3A%0A%20%20%20%20print%28%22Full!%22%29%0Aelse%3A%0A%20%20%20%20print%28%22Potions!%22%29%0A%0Aprint%28%22End%22%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false}}) :
# <figure><img height=270 src="ifelse_as_diagram.{{fr|en}}.svg"/></figure>

## {{Les opérateurs de comparaison|The comparison operators}}
# {{Les opérateurs de comparaison sont|The comparison operators are}}
# <code>"<", ">", "<=", ">=", "==", "!="</code> ({{différent|different}}).

# {{Attention, pour comparer deux valeurs il faut utiliser|Beware, to compare two values, one must use}} <code>"=="</code>.
# et non <code>"="</code>. 
# Autrement dit, <em>si un <code>"="</code> est dans un if, il doit avoir être doublé</em>.

# On se rappelle que <code>a = 5</code> veut dire <em>imposer que a vaut 5</em>
# alors que <code>a == 5</code> veut dire <em>est-ce que a vaut 5 ?</em>

#
# {{Petit exercice, essaie de réécrire le code précédent en utilisant l'opérateur <code>"!="</code> (différent)|As an exercice, try to re-write the previous code by using the <code>"!="</code> (different) operator}}.

## Récapitulons
# {{Dans un <code>if</code>, on peut mettre n'importe quel code|In a <code>if</code>, one can put any code}},
# {{comme un <code>"="</code>, un <code>"print"</code>, ou... un autre <code>"if"</code>|like a <code>"="</code>, a <code>"print"</code>, or... another <code>"if"</code>}}!

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

# {{Essaie ce programme avec plusieurs valeurs et vois ce qu'il se passe|Try this program with mutliple values and see what's going on}}{{ |}}: <ul>
# <li> [<code>a = 5; b = 5;</code>](http://pythontutor.com/visualize.html#code=a%20%3D%205%0Ab%20%3D%205%0A%0Aif%20a%20%3D%3D%205%3A%0A%20%20%20%20a%20%3D%202%0A%20%20%20%20print%28%22Yo%22%29%0A%20%20%20%20if%20b%20%3D%3D%205%3A%0A%20%20%20%20%20%20%20%20print%28%22Hello%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Tada%22%29%0Aelse%3A%0A%20%20%20%20print%28%22Hum%22%29%0A%20%20%20%0Aprint%28a%29&cumulative=false&curInstr=1&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# <li> [<code>a = 5; b = 2;</code>](http://pythontutor.com/visualize.html#code=a%20%3D%205%0Ab%20%3D%202%0A%0Aif%20a%20%3D%3D%205%3A%0A%20%20%20%20a%20%3D%202%0A%20%20%20%20print%28%22Yo%22%29%0A%20%20%20%20if%20b%20%3D%3D%205%3A%0A%20%20%20%20%20%20%20%20print%28%22Hello%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Tada%22%29%0Aelse%3A%0A%20%20%20%20print%28%22Hum%22%29%0A%20%20%20%0Aprint%28a%29&cumulative=false&curInstr=1&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# <li> [<code>a = 2; b = 2;</code>](http://pythontutor.com/visualize.html#code=a%20%3D%202%0Ab%20%3D%202%0A%0Aif%20a%20%3D%3D%205%3A%0A%20%20%20%20a%20%3D%202%0A%20%20%20%20print%28%22Yo%22%29%0A%20%20%20%20if%20b%20%3D%3D%205%3A%0A%20%20%20%20%20%20%20%20print%28%22Hello%22%29%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20print%28%22Tada%22%29%0Aelse%3A%0A%20%20%20%20print%28%22Hum%22%29%0A%20%20%20%0Aprint%28a%29&cumulative=false&curInstr=1&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# </ul>
    
# {{Fais maintenant [l'exercice 0](exercice0_trier_deux_nombres.html)|Do now the [exercice number 0](exercice0_trier_deux_nombres.html)}}
# {{et regarde|and look at}} [{{la correction|the correction}}](http://pythontutor.com/visualize.html#code=a%20%3D%205%0Ab%20%3D%202%0A%0Aif%20a%20%3C%20b%3A%0A%20%20%20print%28a%29%0A%20%20%20print%28b%29%0Aelse%3A%0A%20%20%20print%28b%29%0A%20%20%20print%28a%29&py=3)
# {{sur|on}} [pythontutor](pythontutor.html). {{Pour cet exercice, quels sont les cas à tester ? J'en vois au moins deux !|For that exercise, which case must I test ? I see at least two interesting cases!}}

#
# J'ai également fait une [vidéo](https://youtu.be/zJ-w2izNvg4) sur cette page de théorie.

#
# Pour continuer la théorie, place à [la théorie 2](theorie2_liste_while.py.html)!

#
# {{Mais avant ça, je conseille de faire les exercices 1 à 4|But before doing that, I suggest to do exercices 1 to 4}}.

# <ul>
# <li> [exercice0_trier_deux_nombres.py](exercice0_trier_deux_nombres.html)
# <li> [exercice1_minute_suivante.py](exercice1_minute_suivante.html)
# <li> [exercice2_minute_suivante_un_print.py](exercice2_minute_suivante_un_print.html)
# </ul>

#
# {{Tu peux aussi lire la section ci-dessous qui parle de <code>"and/or"</code> car elle <strong>peut</strong> t'être utile pour les exercices 3 et 4|you can also read the the section <strong>below</strong> about <code>"and/or"</code> that can be useful for the exercices 3 and 4}}.

# <ul>
# <li> [exercice3_trier_trois_nombres.py](exercice3_trier_trois_nombres.py.html)
# <li> [exercice4_le_sept_parfait.py](exercice4_le_sept_parfait.py.html)
# <li> [theorie2_liste_while.py](theorie2_liste_while.html)
# </ul>

## Les conditions combinées avec and et or
#
# {{On peut écrire des conditions combinées avec <code>"and"</code> et <code>"or"</code>, par exemple :|One can write combined conditions with <code>"and"</code> and <code>"or"</code>, for example:}}

if a == 1 and b == 2:
    print("Yo")
else:
    print("Da")

# {{Ce programme affiche <code>"Yo"</code> si a est égal à 1 et b est égal à 2, sinon <code>"Da"</code>|This program displays <code>"Yo"</code> if a is equal to 1 and b is equal to 2, <code>"Da"</code> otherwise}}.
# {{Les <strong>deux</strong> conditions doivent être vraies|<strong>both</strong> conditions must be true}}.
# {{Il est appelé le <em>et logique</em>|It's called the <em>logical and</em>}}.
# Voici une représentation en diagramme d'un exemple de <code>"and"</code> :
# <figure><img height=495 src="and_as_diagram.{{fr|en}}.svg"/></figure>

# [Essayez]({{http://pythontutor.com/visualize.html#code=if%20a%20%3E%205%20and%20a%20%3D%3D%202%3A%0A%20%20%20%20print%28%22Waw%20!%22%29%0A%0Atruc%20%3D%2050%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false|http://pythontutor.com/visualize.html#code=a%20%3D%201%0Ab%20%3D%202%0A%0Aif%20a%20%3E%205%20and%20a%20%3D%3D%202%3A%0A%20%20%20%20print%28%22Wow!%22%29%0A%0Athing%20%3D%2050%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false}})
# de changer les valeurs de a et b pour vérifier que les flèches corespondent bien au code.

#
# {{On peut également utiliser <code>"or"</code> |We can also use <code>"or"</code>}}:

if a == 1 or b == 2:
    print("Yo")
else:
    print("Da")

# {{Ce programme affiche <code>"Yo"</code> si a est égal à 1 ou b est égal à 2|This program displays <code>"Yo"</code> if a is equal to 1 or b is equal to 2}}.
# {{<strong>Au moins une</strong> des deux conditions doit être vraie|<strong>At least one</strong> condtion must be true}}.
# {{Il est appelé le <em>ou logique</em>|It's called the <em>logical or</em>}}.
# Voici une représentation en diagramme d'un exemple de <code>"or"</code> :
# <figure><img height=400  src="or_as_diagram.{{fr|en}}.svg"/></figure>

# [Essayez]({{http://pythontutor.com/visualize.html#code=if%20a%20%3E%205%20or%20a%20%3D%3D%202%3A%0A%20%20%20%20print%28%22Waw%20!%22%29%0A%0Atruc%20%3D%2050%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false|http://pythontutor.com/visualize.html#code=a%20%3D%201%0Ab%20%3D%202%0A%0Aif%20a%20%3E%205%20or%20a%20%3D%3D%202%3A%0A%20%20%20%20print%28%22Wow!%22%29%0A%0Athing%20%3D%2050%0A&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false}})
# de changer les valeurs de a et b pour vérifier que les flèches corespondent bien au code.

# {{Attention, si tu mélanges des <code>and</code> et des <code>or</code>,|Beware, if you mix <code>and</code> and <code>or</code>,}}
# {{utilise des parenthèses pour bien préciser l'ordre des opérations |use parenthesis to be clear on the order you want to use}}:

if a == 2 or b == 2 and c == 2:  # {{qui du "or" ou du "and" a la priorité ?|Who has the greater priority? The "and" or the "or"?}}
    print("Yo")

# {{cette ligne est équivalente à la précédente : or est "comme" un +, and est "comme" un *|this line is equivalent to the previous one: or is "like" a +, and is "like" a *}}
if a == 2 or (b == 2 and c == 2):
    print("Yo")
    
if (a == 2 or b == 2) and c == 2:
    print("Yo")
    
##{{###################|############}}##
# {{Pour en savoir plus|To know more}} 
##{{###################|############}}##

## =

# {{des raccourcis pour incrémenter/décrémenter !|some shortcuts for increment/decrement}}

a = a + 1
a += 1  # {{raccourci pour|shortcut for}} a = a + 1
a -= 1  # {{raccourci pour|shortcut for}} a = a - 1
a *= 2  # a = a * 2
# etc.

# floats ({{nombre à virgule, notez que "entier" se dit "integer" en anglais, souvent abbrégé en "int"|floating/decimal numbers}})
a = 2.5
a = 2.5e6  # {{la notation "e" crée toujours un float, ici 2.5 * 10^6 = 2.5 millions|the "e" notation}}
a = 2e6   # 2000000.0, {{un float|a float}}

# {{exposant|power}}
a = 2 ** 5       # 2 {{exposant|power}} 5 = 32, int ** int = int
a = 2.1 ** 2     # float ** int = float
a = 10 ** 0.5    # number ** float = float
a = 2 * 10 ** 6  # 2000000, {{un|a}} int, {{remarquez que l'exposant a priorité sur le|let's notice that power has priority on}} "*"

# {{si on divise 14 par 4 on a 3.5|when 14 is divided by 4, one obtains 3.5}}
a = 14 / 4         # 3.5 ({{attention ! En python 2|beware! In python 2}}, 14 / 4 = 3)
a = 14 / 4.0       # 3.5 ({{même en python 2|even in python 2}})
a = 14 / float(4)  # 3.5 ({{float(4) fait la conversion int → float|float(4) do the conversion int → float}})

# l'opérateur de division entière "//" et l'opérateur de "reste" % (aussi appelé "modulo")

# {{si on divise 14 par 4 on a 3 avec un reste de 2 (comme à l'école primaire !) et donc sait que 14 = 3 * 4 + 2.|when 14 is divided by 4, one obtains 3 with a rest of 2 (remember primary school!) therefore we know that 14 = 3 * 4 + 2.}}
d = 14 // 4  # 3, {{la partie entière|the integer part}}
m = 14 % 4   # 2, {{le reste|the rest}} ({{on dira|we'll say}} "14 modulo 4 = 2")

# {{modulo négatifs (python is cool !), observez le cycle 0 1 2 3 4 :|(negative modulos (python is cool !), observe the cycle 0 1 2 3 4:}}
n = -2 % 5  # 3 car -2 = -1 * 5 + 3
n = -1 % 5  # 4 car -1 = -1 * 5 + 4
n =  0 % 5  # 0
n =  1 % 5  # 1
n =  2 % 5  # 2
n =  3 % 5  # 3
n =  4 % 5  # 4
n =  5 % 5  # 0
n =  6 % 5  # 1

## {{plusieurs lignes|multiple lines}}

# {{si on ouvre une parenthèse, on peut passer à la ligne autant que l'on veut|if one opens a parenthesis, one can go to the next line until the parenthesis is closed}}
x = (5 + 2 * 3
       + 7 * 2
       + 1
       - 2)

## {{écrire en binaire ou hexadécimal|write in binary or hexadecimal}}

print(0b100)     # 4
print(0xa2)      # 162
print(hex(162))  # 0xa2
print(bin(4))    # 0b100
print(int('100', 2))  # 4
print(int('a2', 16))  # 162

## {{comparaisons multiple|multiple comparisons}}

if 2 <= a <= 5:  # 2 <= a and a <= 5
    print("{{a est entre 2 et 5|a is between 2 and 5}}")

if a == b == 0:  # a == b and b == 0
    print("{{a et b valent 0|a and b are equal to 0}}")

## not: "inverser" une condition

if a == 5:  # si a == 5...
    pass  # ne rien faire
else:
    print("a n'est pas égal à 5")

# équivalent à

if not(a == 5):
    print("a n'est pas égal à 5")
else:
    pass  # ne rien faire

# équivalent à 

if not(a == 5):
    print("a n'est pas égal à 5")
# "sinon ne rien faire" est une opération inutile, on peut donc l'enlever

# équivalent à 
if a != 5:
    print("a n'est pas égal à 5")
    
# En effet, au choix du programmeur, le not peut être simplifié : <ul>
# <li> <code>not(a == b)  ↔ a != b</code>
# <li> <code>not(a < b)   ↔ a >= b</code> (ATTENTION : plus grand ou ÉGAL)
# <li> <code>not(X and Y) ↔ (not X) or (not Y)</code> (ATTENTION : OR)
# <li> <code>not(X or Y)  ↔ (not X) and (not Y)</code> </ul>
# Les deux dernières lois sont souvent appelées <em>lois de De Morgan</em>.

if not(a == 5 and b < 7):
    print("not(a == 5 and b < 7)")
    
if a != 5 or b >= 7:  # équivalent au précédent
    print("a != 5 or b >= 7")
    
# En règle générale, quand on a un if / else quelconque
# on peut, au choix, inverser la condition en mettant un <code>not</code>.
# Je conseille de faire ça quand vous avez un long <code>if</code> et un court <code>else</code> :

if a != 5 and a > 0:
    print("yoyo")
    print("tada")
    print("truc")
    
    if a == 4:
        print("da")
    else:
        print("yo")
        
else:  # ce "else" est court et oublié :(
    print("coucou")

# on peut (au choix) l'inverser en "not(X)" sa condition :
if not(a != 5 and a > 0):  # appliquez les lois de De Morgan si vous voulez
    print("coucou")  # aaah, l'ancien else est mis en avant :) 
else:
    print("yoyo")
    print("tada")
    print("truc")
    if a == 4:
        print("da")
    else:
        print("yo")

## elif
#
# Parfois, on a un <code>else</code> qui ne contient qu'une seule instruction, qui est un <code>if</code> :

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

#
# Il existe un raccourci : <code>elif</code> (else if) :

if a < 5:  # si a < 5
    print("petit")
elif a < 10:  # sinon... si a < 10
    print("moyen")
elif a < 15:
    print("grand")
else:
    print("graaaand")

## bool
# Les conditions peuvent être mises dans des variables,
# cette variable sera de type "bool" (booléen), il vaut Vrai ou Faux (True or False)

condition = (a < 5)
if condition == True:
    print("Plus petit !")
else:
    print("Plus grand ou égal")

#
# Le <code>if</code> attend un bool, on peut donc enlever <code>== True</code>.

condition = a < 5  # parenthèse non nécessaires
if condition:  # == True enlevé
    print("Plus petit")
else:
    print("Plus grand ou égal")

# on peut donc faire des "opérations" sur les bool

x = True
y = False
z = x or y  # z = True or False = True
n = not x  # n = not True = False
g = a < 5 and z

#
# Nous verrons que manipuler des bool sera plus pratique quand nous apprendront les <em>fonctions</em>.

## if fonctionnel
#
# Parfois, on a un <code>if/else</code> qui ne fait qu'assigner une variable, et rien d'autre !

if a == 5:
    b = 8
else:
    b = 3

# Il existe un raccourci: le <code>if/else</code> dit <em>en une ligne</em>,
# ou encore appelé, le <em>if fonctionnel</em> ou <em>l'opérateur ternaire</em> :
b = (8 if a == 5 else 3)  # même code qu'au dessus

b = 8 if a == 5 else 3  # parenthèses non nécessaires

b = (8 if a == 5 else
     3)  # deux lignes c'est plus clair !

c = (8 if a == 5 else
     4 if a == 2 else
     1 if a < 0 else
     0)  # longue chaine !
