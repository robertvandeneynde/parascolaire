#!coding: utf-8
from __future__ import print_function, division

#####################
# Base CINQ : Objets
### objets ##########

# Un objet permet de grouper plusieurs variables dans un... objet.
# Par exemple on peut grouper la "vie" et le "mana" dans un objet de type "Personnage".

# D'abord on définit la classe de l'objet ci-dessous.
# Pour l'instant elle est vide mais utilisable.
# Une classe va définir le "modèle" d'une série d'objet,
# par exemple tous les personnages seront des... personnages.

class Personnage:
    pass  # vide

# Pour créer un objet on écrit sa classe puis une paire de parenthèses.
# Vu que la classe est vide, il n'y a rien à mettre à l'intérieur de ces parenthèses.

bob = Personnage()
print(bob)  # "objet de la classe Personnage à l'adresse mémoire 0x..."

#
# Vu que bob est un objet, on peut lui mettre des variables !
bob.vie = 60 
bob.max_vie = 100
bob.mana = 10

# On peut créer d'autres personnages,
# comme alice, ou deux personnages sans noms :
alice = Personnage()
alice.vie = 40
alice.max_vie = 70
alice.mana = 50

# imaginez une liste de personnages !
les_personnages = [alice, bob]

alice.vie += 10
print(les_personnages[0].vie)  # 50
print(les_personnage[0] == alice)  # True

p = Personnage()
p.vie = 20
p.max_vie = 20
p.mana = 30

les_personnages.append(p)

p = Personnage()
p.vie = 25
p.max_vie = 25
p.mana = 20

les_personnages.append(p)

# Lancez [cet exemple](http://pythontutor.com/visualize.html#py=3&mode=display&code=class%20Personnage%3A%0A%20%20%20%20pass%20%20%23%20vide%0A%0A%23%20Pour%20cr%C3%A9er%20un%20objet%20on%20%C3%A9crit%20sa%20classe%20puis%20une%20paire%20de%20parenth%C3%A8ses.%0A%23%20Vu%20que%20la%20classe%20est%20vide%2C%20il%20n%27y%20a%20rien%20%C3%A0%20mettre%20%C3%A0%20l%27int%C3%A9rieur%20de%20ces%20parenth%C3%A8ses.%0A%0Abob%20%3D%20Personnage%28%29%0Aprint%28bob%29%20%20%23%20%22objet%20de%20la%20classe%20Personnage%20%C3%A0%20l%27adresse%20m%C3%A9moire%200x...%22%0A%0A%23%0A%23%20Vu%20que%20bob%20est%20un%20objet%2C%20on%20peut%20lui%20mettre%20des%20variables%20%21%0Abob.vie%20%3D%2060%20%0Abob.max_vie%20%3D%20100%0Abob.mana%20%3D%2010%0A%0A%23%20On%20peut%20cr%C3%A9er%20d%27autres%20personnages%2C%0A%23%20comme%20alice%2C%20ou%20deux%20personnages%20sans%20noms%C2%A0%3A%0Aalice%20%3D%20Personnage%28%29%0Aalice.vie%20%3D%2040%0Aalice.max_vie%20%3D%2070%0Aalice.mana%20%3D%2050%0A%0A%23%20imaginez%20une%20liste%20de%20personnages%20%21%0Ales_personnages%20%3D%20%5Balice%2C%20bob%5D%0A%0Aalice.vie%20%2B%3D%2010%0Aprint%28les_personnages%5B0%5D.vie%29%20%20%23%2050%0Aprint%28les_personnage%5B0%5D%20%3D%3D%20alice%29%20%20%23%20True%0A%0Ap%20%3D%20Personnage%28%29%0Ap.vie%20%3D%2020%0Ap.max_vie%20%3D%2020%0Ap.mana%20%3D%2030%0A%0Ales_personnages.append%28p%29%0A%0Ap%20%3D%20Personnage%28%29%0Ap.vie%20%3D%2025%0Ap.max_vie%20%3D%2025%0Ap.mana%20%3D%2020%0A%0Ales_personnages.append%28p%29)
# sur pythontutor, et observez la dynamique des flèches lors du deuxième <code>p = Personnage()</code>.
# Plus d'infos sur ces flèches dans la section <em>En savoir plus</em>.

# Essayez de créer une liste de 100 personnages différents en moins de 10 lignes de code.
# Remarquez qu'un personnage peut être différent d'un autre même s'il a les mêmes stats (vie, mana, ...).

