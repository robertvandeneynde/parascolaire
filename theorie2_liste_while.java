import java.util.ArrayList;
public class theorie2_liste_while {
  public static void main(String[] args) {

    ////////////////////////
    // Base TROIS : while //
    ////////////////////////

    // les while sont comme des if, sauf qu'après avoir exécuté leur code, ils recommencent

    int a = 5;

    if(a < 10) {
        System.out.println("Tada");
    }
        
    while(a < 10) {
        System.out.println("Hello");
    }
        
    // ce programme va afficher "Hello" sans s'arrêter...
    // pour éviter de faire une "boucle infinie", il faudrait que la condition devienne fausse
    // par exemple comme ceci

    int i = 0;
    while(i < 10) {
        System.out.println("Hello");
        i = i + 1;
    }
    // maintenant, Hello n'est affiché que dix fois ^^

    // on peut bien sûr utiliser nos variables

    i = 0;
    while(i < 10) {
        System.out.println("Hello " + (2 * i + 5));
        i = i + 1;
    }

    // affichera "Hello 5", "Hello 7", "Hello 9" etc.

    /////////////////////////
    // Base QUATRE : array //
    /////////////////////////

    // on peut créer des array (tableaux)
    int[] maListeZero = new int[4]; // 4 élements ! sont initialisés à 0
    int[] maListe = {3,4,7,4}; // 4 éléments, donnés

    // 1) Lire
    int premier = maListe[0]; // l'élément numéro 0 est le premier
    int dernier = maListe[3]; // vu que notre liste est de taille 4, 3 est le dernier
    int taille = maListe.length; // count permet de savoir la taille (raccourci : sizeof)
    System.out.println(maListe[5]); // ERREUR, il n'y a pas d'élément "5", le dernier était "3"

    // le "numéro" est appelé "l'indice", l'indice du "1" dans notre liste est donc 0

    // 2) Écrire
    maListe[0] = 9; // hop ! le tableau vaut [9,2,7,2]
    maListe[5] = 2; // ERREUR : IndexOutOfBoundsException

    // Les boucles et les array vont bien ensemble,
    // on peut par exemple afficher tous les éléments d'une liste avec un while

    i = 0;
    while(i < maListe.length) {
        System.out.println(maListe[i]);
        i = i + 1;
    }

    // Tu as toutes les bases pour faire tous les exercices
    // Je conseille de faire au moins le 5 (max list) et puis de passer à pygame pour créer des fenêtres !

    ////////////////////////////
    // Pour en savoir plus... //
    ////////////////////////////

    //// while ////
    // certaines structures "while" sont très utilisées, et peuvent être remplacées par des "for"

    // compter !
    for(int j = 0; j < 5; j++) {
        System.out.println(j);
    }
        
    // ce code peut s'écrire comme ceci avec un while :
    i = 0;
    while(i < 5) {
        System.out.println(i);
        i = i + 1;
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
    
    // la seule différence est que toute variable déclarée dans le "A"
    // appartient au bloc du for() (while utilisait une variable globale)
    
    for(int j = 0; j < 5; j++) {
        // le j est local
    }
    // j n'existe plus
    
    // parcourir une liste ! foreach

    for(int nombre : maListe) {
        System.out.println(nombre);
    }
        
    // ce qui peut s'écrire comme ceci avec un while 

    i = 0;
    while(i < maListe.length){
        int nombre = maListe[i];
        System.out.println(nombre);
        i = i + 1;
    }

    //// list ////
    
    // ArrayList
    
    // Les ArrayList peuvent changer de taille !
    // il faut faire import java.util.ArrayList en haut du fichier
    ArrayList<Integer> belleListe = new ArrayList<Integer>(); // une liste d'entiers, vide
    System.out.println(belleListe.size()); // taille 0
    belleListe.add(1); // ajouter à la fin
    belleListe.add(2);
    belleListe.add(7);
    belleListe.add(2);
    System.out.println(belleListe.size()); // taille 4
    premier = belleListe.get(0); // lire : get
    belleListe.set(0, 9); // écrire : set, belleListe = [9, 2, 7, 2]
    
    belleListe.remove(2); // enlever l'élément à l'indice 2 (le 7)
    // belleListe = [9,2,2]
    System.out.println(belleListe.size()); // taille 3

    // TODO: String
  }
}