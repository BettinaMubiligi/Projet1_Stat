import numpy as np
import random
import matplotlib.pyplot as plt

taillebat = {1 : 5, 
            2 : 4,
            3 : 3 ,
            4 : 3,
            5 : 2 }
	

class Grille:
    def __init__(self,nom):
        self.grille = np.zeros((10,10), dtype=int)
        self.name = nom

    def __getvalue__(self,i,j):
         return self.grille[i][j]

    # Partie 1 : Modelisation et fonctions simples

    def peut_placer(self, bateau, position, direction):
        taille = taillebat[bateau]
        x,y = position # On suppose que l'utilisateur va rentrer des valeurs entre 1 et 10 et non 0 et 9

        # Placement horizontal
        if direction==1:
            if y+taille > 10:
                print("Position (" + str(x+1) + "," + str(y+taille+1) + ") : sort de la grille")
                return False
            for i in range(taille):
                if self.grille[x-1][y+i-1]!=0:
                    print("Position (" + str(x+1) + "," + str(y+taille+1) + ") occupée")
                    return False
        # Placement vertical
        elif direction==2:
            if x+taille>10:
                print("Position (" + str(x+taille+1) + "," + str(y+1) + ") : sort de la grille")
                return False
            for i in range(taille):
                if self.grille[x+i-1][y-1]!=0:
                    print("Position (" + str(x+taille+1) + "," + str(y+1) + ") occupée")
                    return False
        return True


    def place(self, bateau, position, direction):
        ligne, colonne = position
        if self.peut_placer(bateau,position,direction):
            if direction==1:
                for i in range(taillebat[bateau]):
                    self.grille[ligne-1][colonne+i-1]=bateau
            if direction==2:
                for i in range(taillebat[bateau]):
                    self.grille[ligne+i-1][colonne-1]=bateau
        return self.grille


    def place_alea(self, bateau):
        x = random.randint(1,10)
        y = random.randint(1,10)
        dir=random.randint(1,2)

        while not(self.peut_placer(bateau, (x,y), dir)):
            x = random.randint(1,10)
            y = random.randint(1,10)
            dir=random.randint(1,2)
        print(str(x))
        print(str(y))
        self.place(bateau, (x,y), dir)
    
        return self.grille

    def affiche(self) :
        plt.imshow(self.grille)
        plt.axis('on')
        plt.title(self.name)
        plt.grid(True)
        plt.xticks(np.arange(0, 10, step=1)-0.5, np.arange(1,11))
        plt.yticks(np.arange(0, 10, step=1)-0.5, np.arange(1,11))
        plt.show()

    def eq(self, grille):
        for i in range(10):
            for j in range(10):
                if (self.__getvalue__(i,j)!=grille.__getvalue__(i,j)):
                    return False
        return True 


    def genere_grille(name):
        grille= Grille(name)
        for i in range (1,6):
            grille.place_alea(i)
        return grille

    # Partie 2 : Combinatoire du jeu 

def nb_placements_possibles_bateau(id):
    grille_vide=Grille("Grille vide")
    taille = taillebat[id]
    return ((np.size(grille_vide.grille,0)-taille+1)*np.size(grille_vide.grille, 1)*2)

def nb_placements_possibles_liste_chev(liste_bateaux):
    grille_vide=Grille("Grille vide")
    nb_possibilites = 0
    for bateau in liste_bateaux : 
        nb_possibilites += nb_placements_possibles_bateau(bateau)
    return nb_possibilites

def nb_placements_possibles_liste_sans_chev(liste_bateaux):
    grille_vide=Grille("Grille vide")
    if (len(liste_bateaux)==0):
        return 1
    nb_possibilites = nb_placements_possibles_bateau(liste_bateaux[0])
    dir=1
    grille_vide.place_alea(liste_bateaux[0])
    for bateau in liste_bateaux[1:] : 
        for i in range(10) :
            for j in range (10):
                for dir in range (1,2):
                    if grille_vide.peut_placer(bateau, (i,j), dir):
                        nb_possibilites+=1
        grille_vide.place_alea(bateau)
    return nb_possibilites
    
def grilles_egales(self):
    cpt=0
    while(not(self.eq(genere_grille))):
        cpt+=1
    return cpt

def nb_total_grilles(liste_bateaux):
    cpt=0
    return cpt

    # Partie 3 : Modelisation probabiliste du jeu