#######################
# Base SIX : Fonctions 
### fonctions #########

# 
# On peut créer des fonctions, comme en math:

def f(x):  # f est une fonction d'un paramètre, appelé x
    return x + 1  # elle renvoie ce paramètre + 1

print(f(5))     # 6, les parenthèses APPELLENT la fonction
y = f(8)        # y = 9
a = 5
b = f(a+1) - 4  # b = (5+1) - 4 = 2
x = 2
z = f(x)        # z = 3
w = f(x+1)      # w = 4

# À quoi ça sert ?
# Certaines structures de code reviennent souvent,
# par exemple dans un exercice précédent, on a calculé le maximum d'une liste:

ma_liste = [1,2,7,2]

m = ma_liste[0]
i = 0
while i < len(ma_liste):
    if ma_liste[i] > m:
        m = ma_liste[i]
    i = i + 1
print(m)

# Ou encore, on aimerait donner <b>20</b> points de vie à un objet <code>Personnage</code>
# sans dépasser son maximum de vie:

bob.vie = bob.vie + 20
if bob.vie > bob.max_vie:
    bob.vie = bob.max_vie

# Cependant, on aimerait bien mettre ça dans une <em>boite</em>,
# une <em>boite à calculer le maximum d'une liste</em>,
# une <em>boite qui donne 20 points de vie sans dépasser le maximum</em>
# et pouvoir la réutiliser autant de fois que l'on veut.

#
# Nous allons donc faire une <strong>FONCTION</strong>:

def calculer_maximum(la_liste):
    m = la_liste[0]
    i = 0
    while i < len(la_liste):
        if la_liste[i] > m:
            m = la_liste[i]
        i = i + 1
    return m

#
# On a fait une fonction, avec un seul paramètre (la liste), et une valeur de retour (le maximum).

#
# Nous pouvons maintenant l'appeler:

une_belle_liste = [1,2,7,2]
a = calculer_maximum(une_belle_liste)

une_autre_liste = [8,0,1,6]
b = calculer_maximum(une_autre_liste)

# Pour appeler une fonction on...<ul>
# <li>écrit son nom,
# <li>ouvre la parenthèse,
# <li>met les paramètres séparés par des virgules,
# <li>ferme la parenthèse</ul>

# remarquez que la valeur de retour peut être stockée dans une variable...
b = calculer_maximum(une_autre_liste)

# ou utilisée dans une expression
c = calculer_maximum(une_belle_liste) + calculer_maximum(une_autre_liste)

# Lancez [cet exemple](http://pythontutor.com/visualize.html#code=def%20calculer_maximum%28la_liste%29%3A%0A%20%20%20%20%22%22%22%0A%20%20%20%20Calcule%20le%20maximum%20d'une%20liste%0A%20%20%20%20%0A%20%20%20%201%20Param%C3%A8tre%20d'entr%C3%A9e%20%3A%0A%20%20%20%20%20%20%20%20-%20la_liste%20%3A%20la%20liste%0A%20%20%20%201%20Param%C3%A8tre%20de%20retour%20%3A%0A%20%20%20%20%20%20%20%20-%20le%20maximum%0A%20%20%20%20%22%22%22%0A%20%20%20%20m%20%3D%20la_liste%5B0%5D%0A%20%20%20%20i%20%3D%200%0A%20%20%20%20while%20i%20%3C%20len%28la_liste%29%3A%0A%20%20%20%20%20%20%20%20if%20la_liste%5Bi%5D%20%3E%20m%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20m%20%3D%20la_liste%5Bi%5D%0A%20%20%20%20%20%20%20%20i%20%3D%20i%20%2B%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20return%20m%0A%20%20%20%20%0Aune_belle_liste%20%3D%20%5B1,2,7,2%5D%0Aune_autre_liste%20%3D%20%5B8,0,1,6%5D%0A%0A%23%20on%20appelle%20la%20fonction%20via%20les%20parenth%C3%A8ses%0Aa%20%3D%20calculer_maximum%28une_belle_liste%29%0A%0A%23%20la%20valeur%20de%20retour%20peut%20%C3%AAtre%20stock%C3%A9e%20dans%20une%20variable...%0Ab%20%3D%20calculer_maximum%28une_autre_liste%29%0A%0A%23%20ou%20utilis%C3%A9e%20dans%20une%20expression%0Ac%20%3D%20calculer_maximum%28une_belle_liste%29%20%2B%20calculer_maximum%28une_autre_liste%29&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# dans pythontutor !

