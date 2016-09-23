#!coding: utf-8

import pygame

pygame.init()

taille = [700, 500]
ecran = pygame.display.set_mode(taille)

clock = pygame.time.Clock()

noir = [0,0,0]
rouge = [255,0,0]
blanc = [255,255,255]

# on charge la police de caractère, 25 est la taille
font = pygame.font.SysFont('Calibri', 25)

ma_position = 0
score = 0

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
    
    ma_position += 10
    
    if ma_position > 700:
        ma_position = 0
        score += 1
    
    # dessin
    ecran.fill(blanc)
    
    pygame.draw.rect(ecran, rouge, [ma_position, 100, 50,50])
    
    # On crée une image depuis la police et le texte
    # True signifie "anti-aliasé" (c'est plus joli)
    image_nom_joueur = font.render("Robert", True, noir)
    image_score = font.render("Score: " + str(score), True, noir)

    # on "blitte" l'image sur l'écran
    ecran.blit(image_nom_joueur, [20,20])
    ecran.blit(image_score, [600,20])
    
    pygame.display.flip()
    
    clock.tick(60)

pygame.quit()

# Pour avoir une police en gras :
# font = pygame.font.SysFont('Calibri', 25, True)

# En Gras ET italique :
# font = pygame.font.SysFont('Calibri', 25, True, True)

# En italique sans gras :
# font = pygame.font.SysFont('Calibri', 25, False, True)

# Pour charger depuis un fichier trouvé par exemple sur https://fontlibrary.org/
# font = pygame.font.Font('hello.otf', 25)

