import numpy as np
import random
import matplotlib.pyplot as plt
from grille import *

# Partie 3 : Modélisation probabiliste du jeu


class Bataille:

    def __init__(self, name):
        self.grille = Grille.genere_grille(name)
        # une grille de tirs vide pour suivre les coups joués
        self.nbTirs = np.zeros((10, 10), dtype=int)

    def joue(self, position):
        #on tire à la position(x, y)
        x, y = position

        # case déjà jouée : 0 si on pas testé la case (x,y), 1 sinon
        if self.nbTirs[x - 1][y - 1] != 0:
            return False
        else:
            self.nbTirs[x - 1][y - 1] = 1
            # cas où on touche un bateau ou pas
            if self.grille.__getvalue__(x, y) != 0:
                return True
            return False

    def victoire(self):
        # on vérifie que toutes les cases contenant un bateau ont été tirées
        for i in range(10):
            for j in range(10):
                if (self.grille.grille[i][j] != 0 and self.nbTirs[i][j] == 0):
                    return False
        return True

    def reset(self):
        #pour vider le tableau des tirs
        self.nbTirs = np.zeros((10, 10), dtype=int)

    # Version aléatoire
    def joue_aleatoire(self):
        exploree = set()
        nb_coups = 0
        while not self.victoire():
            #on tire au hasard des coordonnées
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            #on vérifie qu'il n'a pas déjà été joué
            while (x, y) in exploree:
                x = random.randint(1, 10)
                y = random.randint(1, 10)
            exploree.add((x, y))
            nb_coups += 1
            #on joue le coup
            self.joue((x, y))
        print("Nombre de coups en version aléatoire : ")
        return nb_coups

    # Version heuristique
    def joue_heuristique(self):
        nbCoups = 0
        exploree = set()
        #cases connexes de la case
        cases_voisines = []

        while not self.victoire():
            #si la liste des cases voisines n'est pas vide
            if cases_voisines:
                # on choisit une case connexe à explorer avec .pop et comme ça on le retire direct de la liste
                x, y = cases_voisines.pop()
            else:
                #on tire aléatoirement des coordonnées
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                while (x, y) in exploree:
                    x = random.randint(1, 10)
                    y = random.randint(1, 10)

            exploree.add((x, y))
            nbCoups += 1

            #cas où on touche un bateau : on regarde les cases connexes
            if self.joue((x, y)) == True:
                #on ajoute les cases adjacentes pour explorer (nord,sud,est,ouest)
                #case au nord, on vérifie que la case voisine au-dessus ne dépasse pas de la grille et qu'elle n'a pas été déjà explorée, et ensuite on l'ajoute dans la liste des cases voisines
                if (x > 1 and (x - 1, y) not in exploree):
                    cases_voisines.append((x - 1, y))
                #cas sud
                if (x < 10 and (x + 1, y) not in exploree):
                    cases_voisines.append((x + 1, y))
                #cas ouest
                if (y > 1 and (x, y - 1) not in exploree):
                    cases_voisines.append((x, y - 1))
                #cas est
                if (y < 10 and (x, y + 1) not in exploree):
                    cases_voisines.append((x, y + 1))
        print("Nombre de coups en version heuristique : ")
        return nbCoups

    #Fonction qui génère la matrice des probabilités de présence d'un bateau dans une case
    def genere_mat_nb_possibilites(bateau):
        mat = Grille("x")
        k = taillebat[bateau] - 1

        for i in range(10):
            for j in range(10):
                if i < k or i >= 10 - k or j < k or j >= 10 - k:
                    if (i < k and j < k) or (i < k and j >= 10 - k) or (
                            i >= 10 - k and j < k) or (i >= 10 - k
                                                       and j >= 10 - k):
                        mat.grille[i][j] = 2
                    else:
                        mat.grille[i][j] = 3
                else:
                    mat.grille[i][j] = 4

        return mat.grille

    #Version probabiiste simplifiée
    def joue_proba_simplifiee(self, liste_bateaux):
        mat_total = Grille("grille_probas")
        for b in liste_bateaux:
            matb = Bataille.genere_mat_nb_possibilites(b)
            for i in range(10):
                for j in range(10):
                    mat_total.grille[i][j] += matb[i][j]

        nb_coups = 0
        bateaux_restants = set(liste_bateaux)

        while bateaux_restants:
            coordonnees = coordonnees_triee(mat_total.grille)

            for i, j in coordonnees:
                nb_coups += 1
                if self.joue((i + 1, j + 1)):
                    # Bateau touché
                    id_bateau = self.grille.grille[i][j]
                    if id_bateau != 0:
                        # Marquer toutes les cases du bateau comme touchées
                        for x in range(10):
                            for y in range(10):
                                if self.grille.grille[x][y] == id_bateau:
                                    self.grille.grille[x][y] = 0
                                    mat_total.grille[x][y] -= 4

                        # Retirer le bateau coulé de la liste
                        bateaux_restants.discard(id_bateau)
                else:
                    # Case vide
                    mat_total.grille[i][j] -= 5

                if self.victoire():
                    print("Nombre de coups en version probabiliste : ")
                    return nb_coups

        print("Nombre de coups en version probabiliste : ")
        return nb_coups

