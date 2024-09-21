import numpy as np
import random
import matplotlib.pyplot as plt

taillebat = {1 : 5, 
            2 : 4,
            3: 3 ,
            4: 3,
            5: 2 }

class Grille:
    def __init__(self,nom):
        self.grille = np.zeros((11,11), dtype=int)
        self.name = nom

    def __getvalue__(self,i,j):
         return self.grille[i][j]

    def peut_placer(self, bateau, position, direction):
        taille = taillebat[bateau]
        x, y= position

        #placé horizontal
        if direction==1:
            if x+taille >10:
                print("Débordement de la grille")
                return False
            for i in range(taille):
                if self.grille[x+i][y]!=0:
                    print("occupé à la place " + str(x+i) + ";" +str(y))
                    return False
        #placé vertical
        elif direction==2:
            if y+taille>10:
                print("Débordement de la grille")
                return False
            for i in range(taille):
                if self.grille[x][y+i]!=0:
                    print("occupé à la place " + str(x) + ", " +str(y+i))
                    return False
        return True


    def place(self,bateau, position, direction):
        colonne, ligne = position
        taille = taillebat[bateau]
        if self.peut_placer(bateau,position,direction):
            if direction==1:
                for i in range(taille):
                    self.grille[ligne-1][colonne+i-1]=bateau
            if direction==2:
                for i in range(taille):
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
        self.place(bateau, (x,y), dir)
        print("bateau, direction, (x, y):", bateau,  str(dir)  , (str(x), str(y)))
        return self.grille

    def affiche(self) :
        plt.imshow(self.grille)
        plt.axis('on')
        plt.title(self.name)
        plt.grid(True)
        plt.xticks(np.arange(0, 11, step=1)-0.5, np.arange(1,12))
        plt.yticks(np.arange(0, 11, step=1)-0.5, np.arange(1,12))
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

