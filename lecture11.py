import random
from random import randint

class Equipe:
    def __init__(self, force, nom):
        self.force = force
        self.nom = nom
        
    def prez(self, j):
        for n in range(j):
            print(self.nom, 'for the win')
    
    def calc(self):
        x = self.force + randint(-2,2)
        if x < 0:
            x = 0
        return x

class Match:
    def __init__(self, a, b):
        self.eq = [a, b]
        self.victoire = -1
    
    def play(self):
        """
        simule un match entre les deux équipes
        victoire indique le numéro de l'équipe gagnante
        peut résulter en une égalité (victoire = -1)
        """
        p = self.eq[0].calc()
        q = self.eq[1].calc()
        if p > q:
            self.victoire = 0
        else:
            if p < q:
                self.victoire = 1
            else:
                self.victoire = -1
                
L = []
noms = ["Joz", "Dins", "Mots", "Lurs", "Dars", "Miss", "Robz", "Friz"]
for i in range(8):
    e = Equipe(randint(1,3) + randint(0,2), noms[i])
    e.prez(randint(1,6))
    L.append(e)

historique = []

while len(L) > 1:
    m = Match(L[0], L[1])
    while m.victoire == -1:
        m.play()
        if m.victoire == 0:
            L.append(L[0])
        else:
            if m.victoire == 1:
                L.append(L[1])
        if L.victoire != -1:
            del L[0]
            del L[1]
    historique.append(m)
    
i = 1
for h in historique:
    print('Match', i)
    j = 0
    for e in h.eq:
        if e.victoire == j:
            print('- ', e.nom, '(victoire)')
        else:
            print('- ', e.nom)
        j += 1
    i += 1
    
print(L[0].prez(10))