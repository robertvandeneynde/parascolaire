////////////////////////
// Base TROIS : while //
////////////////////////

// les while sont comme des if, sauf qu'après avoir exécuté leur code, ils recommencent

a = 5

if(a < 10) {
    console.log("Tada")
}
    
while(a < 10) {
    console.log("Hello")
}
    
// ce programme va afficher "Hello" sans s'arrêter...
// pour éviter de faire une "boucle infinie", il faudrait que la condition devienne fausse
// par exemple comme ceci

i = 0
while(i < 10) {
    console.log("Hello")
    i = i + 1
}
    
// maintenant, Hello n'est affiché que dix fois ^^

// on peut bien sûr utiliser nos variables

i = 0
while(i < 10) {
    console.log("Hello", 2 * i + 5)
    i = i + 1
}

// affichera "Hello 5", "Hello 7", "Hello 9" etc.

///////////////////////////
// Base QUATRE : listes  //
///////////////////////////

// on peut créer des listes, avec des crochets
ma_liste = [1,2,7,2] // 4 éléments !
// 4 opérations de base sont possibles sur les listes

// 1) Lire
premier = ma_liste[0] // l'élément numéro 0 est le premier
dernier = ma_liste[3] // vu que notre liste est de taille 4, 3 est le dernier
taille = ma_liste.length // .length permet de savoir la taille
console.log(ma_liste[5]) // il n'y a pas d'élément "5", il vaut undefined 

// le "numéro" est appelé "l'indice", l'indice du "1" dans notre liste est donc 0

// 2) Écrire
ma_liste[0] = 9 // hop ! la liste vaut [9,2,7,2]
ma_liste[5] = 2 // on oblige l'écriture à 5, le tableau vaut [9,2,7,2,undefined,2]
// le undefined est une valeur spéciale en php qui représente "rien"
// on devrait éviter d'en créer
ma_liste[4] = 9 // on remplace le "?" par un 9
ma_liste = [9,2,7,2] // retour à la liste de départ

// 3) Ajouter à la fin
ma_liste.push(0) // hop ! la liste vaut [9,2,7,2,0]

// 4) Supprimer
ma_liste.splice(1, 1) // l'élément numéro "1" est supprimé, la liste vaut donc [9,7,2,0]
// le deuxième "1" indique le nombre d'élément à supprimer

// Les boucles et les listes vont bien ensemble,
// on peut par exemple afficher tous les éléments d'une liste avec un while

i = 0
while(i < ma_liste.length) {
    console.log(ma_liste[i])
    i = i + 1
}

// Tu as toutes les bases pour faire tous les exercices
// Je conseille de faire au moins le 5 (max list) et puis de passer à pygame pour créer des fenêtres !

////////////////////////////
// Pour en savoir plus... //
////////////////////////////

//// while ////
// certaines structures "while" sont très utilisées, et peuvent être remplacées par des "for"

// compter !
for(i = 0; i < 5; i++) {
    console.log(i)
}
    
// ce code peut s'écrire comme ceci avec un while :
i = 0
while(i < 5) {
    console.log(i)
    i = i + 1
}

// plus généralement, le for est un raccourci pour une structure comme celle ci :
/*
A
while(B) {
    C
    D
}
=>
for(A; B; D) {
    C
}
*/
// Quand on lit un code :
// - on "rentre" dans le for par la gauche (on fait A)
// - on fait la condition (B)
// - si elle est vraie : on fait l'intérieur (C)
// - Quand on arrive à l'accolade fermante, on fait "D"
// - et on recommence à la condition (B)
// pour les débutants, le while est plus facile à suivre.

// les str (string / chaînes de caractères)
// les chaînes de caractère ont un point commun avec les listes :
// elles ont plusieurs éléments (des caractères)
prenom = "Robert"
prenom = 'Robert' // même chose

// on ne peut que les lire
lettre = prenom[0] // 'R'
taille = prenom.length // 6
console.log(lettre.length) // 1

// on peut faire de drôles de math avec !
nom_de_famille = "Vanden Eynde"
long_nom = prenom + " " + nom_de_famille // "Robert Vanden Eynde"
phrase = long_nom + " a " + 24 + " ans."

// comparer, via l'alphabet
if prenom < 'Frederic':
    console.log("Avant Frederic")
else:
    console.log("Après ou est Frederic")

// Attention, majuscules, minuscules
console.log('A' == 'a') // false
console.log('a' < 'B') // false
petit_robert = prenom.toLowerCase() // "robert"
grand_robert = prenom.toUpperCase() // "ROBERT"

// str et liste de str
liste = ['A', 'B', 'C']
chaine = liste.join('') // "ABC"
chaine_v = liste.join(', ') // "A, B, C"

// str et conversions
texte = "" + 52 // "52"
nombre = parseInt("23") // 23
virgule = parseFloat("41.25") // 41.25
some_names = "Hello World;Bonjour le monde;Donkey Konga".split(';') // ['Hello World', 'Bonjour le monde', 'Donkey Konga']
no_space = " \t  Yeyo Yayo \n ".trim() // "Yeyo Yayo"

// slicing
console.log(prenom.slice(1,4)) // de 1 à 4 non compris : "obe"
console.log(prenom.substr(1,3)) // de 1, prend 3 : "obe"
console.log(prenom.slice(4)) // de 4 à la fin : "rt"