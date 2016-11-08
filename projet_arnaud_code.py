import pygame
import random

pygame.init()

taille_ecran = [700, 600]
ecran = pygame.display.set_mode(taille_ecran)

clock = pygame.time.Clock()

noir = [0,0,0]
rouge = [255,0,0]
blanc = [255,255,255]
vert = [0,255,0]

x = 5
y = 5

class Missile:
    pass

les_missiles = []

class Ennemi:
    pass

les_ennemis = []

image_perso = pygame.image.load('asset/player.png').convert()
image_perso.set_colorkey(noir)

image_vie = pygame.image.load('asset/vie.png').convert()
image_vie.set_colorkey(blanc)

image_missile = pygame.image.load('asset/missile.png').convert()
image_missile.set_colorkey(noir)

image_ennemi = pygame.image.load('asset/ennemi.png').convert()
image_ennemi.set_colorkey(noir)

vie = 3

font = pygame.font.SysFont('Calibri', 50)
score = 0

fini = 0
while fini == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1
        elif event.type == pygame.KEYDOWN:
            if event.key == 32:
                if len(les_missiles) <= 9:
                    m = Missile()
                    m.x = x + 77
                    m.y = y + 40
                    les_missiles.append(m)



    pressed = pygame.key.get_pressed()

    if y < 391:
        if pressed[274]:
            y += 5

    if y > 5:
        if pressed[273]:
            y -= 5

    i = 0
    while i < len(les_missiles):
        m = les_missiles[i]
        m.x += 5
        if m.x > 700:
            del les_missiles[i]
            i -= 1
        i += 1

    j = random.randrange(120)
    if j == 1:
        e = Ennemi()
        e.x = 700
        e.y = random.randrange(50, 450) # 50 + randrange(400)
        les_ennemis.append(e)

    for e in les_ennemis:
        e.x -= 2
        if e.x < 80:
            del les_ennemis[0]
            vie -= 1

    j = 0
    while j < len(les_missiles):
        m = les_missiles[j]
        supprimer = 0

        i = 0
        while i < len(les_ennemis):
            e = les_ennemis[i]
            if m.x > (e.x + 20) or (m.x + 20) < e.x or m.y > (e.y + 20) or (m.y + 20) < e.y:
                pass
            else:
                del les_missiles[j]
                del les_ennemis[i]
                i = len(les_ennemis)
                supprimer = 1
                score += 1

            i += 1

        if supprimer == 0:
            j += 1
        else:
            pass

    image_score = font.render("Score: " + str(score), True, blanc)

    if vie == 0:
        fini = 1

    # DESSIN
    ecran.fill(noir)

    for m in les_missiles:
        ecran.blit(image_missile, [m.x, m.y])


    for e in les_ennemis:
        ecran.blit(image_ennemi, [e.x, e.y])

    pygame.draw.rect(ecran, blanc, [0, 500, 750, 5])
    pygame.draw.rect(ecran, rouge, [85, 0, 5, 500])

    ecran.blit(image_perso, [x , y])


    if vie > 2:
        ecran.blit(image_vie, [600, 525])
    if vie > 1:
        ecran.blit(image_vie, [550, 525])
    if vie >0:
        ecran.blit(image_vie, [500, 525])

    ecran.blit(image_score, [25, 525])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()

