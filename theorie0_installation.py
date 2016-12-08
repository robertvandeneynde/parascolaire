#!coding: utf-8
'''
Bonjour ! 
Voici le premier fichier du cours, il contient des détails d'installation.
La théorie de ce cours se veut très courte et va droit au but.
Dans chaque chapitre de théorie, je demande de lire la partie 'Base'
Il existe aussi une partie "Pour en savoir plus" qui est facultative.
Pour donner un chiffre sur "Se veut très courte",
voici le nombre de pages A4 pour chaque chapitre :

                    theorie1 | theorie2 | theorie3 | TOTAL
                  |----------|----------|----------|------
Base              |     2    |    2     |    4     |   8
Base+EnSavoirPlus |     4    |    4     |    7     |  15

En moins de 10 pages, vous avez toute la théorie nécessaire.

Ces 3 pdf sont disponibles en cliquant sur "pdf" en haut du fichier correspondant.

Dans le cadre du parascolaire, je fais les deux premiers chapitres de théorie pendant 4h,
puis on attaque la partie graphique (faire des fenêtres !) pour les 14h restantes.
Le chapitre 3 de la théorie sera appris à chaque étudiant en fonction de son avancée de projet.

Installation
------------
Pour tester un code, vous avez deux options, la première n'installe rien du tout
et la deuxième vous installe tout ce qu'il vous faut (obligatoire à partir de la séance 5) !

Que vous choisissez l'option 1 ou l'option 2, je vous souhaite un Happy Coding et vous
invite à cliquer sur le titre en haut de la page pour commencer la leçon 1 !

Option 1 : Tester en ligne
--------------------------
Tester votre code en ligne sur www.pythontutor.com/visualize.html
Choisissez votre version de python (lisez la remarque voir ci-dessous)
Et cliquez sur "exécuter", le programme s'exécute pas à pas.
Appuyez sur "Next" pour avancer d'une ligne.
Vous pouvez aussi sauter à la fin en appuyant sur "End".

Un exemple ici : robertvandeneynde.be/parascolaire/pythontutor.html

Cependant dès que nous ferons des fenêtres, vous devrez installer pygame et donc faire l'Option 2.

Option 2 : Installer
--------------------

Si vous avez un souci, envoyez moi un mail !

- Téléchargez python 3.5 sur https://www.python.org/downloads/

- Téléchargez pygame :
  - (windows) : téléchargez un des deux whl suivants sur http://www.lfd.uci.edu/~gohlke/pythonlibs/
    (windows 64 bits) pygame‑1.9.2rc1‑cp35‑cp35m‑win_amd64.whl
    (windows 32 bits) pygame‑1.9.2rc1‑cp35‑cp35m‑win32.whl
    Si vous ne savez pas si votre ordi est 32 ou 64 bits, allez dans "Panneau de configuration > Système"
    
    Placez ce fichier dans le dossier existant C:\Python35\Script\
    (Bouton windows > Ordinateur > C > Python35 > Script)
    
    Ouvrez "cmd" (cliquez sur le bouton windows, tappez "cmd") et entrez les deux commandes suivantes :
    
    cd C:\Python35\Script\
    pip.exe pygame‑1.9.2rc1‑cp35‑cp35m‑win_amd64.whl
    
    (changer le nom du fichier whl si nécessaire)
    
  - (mac) : suivez ceci : http://stackoverflow.com/questions/30743194/pygame-installation-mac-os-x
    Vous devez donc d'abord installer XCode via l'AppStore
    Puis lancer une commande ruby pour installer homebrew (brew)
    Puis lancer plein de commandes brew pour installer le reste 
    
  - (linux) : suivez ceci : http://askubuntu.com/questions/401342/how-to-download-pygame-in-python3-3

(Si vous utilisez l'ancienne version de python : python 2, lisez la remarque ci dessous

Ensuite vous lancer le programme "IDLE",
vous faites "File > New", écrivez du code, enregistrez le fichier sur votre bureau,
et appuyez sur F5 (ou "Run" dans les menus) pour le lancer.

(Pour d'autres éditeurs de texte, lisez la note ci-dessous)

Remarque sur les versions de python
-----------------------------------
Si vous avez reçu une clef usb avec python, la version est 2.7 (ancienne version)
Les ordis à l'école ont la version récente : 3.5 (nouvelle version)
Pour ce cours, ça ne change quasi rien, à part trois petites différences suivantes :

1) (python2) print a,b | (python3) print(a,b)
2) (python2) 7/2 == 3  | (python3) 7/2 == 3.5
3) La gestion des accents dans les chaînes de caractère

Si vous avez python2 et voulez utiliser certaines fonctionnalités de python3,
ajoutez une ligne comme ceci au début du fichier :
from __future__ import print_function  # pour le print
from __future__ import division        # pour la division
Pour les accents, c'est plus compliqué, mais from __future__ import unicode_litterals est un bon début

Autres éditeurs de texte
------------------------
PYCHARM: https://www.jetbrains.com/pycharm/download/

WINDOWS: notepad++
Téléchargez le sur https://notepad-plus-plus.org/
et vous pourrez aisément modifier des fichiers python (entre autres !)
Pour lancer le programme, allez dans le menu "Exécuter", cliquez sur "Exécuter" et entrez la commande suivante :
C:\Python27\python.exe -i "$(FULL_CURRENT_PATH)"
(27 est la version, changez en 34 ou 35 en fonction de votre téléchargement)
Et cliquez sur "Exécuter". Pour éviter de refaire la tâche,
assignez un raccourci (comme F9) en cliquant sur le bouton "Enregistrer".

Opengl
------
À la fin du cours je ferai une introduction à la 3D pour les intéressés.
Il faut installer pyOpenGL (http://pyopengl.sourceforge.net/)
et numpy (http://www.scipy.org/scipylib/download.html)
PyOpengl et numpy sont installés sur les ordis de l'école.
Si vous êtes intéressés de l'installer chez vous, contactez moi.
Sous windows pous pouvez faire la même chose qu'avec pygame.
(via http://www.lfd.uci.edu/~gohlke/pythonlibs/)
'''