# Les objets et fonctions vont bien ensemble,
# quand une fonction a accès à un objet elle peut modifier ses attributs:

def donner_potion(perso, montant):
    """Donne "montant" pv à un Personnage "perso" sans dépasser son maximum de vie"""
    perso.vie = perso.vie + montant
    if perso.vie > perso.max_vie:
        perso.vie = perso.max_vie
        
# on appelle la fonction avec nos personnages de la base CINQ
donner_potion(bob, 25)  # 25 points de vie pour bob
donner_potion(alice, 100)  # 100 points de vie pour alice

# Vous pouvez aussi voir [cet exemple](http://pythontutor.com/visualize.html#code=class%20Personnage%3A%0A%20%20%20%20pass%20%20%23%20vide%0A%0Abob%20%3D%20Personnage%28%29%0Abob.vie%20%3D%2060%20%0Abob.max_vie%20%3D%20100%0Abob.mana%20%3D%2010%0A%0Aalice%20%3D%20Personnage%28%29%0Aalice.vie%20%3D%2040%0Aalice.max_vie%20%3D%2070%0Aalice.mana%20%3D%2050%0A%0Adef%20donner_potion%28perso,%20montant%29%3A%0A%20%20%20%20%22%22%22Donne%20%22montant%22%20pv%20%C3%A0%20un%20perso%20%22perso%22%20sans%20d%C3%A9passer%20son%20maximum%20de%20vie%20%22%22%22%0A%20%20%20%20perso.vie%20%3D%20perso.vie%20%2B%20montant%0A%20%20%20%20if%20perso.vie%20%3E%20perso.max_vie%3A%0A%20%20%20%20%20%20%20%20perso.vie%20%3D%20perso.max_vie%0A%20%20%20%20%20%20%20%20%0A%23%20on%20appelle%20la%20fonction%20avec%20nos%20personnages%20de%20la%20base%20CINQ%0Adonner_potion%28bob,%2025%29%20%20%23%2025%20points%20de%20vie%20pour%20bob%0Adonner_potion%28alice,%20100%29%20%20%23%20100%20points%20de%20vie%20pour%20alice&cumulative=false&curInstr=0&heapPrimitives=false&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)
# sur pythontutor

# Quand une fonction est appelée, python... <ul>
# <li> crée un bloc dans la mémoire "de gauche"
# <li> copie les paramètres comme si on avait fait "="
# <li> exécute le code de la fonction, qui peut faire tout ce qu'il veut
# <li> supprime le bloc quand on est à la fin</ul>

# Remarquez que la variable <code>i</code> et <code>m</code> sont <em>locales</em> à la fonction,
# elles sont crées dans la fonction et détruites à la fin.

## La boite noire

# <strong>EN UN MOT</strong>: une fonction, c'est une sorte de <em>boite noire</em>:<ol>
# <li>Elle a des paramètres d'entrée... ou pas,
# <li>fait un calcul,
# <li>et sort des valeurs de retour ... ou pas.</ol>

def f(x,y):
    return x + 2 * y

#
# Super dessin de la <em>boite noire</em>: 

# x,y -> [f] -> z

# Les fonctions peuvent avoir:<ul>
# <li>0 ou plus paramètres d'entrées (<em>paramètres</em> ou <em>arguments</em>).
# <li>0 ou plus paramètres de sortie (<em>valeur(s) de retour</em>).</ul>

## Exemples

#
# Voici plusieurs exemples de fonctions:

# 0 paramètre d'entrée, 0 de retour
def afficher_description():
    print("+------------------+")
    print("| Hello !          |")
    print("| Je suis Robert ! |")
    print("+------------------+")
    
afficher_description()

# 1 paramètre d'entrée, 0 de retour
def afficher_etoiles(nombre):
    for i in range(nombre):
        print("*")
        
afficher_etoiles(5)

# 2 paramètres d'entrée, 2 de retour
def minute_suivante(h,m):
    if m < 59:
        nouveau_h = h
        nouveau_m = m + 1
    else:
        nouveau_h = h + 1
        nouveau_m = 0
    return nouveau_h, nouveau_m

a,b = minute_suivante(13,30)
c,d = minute_suivante(12,59)

