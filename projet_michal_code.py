import random
import pygame
from math import atan2, degrees, sin, cos, sqrt

pygame.init()

res = [800, 600]
screen = pygame.display.set_mode(res)

clock = pygame.time.Clock()

x = 100
y = 100
speed = 0
planetx = -100
planety = -100

font = pygame.font.SysFont('Calibri', 25)
score = 0
lvl = 1

class Missile:
    pass
class Rocket:
    pass
class Ennemi:
    pass
liste_missile = []
liste_rocket = []
liste_ennemi = []

def pythagore(point1, point2):
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return sqrt(dx * dx + dy * dy)

def blit_center(image, pos):
    screen.blit(image, [pos[0] - image.get_width() / 2, pos[1] - image.get_height()/2])

vert = [0, 255, 0]

ship = pygame.image.load('ship.png').convert_alpha()
blast = pygame.image.load('blast.png').convert_alpha()
rocketimg = pygame.image.load('rocket.png').convert_alpha()
background_800x600 = pygame.image.load('background_800x600.png').convert_alpha()
background_1280x720 = pygame.image.load('background_1280x720.png').convert_alpha()
planete = pygame.image.load('planet.png').convert_alpha()

compteur_ennemis = 0
fini = 0
while fini == 0:
    position_souris = pygame.mouse.get_pos()
    mouse_x = position_souris[0]
    mouse_y = position_souris[1]
    image_score = font.render("Score: " + str(score), True, [255,255,255])
    image_lvl = font.render("Level: " + str(lvl), True, [255,255,255])
    image_vitesse = font.render(str(speed * 20) + "%", True, [255,255,255])
    if score >= 100:
        lvl += 1
        score = 0
    compteur_ennemis += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            fini = 1

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(liste_missile) >= 10:
                print ("reloading")
            else:
                le_missile = Missile()
                le_missile.x = x
                le_missile.y = y
                le_missile.angle = atan2(mouse_y - y, mouse_x - x)
                liste_missile.append(le_missile)

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                if len(liste_rocket) >= 1:
                    print ("reloading rocket")
                else:
                    rocket = Rocket()
                    rocket.x = x
                    rocket.y = y

                    liste_rocket.append(rocket)

    if compteur_ennemis >= 60*5:
        compteur_ennemis = 0
        ennemi = Ennemi()
        liste_ennemi.append(ennemi)
        ennemi.x = random.randrange(800)
        ennemi.y = random.randrange(600)
        ennemi.couleur = [random.randrange(255), random.randrange(255), random.randrange(255)]

    # supprimer les missles trop loin
    if len(liste_missile) > 0 and liste_missile[0].x >= 800:
        del liste_missile[0]
    if len(liste_missile) > 0 and liste_missile[0].y >= 600:
        del liste_missile[0]
    if len(liste_missile) > 0 and liste_missile[0].x <= 0:
        del liste_missile[0]
    if len(liste_missile) > 0 and liste_missile[0].y <= 0:
        del liste_missile[0]

    if len(liste_rocket) > 0 and liste_rocket[0].x >= 800:
        del liste_rocket[0]
    if len(liste_rocket) > 0 and liste_rocket[0].y >= 600:
        del liste_rocket[0]
    if len(liste_rocket) > 0 and liste_rocket[0].x <= 0:
        del liste_rocket[0]
    if len(liste_rocket) > 0 and liste_rocket[0].y <= 0:
        del liste_rocket[0]

    # bouger le vaisseau
    pressed = pygame.key.get_pressed()

    angle = atan2(mouse_y - y, mouse_x - x)
    deplacement_x = cos(angle)
    deplacement_y = sin(angle)

    if pressed[pygame.K_w]:
        speed += 0.1
    if speed >= 5:
        speed = 5
    if pressed[pygame.K_s]:
        speed -= 0.1
    if speed <= -5:
        speed = -5
    if speed == 0:
        etat = 0
    elif speed > 0:
        etat = 1
    elif speed < 0:
        etat = 2
    if pressed[pygame.K_SPACE]:
        if etat == 1:
            speed -= 0.1
            if speed <= 0:
                speed = 0
        if etat == 2:
            speed += 0.1
            if speed >= 0:
                speed = 0

    if etat == 1:
        planetx -= deplacement_x/20 * speed
        planety -= deplacement_y/20 * speed
    else:
        if etat == 2:
            planetx += deplacement_x/20 * speed
            planety += deplacement_y/20 * speed

    x += speed * deplacement_x
    y += speed * deplacement_y

    # bouger les missiles
    i = 0
    while i < len(liste_missile):
        liste_missile[i].x += 12 * cos(liste_missile[i].angle)
        liste_missile[i].y += 12 * sin(liste_missile[i].angle)
        i = i + 1

    j = 0
    while j < len(liste_rocket):
        angle_rocket = atan2(mouse_y - liste_rocket[j].y, mouse_x - liste_rocket[j].x)
        liste_rocket[j].x += 10 * cos(angle_rocket)
        liste_rocket[j].y += 10 * sin(angle_rocket)
        j += 1

    j = 0
    while j < len(liste_missile):
        m = liste_missile[j]
        i = 0
        while i < len(liste_ennemi):
            e = liste_ennemi[i]
            distance = pythagore([m.x, m.y],[e.x, e.y])
            if distance <= 20:
                del liste_ennemi[i]
                i -= 1
                score += 1
            i += 1
        j += 1

    # DESSIN
    if res == [800,600]:
        screen.blit(background_800x600, [0,0])
    else:
        if res == [1280,720]:
            screen.blit(background_1280x720, [0,0])
    screen.blit(planete, [planetx,planety])


    # vaisseau
    ship_rot = pygame.transform.rotozoom(ship, - degrees(angle) + 90, 1)
    blit_center(ship_rot, [x, y])

    # missiles
    i = 0
    while i < len(liste_missile):
        blit_center(pygame.transform.rotozoom(blast, -degrees(liste_missile[i].angle),1), [liste_missile[i].x, liste_missile[i].y])
        i = i + 1

    # rocket
    j = 0
    while j < len(liste_rocket):
        angle_rocket = atan2(mouse_y - liste_rocket[j].y, mouse_x - liste_rocket[j].x)
        screen.blit(pygame.transform.rotozoom(rocketimg, -degrees(angle_rocket),1), [liste_rocket[j].x, liste_rocket[j].y])
        j += 1

    # ennemi
    p = 0
    while p < len(liste_ennemi):
        pygame.draw.circle(screen, liste_ennemi[p].couleur, [liste_ennemi[p].x,liste_ennemi[p].y], 20)
        p += 1

    screen.blit(image_score, [600,20])
    screen.blit(image_lvl, [600,45])
    screen.blit(image_vitesse, [600,500])
    if x >= 730:
        x = 730
    if x <= 70:
        x = 70
    if y >= 530:
        y = 530
    if y <= 70:
        y = 70

    pygame.display.flip()

    clock.tick(60)
pygame.quit()