#!coding: utf-8

# ÉCRIRE

# L'ouvrir en mode "écriture" (w = write)
# si le fichier n'existe pas, il sera crée
# si le fichier existe, il sera vidé
f = open('hello.txt', 'w')

# écrire une str (chaîne de caractère)
f.write("Salut")

# pour passer à la ligne, écrivez le caractère ascii 13 : passer à la ligne
f.write("\n")

f.write("Comment ça va ?\n")
f.write("Moi c'est l'éclate !\n")

# finalement, fermer le fichier
f.close()

# LIRE

# ouverture en mode lecture
f = open('hello.txt')
for line in f:
    # la ligne contient donc "Salut\n"
    line = line.strip() # strip enlève les espaces ou \n en début et fin de ligne
    # line == "Salut"
    print(line) # on fait quelque chose avec la ligne, ici print
f.close()

# les lignes peuvent être traitées ou simplement ajoutées à une liste

# WITH

# python propose l'instruction "with" qui permet
# de faire le close tout seul à la fin du bloc

with open('hello.txt') as f:
    f.write("One\n")
    f.write("Two\n")
    f.write("Three\n")
# le close est appelé automatiqmenr