# pas d'entrée, un retour
def generate():
    liste = []
    for i in range(5):
        liste.append(i * i)
    return liste

l = generate()

## return

# Remarquez qu'on peut mettre autant de <code>return</code> que l'on veut,
# quand python lit un return, il arrête tout de suite la fonction et renvoie (ou non) une valeur.

def manger(x):
    if x < 0: # si x est négatif
        return -1  # la fonction s'arrête et renvoie -1
    
    i = 0
    s = 0
    while i < x:
        s += i
        i = i + 1
    return s

# Le mot clé <code>return</code>
# rappelle que le code <em>retourne</em> dans la fonction appelante.

###
# Pour en savoir plus (fonctions)
### pour-en-savoir-plus-fonctions, pour-en-savoir-plus-(fonctions)

## Paramètres par défaut

def f(x, y=5):
    return x + y

print(f(1))    # x=1, y=5
print(f(1,2))  # x=1, y=2

# Attention, ne mettre comme valeur par défaut que des objets <em>non modifiables</em> (<em>immutable</em> en anglais)
# comme des <code>int</code>, <code>str</code>, <code>tuple</code> mais pas 
# des <code>list</code> ni des objets classiques (la raison est expliquée plus bas).

#
# Un bon défaut est <code>None</code> qui est une valeur spéciale en Python :

def f(x, y=None):
    if y is None:
        y = x + 1
    return x + y

## Appel utilisant les noms des paramètres

def f(x, y):
    return x - y

print(f(5, 2))      # 3    
print(f(5, y=2))    # 3
print(f(x=5, y=2))  # 3
print(f(y=2, x=5))  # 3

## Docstring et interfaces

# Un des grand intérêt des fonctions est de les voir comme une boîte noire.
# Quand quelqu'un voit la première ligne (la <em>signature</em>) de la fonction,
# <code>def calculer_maximum(la_liste)</code>,
# il peut comprendre qu'il peut utiliser cette fonction pour calculer
# le maximum d'une liste <strong>sans en lire son code</strong>.

# Parfois, le nom à lui tout seul n'est pas suffisant pour bien utiliser
# la fonction, on y ajoute alors une <em>docstring</em>
# qui est un petit texte expliquant le <strong>rôle</strong> de la fonction.
# C'est généralement fait via <code>"""</code> et sur plusieurs lignes :

def calculer_maximum(la_liste):
    """
    Calcule le maximum d'une liste
    en utilisant une recherche linéaire.
    """
    m = la_liste[0]
    i = 0
    while i < len(la_liste):
        if la_liste[i] > m:
            m = la_liste[i]
        i = i + 1
    return m

# Une docstring doit donner des informations sur son <strong>rôle</strong>
# et non sur <em>comment</em> elle remplit son rôle.
# Sur <strong>ce</strong> qu'elle fait et non sur <em>comment</em> elle le fait.
# L'idée est de donner uniquement les informations pertinentes à la personne <strong>appelant</strong> la fonction,
# le reste étant des <em>détails d'implémentation</em>.

# Quand on a beaucoup de paramètres d'entrée et de retour dont les noms mérite explications,
# il est souvent utile de les lister dans la docstring :

def effectuer_un_combat(attaquant, defenseur, butin, lieu):
    """
    Effectue un combat entre une équipe attaquante et 
    une équipe en défense et renvoie la durée du combat.
    
    @param attaquant: l'équipe attaquante (de type Equipe)
    @param defenseur: l'équipe attaquante (de type Equipe)
    @param lieu: la position de la bataille (un tuple (latitude, longitude))
    @param butin: le nombre de pièce d'or volées à l'adversaire en cas de victoire (un int)
    
    @returns la durée du combat (un timedelta)
    """
    ...  # le code effectuant le combat!

# Indiquer les types d'arguments étant une tâche très récurrente et utile,
# python 3 introduit les annotations en parallèle de la docstring:

def effectuer_un_combat(attaquant:Equipe, defenseur:Equipe, butin:int, lieu:tuple) -> timedelta:
    """Effectue un combat entre une équipe attaquante et 
    une équipe en défense en une (latitude, longitude) donnée et renvoie la durée du combat."""
    ...  # le code effectuant le combat!

# Dans cet exemple, la docstring a pu être épurée
# les annotations ne doivent pas nécessairement être des types, ce code est possible:

