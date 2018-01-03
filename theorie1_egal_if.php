<?php
////////////////////
// Base UNE : "=" //
////////////////////

// "=" permet de changer la valeur d'une variable
// echo (ou print) permet de voir à l'écran la valeur d'une variable
// les variables commencent toujours par un "$"
// chaque instruction finit toujours par un ";"

$a = 5;
echo $a;
$a = 6;
echo $a;
// on peut faire des maths
$b = $a + 1; 
$c = $a + $b * 2; // priorité des opérations
$d = ($a + $b) * 2; // parenthèses si nécessaire !
$a = $a + 1; // a est augmenté de 1
echo $a;
echo $b;
echo $c;
echo $d;

// pour afficher du texte, il faut le mettre entre guillemets
echo "fin";
print "fin"; // print est un alias pour echo

/*
    Ceci est un commentaire sur
    plusieurs lignes
*/

//////////////////////
// Base DEUX : "if" //
//////////////////////

$a = 7;

if($a < 10) {
    print "Coucou";
    print "Hello";
}
    
// ici le programme va afficher "Coucou", puis "Hello" seulement si a est plus petit que 10
// sinon, il saute le bloc et donc, ne fait rien 
// un bloc est marqué par des accolades : {}

// un autre exemple, on veut donner 50 points de vie à un personnage, sans dépasser 100...
$vie = 75;
$vie = $vie + 50;
if($vie > 100) {
    $vie = 100;
}

// pour afficher plusieurs choses on écrit un point
print "Votre vie est ".$vie;

// on peut faire un else, le code ira dans le else si la condition est fausse
if($vie == 100) {
    print "You are full !";
} else {
    print "You can drink potions.";
}

$a = 8;
$b = 2;
// les opérateurs de comparaison sont "<", ">", "<=", ">=", "==", "!=" (différent)
// attention, pour comparer deux valeurs il faut utiliser "=="
// par exemple, ce programme ci

if($a == 5) {
    print "Yo";
} else {
    print "Da";
}

// affiche "Yo" si a est égal à 5 et "Da" sinon
// essaie de réécrire ce code en utilisant l'opérateur "!=" (différent)

// Dans un if, on peut mettre n'importe quel code
// Comme un "=", un print, ou... un autre if !

if($a == 5) {
    $a = 2;
    print "Yo";
    if($b == 5) {
        print "Hello";
    } else {
        print "Tada";
    }
} else {
    print "Hum";
}
   
print $a;
    
// Essaie ce programme avec a=5 b=5, a=5 b=2, a=2 b=2 et voit ce qu'il se passe

// Fais maintenant l'exercice 0 (trier_deux_nombres)

// Ensuite tu peux faire les exercices 1 à 4 sans lire la suite
// Cependant la suite PEUT être utile pour les exercices suivants

// On peut écrire des conditions combinées avec && (and) et || (or)
// par exemple

if($a == 1 && $b == 2) {
    print "Yo";
} else {
    print "Da";
}

// est un programme qui affiche "Yo" si a est égal à 1 et b est égal à 2, sinon Da
// les Deux conditions doivent être vraies
// Celui ci

if($a == 1 || $b == 2) {
    print "Yo";
} else {
    print "Da";
}

// affiche Yo si a est égal à 1 ou b est égal à 2
// ou moins une des deux conditions doit être vraie

// attention, si tu mélanges des and et des or,
// utilise des parenthèses pour bien préciser l'ordre des opérations

if($a == 2 || $b == 2 && $c == 2) { // qui du "||" ou du "&&" a la priorité ?
    print "Yo";
}

// équivalent au précédent : || est "comme" un +, && est "comme" un *
if($a == 2 || ($b == 2 && $c == 2)) {
    print "Yo";
}
    
if(($a == 2 || $b == 2) && $c == 2) {
    print "Yo";
}
    
////////////////////////
// Pour en savoir plus //
////////////////////////

// =

// des raccourcis pour incrémenter/décrémenter !

$a = $a + 5;
$a += 5; // raccourci pour $a = $a + 5
$a++;    // raccourci pour $a = $a + 1
$a -= 5; // raccourci pour $a = $a - 5
$a--;    // raccourci pour $a = $a - 1
$a *= 2; // a = a * 2
// etc.

// floats
$a = 2.5;

// division et modulo %
// si on divise 14 par 4 on a 3 avec un reste de 2

$a = 14 / 4; // 3
$a = 14 / 4.0; // 3.5
$a = 14 / floatval(4); // 3.5
$mod = 14 % 4; // 2, le reste

// plusieurs lignes

// les instructions finissent par ";", on peut donc facilement passer à la ligne 
$a = (5 + 2 * 3
        + 7 * 2
        + 1 - 2);

// !(not) "inverser" une condition

if($a == 5) { // si a == 5...
    // ne rien faire
} else {
    print("a n'est pas égal à 5");
}

// équivalent à

if(!($a == 5)) {
    print("a n'est pas égal à 5");
}

// au choix du programmeur, le not peut être simplifié
// !(a == b) ↔ a != b
// !(a < b)  ↔ a >= b (ATTENTION : plus grand ou ÉGAL)
// !(X && Y) ↔ (!X) || (!Y) (ATTENTION : ||)
// !(X || Y) ↔ (!X) && (!Y)

if(!($a == 5 && $b < 7)) {
    print("not(a == 5 and b < 7)");
}
    
if($a != 5 || $b >= 7) { // équivalent au précédent
    print("a != 5 or b >= 7");
}

// else if : parfois, on a un "else" qui ne contient qu'une seule instruction, qui est un "if"

if($a < 5) {
    print "petit";
} else {
    if($a < 10) {
        print "moyen";
    } else {
        if($a < 15) {
            print "grand";
        } else {
            print "graaaand";
        }
    }
}

// raccourci : else if

if($a < 5) { // si $a < 5
    print "petit";
} else if($a < 10) { // sinon... si $a < 10
    print "moyen";
} else if($a < 15) {
    print "grand";
} else {
    print "graaaand";
}
    
// enlever des accolades
// si un if ou un else a UNE instruction (UN ";"), on peut enlever les accolades

if($a == 5) {
    print "a";
} else {
    print "b";
}

// équivalent au précédent

if($a == 5)
    print "a";
else
    print "b";
    
// cependant, en tant que débutant, il est conseillé de Toujours mettre les accolades

// bool: les conditions peuvent être mises dans des variables
// un (booléen) vaut Vrai ou Faux (true / false)

$condition = ($a < 5);
if($condition == true) {
    print "Plus petit !";
} else {
    print "Plus grand ou egal";
}
    
// le "if" attend un bool, on peut donc enlever "== true"

$condition = $a < 5; // parenthèses non nécessaires
if($condition) { // == true enlevé
    print "Plus petit";
} else {
    print "Plus grand ou egal";
}

// on peut donc faire des "opérations" sur les bool

$x = true;
$y = false;
$z = $x || $y; // $z = true || false = true
$n = !$x; // $n = !true = false
$g = $a < 5 && $z;

// if fonctionnel : parfois, on a un "if/else" qui ne fait qu'assigner une variable (et rien d'autre !)

if($a == 5) {
    $b = 8;
} else {
    $b = 3;
}

// raccourci: le "if/else" "en une ligne"
$b = ($a == 5 ? 8 : 3); // même code qu'au dessus

$b = $a == 5 ? 8 : 3; // parenthèses non nécessaires

$c = $a == 5 ? 8 :
     $a == 2 ? 4 :
     $a < 0 ? 1 : 0; // longue chaine !
?>
