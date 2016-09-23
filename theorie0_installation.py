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
- Téléchargez python 2.7 sur https://www.python.org/downloads/
- Téléchargez pygame :
  - (windows) : https://bitbucket.org/pygame/pygame/downloads/pygame-1.9.1.win32-py2.7.msi
  - (mac) : http://pygame.org/ftp/pygame-1.9.1release-python.org-32bit-py2.7-macosx10.3.dmg
  - (linux) : sudo apt-get install python-pygame

(Pour utiliser une version plus récente de python : python 3, lisez la remarque ci-dessous)

Ensuite vous lancer le programme "IDLE",
vous faites "File > New", écrivez du code, enregistrez le fichier sur votre bureau,
et appuyez sur F5 (ou "Run" dans les menus) pour le lancer.

(Pour d'autres éditeurs de texte, lisez la note ci-dessous)

Remarque sur les versions de python
-----------------------------------
Le cours utilise la version 2.7 à cause des contraintes des salles informatiques à l'école,
mais le futur de python sont les versions 3.x ! (Comme 3.4)
Pour ce cours ci ça ne change quasi rien, à part trois petites différences décrites ci-dessous.

Si vous voulez suivre exactement le cours, prenez 2.7
Si vous voulez suivre le cours en python 3, choisissez 3.4 (et non 3.5)
Si vous êtes sous mac, il est plus facile d'installer python 2.7 (à cause de pygame, voir ci-dessous)

Les 3 différences entre python 2 et python3 sont celles-ci :

1) (python2) print a,b | (python3) print(a,b)
2) (python2) 7/2 == 3  | (python3) 7/2 == 3.5
3) La gestion des accents dans les chaînes de caractère

Si vous avez python2 et voulez utiliser certaines fonctionnalités de python3,
ajoutez une ligne comme ceci au début du fichier :
from __future__ import print_function  # pour le print
from __future__ import division        # pour la division
Pour les accents, c'est plus compliqué, mais from __future__ import unicode_litterals est un bon début

Pygame et versions de python :

À partir de la 5ème séance, nous ferons des fenêtres, et vous devrez installer pygame.
Sur windows, c'est très simple : https://bitbucket.org/pygame/pygame/downloads
Choisissez en fonction de la version de python et la version de votre ordi parmi
win-amd64-py2.7.msi / win-amd64-py3.4.msi / win32-py2.7.msi / win32-py3.4.msi
Si vous ne savez pas si votre ordi est 32 ou 64 bits, allez dans "Panneau de configuration > Système"

Sur mac, je conseille surtout python2, vous pouvez trouver un installateur sur http://www.pygame.org/download.shtml
pour python3, je vais devoir vous demander de suivre les instructions compliquées ici :
http://programarcadegames.com/index.php?chapter=foreword&lang=fr

Sur linux pour python2, c'est très simple : sudo apt-get install python-pygame
Pour python3, veuillez suivre le lien ci dessous :
http://programarcadegames.com/index.php?chapter=foreword&lang=fr
Copier coller 4 commandes et hop, c'est fait.

Autres éditeurs de texte
------------------------
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
Je n'ai pas encore essayé d'installer ceux-ci sous windows. Google est votre ami.
'''