def effectuer_un_combat(attaquant:Equipe, defenseur:Equipe, butin:int, lieu:(float, float)) -> timedelta:
    ...  # le code effectuant le combat!

# En python 3.7, à condition d'écrire
# <code>from __future__ import annotations</code>
# au début du fichier, les variables utilisées commme <code>Equipe</code> ou <code>timedelta</code> ne doivent même pas être déclarées.

## Simplifications automatiques

#
# Voici un aperçu de mon [article](progra_equivalences.html) obtenues grâce aux fonctions.

#
# (1) Les fonctions renvoyant un <code>bool</code> :

# avant
def f():
    ...
    if CONDITION:
        return True
    else:
        return False
    
# après (bool)
def f():
    ...
    return CONDITION

#
# Le return se lira alors <em>si et seulement si</em> (ssi).

#
# Par exemple:

# x est une voyelle ssi x == 'a' or x == 'e' or x == 'i' or x = 'o' or x = 'u'
def voyelle(x):
    return x == 'a' or x == 'e' or x == 'i' or x = 'o' or x = 'u'

# plus d'infos [ici](progra_equivalences.html#boolean-return)
# et [là](progra_equivalences.html#==-True).

#
# (2) Le if fonctionnel

# avant:
def f():
    ...
    if CONDITION:
        return X
    else:
        return Y
    
# après (if fonctionnel)
def f():
    ...
    return X if CONDITION else Y

# Cette transformation n'est pas obligatoire
# c'est juste un autre style de programmation.

# Plus d'infos [ici](progra_equivalences.html#if-variable)
# et [là](progra_equivalences.html#if-elif-cascade-on-variable)

#
# (2) Le return dans un if :

# avant
def f():
    if CONDITION:
        A
        return X
    else:
        B
        return Y
    
# après (return)
def f():
    if CONDITION:
        A
        return X
    B
    return Y

# A et B sont une suite de 0 ou plus instructions,
# je conseille de faire ceci si il y a peut d'instructions dans "A" et beaucoup dans "B".

# Plus d'infos
# [ici](progra_equivalences.html#if-return).

#
# (3) ∃ et ∀ :

# avant
def f():
    ...
    for X in L:
        if CONDITION:
            return True
    return False

# après : (voir fichier [progra_functionals](progra_functionals.py.html))
def f():
    ...
    return any(CONDITION for X in L)

# Lire ça comme <em>il existe un X dans L qui vérifie <b>CONDITION</b></em>
# ou <em>il existe un X dans L tel que <strong>CONDITION</strong></em>.

#
# Par exemple:
if any(x == 2 for x in L):
    ...

# Se lit <em>si</em> : <ul>
# <li> Il existe un <b>2</b> dans <code>L</code>.
# <li> <em>Il existe un x dans L tel que <code>x == 2</code></em>
# <li>∃ x ∈ L: x == 2</ul>

#
# Un conseil: passer à la ligne en fonction de la longueur dans le <code>any</code>!

#
# ∀ est le cas dual de ∃ :

# avant
def f():
    ...
    for X in L:
        if not CONDITION:
            return False
    return True

# après: (voir fichier [progra_functionals](progra_functionals.py.html))
def f():
    ...
    return all(CONDITION for X in L)

# On peut lire ça de plusieurs manières: <ul>
# <li> tous les X de L vérifient <b>CONDITION</b>
# <li> quel que soit X, il vérifie <strong>CONDITION</strong>
# <li> pour tous les éléments de X, il vérifie <strong>CONDITION</strong> </ul>

#
# Par exemple:
if all(x > 0 for x in L):
    ...
    
# Se lit <em>si</em> : <ul>
# <li> Tous les nombres de L sont > 0
# <li> Pour tous les élements x de L, on a x > 0
# <li> ∀ x ∈ L: x > 0 </ul>

# Plus d'infos [ici](progra_equivalences.html#for-if-return-True)
# et [là](progra_equivalences.html#for-if-return-False)

#
# (4+) Plus d'exemples dans mon [article](progra_equivalences.html) sur les équivalences.

## Récursivité

#
# Méditez là dessus avec pythontutor...

def f(x):
    if x > 0:
        f(x-1)
        print("Hello", x)
        f(x-1)

f(4)

## Variables locales

#
# Méditez là dessus sur pythontutor:

g = 5
p = 2
def f(x):
    print(g)
    y = x + 1
    p = 5
    print(p)