#Affichage des matrices avec les tirs

    def affiche_mat_nbTirs_aleatoire(self):
        nb_coups = 0

        while not self.victoire():
            nb_coups += self.joue_aleatoire()

        print("matrice tirs après victoire :")
        print(self.nbTirs)

        print("\ngrille bateaux :")
        print(self.grille.grille)
        print("nb coups : " + str(nb_coups))

    def affiche_mat_nbTirs_heuristique(self):
        nb_coups = 0

        while not self.victoire():
            nb_coups += self.joue_heuristique()

        print("matrice tirs après victoire :")
        print(self.nbTirs)

        print("\ngrille bateaux :")
        print(self.grille.grille)
        print("nb coups : " + str(nb_coups))

    def affiche_mat_nbTirs_probabiliste(self, liste_bateaux):
        nb_coups = 0

        while not self.victoire():
            nb_coups += self.joue_proba_simplifiee(liste_bateaux)

        print("matrice tirs après victoire :")
        print(self.nbTirs)

        print("\ngrille bateaux :")
        print(self.grille.grille)
        print("nb coups : " + str(nb_coups))


# Partie graphique : distribution des coups
# Simulation aléatoire

    def simulation_distribution(nbSimu):
        resultats = []
        for _ in range(nbSimu):
            jeu = Bataille("simulation")
            resultats.append(jeu.joue_aleatoire())

        # Tracer la distribution
        plt.hist(resultats, bins=20, edgecolor='black', alpha=0.7)
        plt.title("Distribution du nombre de coups avec joue aléatoire")
        plt.xlabel("Nombre de coups")
        plt.ylabel("Nombre de parties")
        plt.show()

    # Simulation probabiliste
    def simulation_distribution_probabiliste(nbSimu):
        resultats = []
        for _ in range(nbSimu):
            jeu = Bataille("simulation")
            resultats.append(jeu.joue_proba_simplifiee([1, 2, 3, 4, 5]))

        plt.hist(resultats, bins=20, edgecolor='black', alpha=0.7)
        plt.title("Distribution du nombre de coups avec joue proba simplifiée")
        plt.xlabel("Nombre de coups")
        plt.ylabel("Nombre de parties")
        plt.show()

    # Simulation heuristique
    def simulation_distribution_heuristique(nbSimu):
        resultats = []
        for _ in range(nbSimu):
            jeu = Bataille("simulation")
            resultats.append(jeu.joue_heuristique())

        plt.hist(resultats, bins=20, edgecolor='black', alpha=0.7)
        plt.title("Distribution nombre coups avec joue heuristique")
        plt.xlabel("Nombre de coups")
        plt.ylabel("Nb parties")
        plt.show()
