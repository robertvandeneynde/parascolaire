public class theorie1_egal_if {
  public static void main(String[] args) {
    ////////////////////
    // Base UNE : "=" //
    ////////////////////
    
    // pour créer une variable, il faut indiquer son TYPE et puis son NOM 
    int a; // int : entier
    // "=" permet de changer la valeur d'une variable
    // System.out.println permet de voir à l'écran la valeur d'une variable
    // chaque instruction finit toujours par un ";"

    a = 5;
    System.out.println(a);
    a = 6;
    System.out.println(a);
    int h = 9; // créer une variable et lui donner directement une valeur
    
    // on peut faire des maths
    int b = a + 1; 
    int c = a + b * 2; // priorité des opérations
    int d = (a + b) * 2; // parenthèses si nécessaire !
    a = a + 1; // a est augmenté de 1
    System.out.println(a);
    System.out.println(b);
    System.out.println(c);
    System.out.println(d);

    // pour afficher du texte, il faut le mettre entre guillemets
    System.out.println("fin");
    
    // conseil pour les utilisateurs d'ECLIPSE,
    // tappez "syso" puis appuyez sur CTRL+ESPACE et System.out.println apparaîtra !
    // CTRL+ESPACE sert aussi à finir le mot d'une longue variable
    int maLongueVariable = 8;
    maLongueVariable = 1; // ici j'ai fait CTRL+ESPACE après avoir tappé "ma"
    // tapper les initiales (mLV) marche aussi

    /*
        Ceci est un commentaire sur
        plusieurs lignes
    */

    //////////////////////
    // Base DEUX : "if" //
    //////////////////////

    a = 7;

    if(a < 10) {
        System.out.println("Coucou");
        System.out.println("Hello");
    }
        
    // ici le programme va afficher "Coucou", puis "Hello" seulement si a est plus petit que 10
    // sinon, il saute le bloc et donc, ne fait rien 
    // un bloc est marqué par des accolades : {}

    // un autre exemple, on veut donner 50 points de vie à un personnage, sans dépasser 100...
    int vie = 75;
    vie = vie + 50;
    if(vie > 100) {
        vie = 100;
    }

    // pour afficher plusieurs choses on écrit "+" et on alterne du texte et des variables 
    System.out.println("Votre vie est " + vie);

    // on peut faire un else, le code ira dans le else si la condition est fausse
    if(vie == 100) {
        System.out.println("You are full !");
    } else {
        System.out.println("You can drink potions.");
    }

    a = 8;
    b = 2;
    // les opérateurs de comparaison sont "<", ">", "<=", ">=", "==", "!=" (différent)
    // attention, pour comparer deux valeurs il faut utiliser "=="
    // par exemple, ce programme ci

    if(a == 5) {
        System.out.println("Yo");
    } else {
        System.out.println("Da");
    }

    // affiche "Yo" si a est égal à 5 et "Da" sinon
    // essaie de réécrire ce code en utilisant l'opérateur "!=" (différent)

    // Dans un if, on peut mettre n'importe quel code
    // Comme un "=", un print, ou... un autre if !

    if(a == 5) {
        a = 2;
        System.out.println("Yo");
        if(b == 5) {
            System.out.println("Hello");
        } else {
            System.out.println("Tada");
        }
    } else {
        System.out.println("Hum");
    }
    
    System.out.println(a);
        
    // Essaie ce programme avec a=5 b=5, a=5 b=2, a=2 b=2 et voit ce qu'il se passe

    // Fais maintenant l'exercice 0 (trier_deux_nombres)
    // regarde la correction sur pythontutor (http://robertvandeneynde.be/parascolaire/pythontutor.html)
    // (après avoir choisi "java")
    
    // Ensuite tu peux faire les exercices 1 à 4 sans lire la suite
    // Cependant la suite PEUT être utile pour les exercices suivants

    // On peut écrire des conditions combinées avec && (and) et || (or), par exemple

    if(a == 1 && b == 2) {
        System.out.println("Yo");
    } else {
        System.out.println("Da");
    }

    // est un programme qui affiche "Yo" si a est égal à 1 et b est égal à 2, sinon Da
    // les Deux conditions doivent être vraies
    // Celui ci

    if(a == 1 || b == 2) {
        System.out.println("Yo");
    } else {
        System.out.println("Da");
    }

    // affiche Yo si a est égal à 1 ou b est égal à 2
    // ou moins une des deux conditions doit être vraie

    // attention, si tu mélanges des and et des or,
    // utilise des parenthèses pour bien préciser l'ordre des opérations

    if(a == 2 || b == 2 && c == 2) { // qui du "||" ou du "&&" a la priorité ?
        System.out.println("Yo");
    }

    // équivalent au précédent : || est "comme" un +, && est "comme" un *
    if(a == 2 || (b == 2 && c == 2)) {
        System.out.println("Yo");
    }
        
    if((a == 2 || b == 2) && c == 2) {
        System.out.println("Yo");
    }
        
    ////////////////////////
    // Pour en savoir plus //
    ////////////////////////

    // =

    // des raccourcis pour incrémenter/décrémenter !

    a = a + 5;
    a += 5; // raccourci pour a = a + 5
    a++;    // raccourci pour a = a + 1
    a -= 5; // raccourci pour a = a - 5
    a--;    // raccourci pour a = a - 1
    a *= 2; // a = a * 2
    // etc.

    // double : nombre à virgule
    double v = 2.5;

    // division et modulo %
    // si on divise 14 par 4 on a 3 avec un reste de 2

    a = 14 / 4; // 3
    v = 14 / 4.0; // 3.5
    v = 14 / (double) 4; // 3.5
    int mod = 14 % 4; // 2, le reste

    // plusieurs lignes

    // les instructions finissent par ";", on peut donc facilement passer à la ligne 
    a = (5 + 2 * 3
           + 7 * 2
           + 1 - 2);

    // !(not) "inverser" une condition

    if(a == 5) { // si a == 5...
        // ne rien faire
    } else {
        System.out.println("a n'est pas égal à 5");
    }

    // équivalent à

    if(!(a == 5)) {
        System.out.println("a n'est pas égal à 5");
    }

    // au choix du programmeur, le not peut être simplifié
    // !(a == b) ↔ a != b
    // !(a < b)  ↔ a >= b (ATTENTION : plus grand ou ÉGAL)
    // !(X && Y) ↔ (!X) || (!Y) (ATTENTION : ||)
    // !(X || Y) ↔ (!X) && (!Y)

    if(!(a == 5 && b < 7)) {
        System.out.println("not(a == 5 and b < 7)");
    }
        
    if(a != 5 || b >= 7) { // équivalent au précédent
        System.out.println("a != 5 or b >= 7");
    }

    // else if : parfois, on a un "else" qui ne contient qu'une seule instruction, qui est un "if"

    if(a < 5) {
        System.out.println("petit");
    } else {
        if(a < 10) {
            System.out.println("moyen");
        } else {
            if(a < 15) {
                System.out.println("grand");
            } else {
                System.out.println("graaaand");
            }
        }
    }

    // raccourci : else if

    if(a < 5) { // si a < 5
        System.out.println("petit");
    } else if(a < 10) { // sinon... si a < 10
        System.out.println("moyen");
    } else if(a < 15) {
        System.out.println("grand");
    } else {
        System.out.println("graaaand");
    }
        
    // enlever des accolades
    // si un if ou un else a UNE instruction (UN ";"), on peut enlever les accolades

    if(a == 5) {
        System.out.println("a");
    } else {
        System.out.println("b");
    }

    // équivalent au précédent

    if(a == 5)
        System.out.println("a");
    else
        System.out.println("b");
        
    // cependant, en tant que débutant, il est conseillé de Toujours mettre les accolades

    // boolean: les conditions peuvent être mises dans des variables
    // un (booléen) vaut Vrai ou Faux (true / false)

    boolean condition = (a < 5);
    if(condition == true) {
        System.out.println("Plus petit !");
    } else {
        System.out.println("Plus grand ou egal");
    }
        
    // le "if" attend un bool, on peut donc enlever "== true"

    condition = a < 5; // parenthèses non nécessaires
    if(condition) { // == true enlevé
        System.out.println("Plus petit");
    } else {
        System.out.println("Plus grand ou egal");
    }

    // on peut donc faire des "opérations" sur les bool

    boolean x = true;
    boolean y = false;
    boolean z = x || y; // z = true || false = true
    boolean n = !x; // $n = !true = false
    boolean g = a < 5 && z;

    // if fonctionnel : parfois, on a un "if/else" qui ne fait qu'assigner une variable (et rien d'autre !)

    if(a == 5) {
        b = 8;
    } else {
        b = 3;
    }

    // raccourci: le "if/else" "en une ligne"
    b = (a == 5 ? 8 : 3); // même code qu'au dessus

    b = a == 5 ? 8 : 3; // parenthèses non nécessaires

    c = a == 5 ? 8 :
        a == 2 ? 4 :
        a < 0 ? 1 : 0; // longue chaine !
        
    // localité des variables
    // Quand une variable est Créée, elle n'est accessible que dans son BLOC
    // Un bloc c'est une paire d'accolades
    // nos variables utilisées jusqu'à présent étaient "globales" à la fonction main
    // (regardez les premières lignes, main ouvre une accolade)
    if(a > 5) {
        int f = 5; // y est local au bloc "if"
    }
    // f n'est plus accessible
  }
}