# <strong>LECTURE</strong>: Quand on lit une variable (print(x) par exemple), python fait ceci : <ul>
# <li> Regarder si la variable existe dans la Fonction en cours (dans le bloc à gauche, en bas sur pythontutor)
# <li> Si elle existe, il donne la valeur (contenu de la case), sinon :
# <li> Il regarde dans l'espace GLOBAL (global frame dans pythontutor), et s'il ne la trouve pas...
# <li> lance une NameError (variable non trouvée) </ul>

# <strong>ÉCRITURE</strong>: Quand on écrit dans une variable (variable = ), python fait ceci : <ul>
# <li> Regarder si la variable existe dans la Fonction en cours (dans le bloc à gauche, en bas sur pythontutor)
# <li> Si elle existe, il écrit la valeur (modifie le contenu de la case), sinon :
# <li> Il Crée la variable DANS LA FONCTION, on peut donc avoir une variable globale et locale avec le même nom</ul>

# Quand une fonction se termine (<code>return</code> ou arrivée à la fin du bloc),
# les variables sont détruites

# Même si c'est une mauvaise pratique, il est possible de dire qu'on parle d'une variable globale
# cela modifie donc la dynamique lors de l'écriture

g = 5
def f():
    global g
    g = 2

f()
print(g)

# comment éviter de marquer une variable comme "globale" ?
# En <strong>RENVOYANT</strong> quelque chose.

def f():
    return 2

g = f()

#
# Ou en groupant des variables dans des... <strong>OBJETS</strong> !

class Groupy:
    pass

def f(group):
    group.n = 2

group = Group()
group.n = 5

f(group)

print(group.n)

###
# Pour en savoir plus (objets)
### pour-en-savoir-plus-objets, pour-en-savoir-plus-(objets)

## Méthodes

# Rappelons nous de notre fonction qui prend un objet en paramètre
def donner_potion(perso, montant):
    """Donne "montant" pv à un Personnage "perso" sans dépasser son maximum de vie"""
    perso.vie = perso.vie + montant
    if perso.vie > perso.max_vie:
        perso.vie = perso.max_vie
        
# on appelle la fonction avec nos personnages de la base CINQ
donner_potion(bob, 25)  # 25 points de vie pour bob
donner_potion(alice, 100)  # 100 points de vie pour alice

# On peut mettre des fonctions dans les classes,
# on appelle ça des <em>méthodes</em>.

# À la place de le faire dans l'espace global, on le fait dans la classe
# Ces fonctions reçoivent <strong>TOUJOURS</strong> un premier paramètre "self"
# qui représente l'objet manipulé.

# Dans notre fonction <code>donner_potion(perso, montant)</code>
# le <code>self</code>, c'est <code>perso</code>

class Personnage:
    def boire_potion(self, montant):
        """Donne montant pv au Personnage sans dépasser son maximum de vie"""
        self.vie = self.vie + montant
        if self.vie > self.max_vie:
            self.vie = self.max_vie
            
    def crier(self):
        """Affiche un cri de guerre à l'écran"""
        print("Bouh!")

bob = Personnage()
bob.vie = 60 
bob.max_vie = 100
bob.mana = 10

alice = Personnage()
alice.vie = 40
alice.max_vie = 70
alice.mana = 50

bob.boire_potion(25)  # on appelle les méthodes comme ceci :)
alice.boire_potion(100)
alice.crier()

## Contructeur

# On voit des parties du code précédent qui sont répétées.
# Ce serait pratique de faire une fonction qui <em>initialise</em> les attributs.

def init_personnage(perso, a, b, c):
    perso.vie = a
    perso.max_vie = b
    perso.mana = c
    
bob = Personnage()
init_personnage(bob, 60, 100, 10)
alice = Personnage()
init_personnage(alice, 60, 100, 10)

# Cette fonctionnalité existe : Le constructeur.
# C'est une fonction qui est appelée à la création de tout objet.
# Le constructeur d'une classe s'appelle toujours <code>__init__</code>.

class Personnage:
    def __init__(self, a, b, c):
        self.vie = a
        self.max_vie = b
        self.mana = c
        
# On donne les paramètres à la création
bob = Personnage(60, 100, 10)
alice = Personnage(40, 70, 50)

## Héritage

# Méditez là dessus (pythontutor):

