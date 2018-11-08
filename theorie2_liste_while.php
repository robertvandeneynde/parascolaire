<?php

////////////////////////
// Base TROIS : while //
////////////////////////

// les while sont comme des if, sauf qu'après avoir exécuté leur code, ils recommencent

$a = 5;

if($a < 10) {
    print "Tada";
}
    
while($a < 10) {
    print "Hello";
}
    
// ce programme va afficher "Hello" sans s'arrêter...
// pour éviter de faire une "boucle infinie", il faudrait que la condition devienne fausse
// par exemple comme ceci

$i = 0;
while($i < 10) {
    print "Hello";
    $i = $i + 1;
}
// maintenant, Hello n'est affiché que dix fois ^^

// on peut bien sûr utiliser nos variables

$i = 0;
while($i < 10) {
    print "Hello". 2 * $i + 5;
    $i = $i + 1;
}

// affichera "Hello 5", "Hello 7", "Hello 9" etc.

/////////////////////////
// Base QUATRE : array //
/////////////////////////

// on peut créer des array (tableaux, listes)
$ma_liste = array(3,4,7,4); // 4 éléments !

// 1) Lire
$premier = $ma_liste[0] // l'élément numéro 0 est le premier
$dernier = $ma_liste[3] // vu que notre liste est de taille 4, 3 est le dernier
$taille = count($ma_liste) // count permet de savoir la taille (raccourci : sizeof)
print $ma_liste[5] // il n'y a pas d'élément "5", cela ne va rien afficher

// le "numéro" est appelé "l'indice", l'indice du "1" dans notre liste est donc 0

// 2) Écrire
$ma_liste[0] = 9; // hop ! le tableau vaut [9,2,7,2]
$ma_liste[5] = 2; // on oblige l'écriture à 5, le tableau vaut [9,2,7,2,?,2]
// le "?" est une valeur spéciale en php qui représente "rien",
// on devrait éviter d'en créer
$ma_liste[4] = 9; // on remplace le "?" par un 9
$ma_liste = array(9,2,7,2); // retour à la liste de départ

// Astuce : Ajouter à la fin
$ma_liste[] = 0 // hop ! la liste vaut [9,2,7,2,0]
// on aurait pu faire ceci en faisant ma_liste[4] = 0 mais on aurait dû se souvenir de la taille

// Les boucles et les listes vont bien ensemble,
// on peut par exemple afficher tous les éléments d'une liste avec un while

$i = 0;
while($i < count($ma_liste)) {
    print $ma_liste[$i];
    $i = $i + 1;
}

// Tu as toutes les bases pour faire tous les exercices
// Je conseille de faire au moins le 5 (max list) et puis de passer à pygame pour créer des fenêtres !

//////////////////////////
// Pour en savoir plus... //
//////////////////////////

//// while ////
// certaines structures "while" sont très utilisées, et peuvent être remplacées par des "for"

// compter !
for($i = 0; $i < 5; $i++) {
    print $i;
}
    
// ce code peut s'écrire comme ceci avec un while :
$i = 0
while($i < 5) {
    print $i;
    $i = $i + 1;
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

// parcourir une liste ! foreach

foreach($ma_liste as $nombre) {
    print $nombre;
}
    
// ce qui peut s'écrire comme ceci avec un while 

$i = 0;
while($i < count($ma_liste)){
    $nombre = $ma_liste[$i];
    print $nombre;
    $i = $i + 1;
}

//// list ////

// TODO: String

?>