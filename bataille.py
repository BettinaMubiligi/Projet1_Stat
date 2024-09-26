import numpy as np
import random
import matplotlib.pyplot as plt
from grille import *

# Partie 3 : Modelisation probabiliste du jeu

class Bataille :
    def __init__(self, name):
        self.grille=Grille.genere_grille(name)
    
    # Version aleatoire

    def joue_aleatoire(self):
        grille_vide= Grille('grille_vide')
        x = random.randint(1,10)
        y = random.randint(1,10)
        direction=random.randint(1,2)
        bateau = random.randint(1,5)
        position = x,y
        exploree =set()
        nb_coups = 0

        while (not(self.grille.eq(grille_vide))):
            if(self.grille.peut_placer(bateau, position,direction)):
                exploree.add((x,y))
                nb_coups+=1
                x = random.randint(1,10)
                y = random.randint(1,10)
                while((x,y) in exploree) :
                    x = random.randint(1,10)
                    y = random.randint(1,10)
                direction=random.randint(1,2)
                bateau = random.randint(1,5)
                position = x,y
            else :
                exploree.add((x,y))
                nb_coups+=1
                self.grille.grille[x-1][y-1]=0
                x = random.randint(1,10)
                y = random.randint(1,10)
                while((x,y) in exploree) :
                    x = random.randint(1,10)
                    y = random.randint(1,10)
                direction=random.randint(1,2)
                bateau = random.randint(1,5)
                position = x,y
        
        return nb_coups

    # Version heuristique
    def joue_heuristique(self):
        grille_vide= Grille('grille_vide')
        x = random.randint(1,10)
        y = random.randint(1,10)
        direction=random.randint(1,2)
        bateau = random.randint(1,5)
        position = x,y
        exploree =set()
        nb_coups = 0

        while (not(self.grille.eq(grille_vide))):
            if(self.grille.peut_placer(bateau, position,direction)):
                exploree.add((x,y))
                nb_coups+=1
                x = random.randint(1,10)
                y = random.randint(1,10)
                while((x,y) in exploree) :
                    x = random.randint(1,10)
                    y = random.randint(1,10)
                direction=random.randint(1,2)
                bateau = random.randint(1,5)
                position = x,y

            else :
                exploree.add((x,y))
                nb_coups+=1
                id = self.grille.grille[x-1][y-1]
                self.grille.grille[x-1][y-1]=0
                x-=1
                y-=1
                cases_bat= set()
                for i in range(10):
                    if (self.grille.grille[x][i]==bateau):
                        cases_bat.add((x,i))
                        self.grille.grille[x][i]=0
                        nb_coups+=1
                    elif (self.grille.grille[i][y]==bateau):
                        cases_bat.add((i,y))
                        self.grille.grille[i][y]=0
                        nb_coups+=1
                x = random.randint(1,10)
                y = random.randint(1,10)
                direction=random.randint(1,2)
                bateau = random.randint(1,5)
                position = x,y
        
        return nb_coups

    # Version probabiliste simplifiee

    def joue_proba_simplifiee(self):
        pos_grille=set()

        for i in range(1,11):
            for j in range (1,11):
                pos_grille.add((i,j))
    
        return pos_grille
        