class Personnage:
    def __init__(self, vie, max_vie):
        self.vie = vie
        self.max_vie = max_vie
        
    def crier(self):
        """Affiche un cri de guerre à l'écran"""
        print("Bouh!")
        
    def boire_potion(self, x):
        self.vie = min(self.vie + x, self.max_vie)

class Guerrier(Personnage):  # un Guerrier est un Personnage
    def crier(self):  # mais qui fait "crier()" différemment
        print("Arrrrrrrrgggg")
    
class Magicien(Personnage):
    def crier(self):
        print("Wololo")

alice = Magicien(50, 100)
bob = Guerrier(75, 125)
guy = Personnage(20, 80)
personnages = [alice, bob, guy]  # différentes classes, mais tous des Personnages
for perso in personnages:
    perso.crier()                # va appeler une version différente en fonction de la classe
    perso.boire_potion(10)       # la fonction boire_potion existe toujours

#
# Pour réutiliser une fonction de la classe héritée, on fait comme ceci :

class Chou(Personnage):
    def crier(self):
        Personnage.crier(self)  # on appelle la version de "crier" qui se trouve dans "Personnage"
        print("Wouloulou")
      
class Marchand(Personnage):
    def __init__(self):  # on crée un Marchand sans paramètre
        Personnage.__init__(self, 50, 100)  # on appelle la version de __init__ dans Personnage
        self.argent = 10  # une nouvelle variable
    
    def crier(self):
        if self.argent > 0:
            print("Je suis un Marchand riche !")
        else:
            print("Je suis un Marchand fauché...")
        
denis = Chou(20, 40)
denis.crier()  # Affiche "Bouh!", puis "Wouloulou"

marc = Marchand()   # pas de paramètres vu que Marchand.__init__ n'a pas de paramètres
print(marc.vie)     # 50
print(marc.argent)  # 10
marc.crier()

# Comment ça se passe ?
# Python regarde si la classe de l'objet a la fonction appelée,
# si elle l'a, il l'appele,
# sinon, il regarde dans sa classe parente, et puis la parente de la parente.
# Et finalement si aucune des classes parentes n'a la fonction, il lance une exception.

#
# On peut savoir si un objet est d'une classe
print(isinstance(alice, Magicien))  # True
print(isinstance(bob, Magicien))    # False
print(isinstance(guy, Magicien))    # False
print(isinstance(guy, int))         # False

print(isinstance(alice, Personnage))  # True car héritage

# ou donner plusieurs classes pour éviter de faire un "or"
print(isinstance(alice, Magicien) or isinstance(alice, Guerrier))  # long
print(isinstance(alice, (Magicien, Guerrier)))  # raccourci

# bien que peu utile en pratique, on peut accéder à la classe d'un objet
cls = alice.__class__
print(cls == Magicien)    # True
print(cls == Personnage)  # False
print(type(alice) == alice.__class__)  # True 

# Veuillez toujours utiliser <code>isinstance</code> quand vous voulez tester l'appartenance,
# si votre code fait quelque chose pour un <code>Personnage</code>, ça devrait également
# marcher avec un <code>Magicien</code> ou un <code>Guerrier</code>.

## Références 

# Méditez là dessus avec pythontutor:

a = 5
b = a
a = 6
print(a)
print(b)

a = [1,2,3]
b = a
a[0] = 2
print(a)
print(b)

class Personnage:
    pass

a = Personnage()
b = a
a.vie = 1
print(a.vie)
print(b.vie)

# Plot twist : les listes sont des objets, de la classe <code>list</code>.
# Quand on crée un objet (et donc une liste),
# on reçoit une "référence" (symbolisée par une "flèche").

# Contrairement aux objets, les int, float, string n'ont pas de flèche,
# leur valeur est écrite directement dans la case.

# Les objets et références sont dans deux zones de la mémoire différentes,
# symbolisées par deux colonnes dans pythontutor.

# Quand on <strong>COPIE</strong> une variable, on copie la <strong>CASE</strong>,
# donc quand on copie un int, on copie le nombre.

# Quand on copie une "flèche", on fait une nouvelle flèche avec la même cible
# une <strong>COPIE</strong> se passe uniquement avec <code>x =</code>, <code>for x in</code> ou un appel de fonction :)

#
# Ainsi, dans le code précédent, on a plusieurs exemples de copie avec =

def modifier_premier(liste):
    liste[0] = 0

ma_liste = [1,2,3]
modifier_premier(ma_liste)

def modifier_local(x):
    x = 2

p = 2
modifier_local(p)
    
