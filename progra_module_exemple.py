#!coding: utf-8

def calcul(x):
    y = x + 5
    if y > 10:
        y = 10
    return y + 2

TAILLE = 16

class Personnage:
    def __init__(self, vie, max_vie=100, mana=0):
        self.vie = vie
        self.max_vie = max_vie
        self.mana = mana
    
    def boire_potion(self, montant):
        self.vie += montant
        if self.vie > self.max_vie:
            self.vie = self.max_vie
    
