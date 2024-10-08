import numpy as np
import random
import matplotlib.pyplot as plt
from grille import *

# Partie 3 : Modelisation probabiliste du jeu


class Bataille:

    def __init__(self, name):
        self.grille = Grille.genere_grille(name)

    # Version aleatoire :
    "On parcourt tous les indices de la grille aléatoirement en comptant le nombre de coups et on touche toutes les cases jusqu'à ce que la grille soit vide (on la compare à la grille vide pour vérifier si c'est bien le cas) "

    def joue_aleatoire(self):
        grille_vide = Grille('grille_vide')
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        direction = random.randint(1, 2)
        bateau = random.randint(1, 5)
        position = x, y
        exploree = set()
        nb_coups = 0

        while (not (self.grille.eq(grille_vide))):
            if (self.grille.peut_placer(bateau, position, direction)):
                exploree.add((x, y))
                nb_coups += 1
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                while ((x, y) in exploree):
                    x = random.randint(1, 10)
                    y = random.randint(1, 10)
                direction = random.randint(1, 2)
                bateau = random.randint(1, 5)
                position = x, y
            else:
                exploree.add((x, y))
                nb_coups += 1
                self.grille.grille[x - 1][y - 1] = 0
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                while ((x, y) in exploree):
                    x = random.randint(1, 10)
                    y = random.randint(1, 10)
                direction = random.randint(1, 2)
                bateau = random.randint(1, 5)
                position = x, y
        print("Nombre de coups en version aleatoire : ")
        return nb_coups

    # Version heuristique
    "Parcours aléatoire de la grille jusqu'à ce qu'on touche un bateau, dans quel cas on parcours la ligne et la colonne de la case du bateau pour trouver le reste de ses cases et le couler "

    def joue_heuristique(self):
        grille_vide = Grille('grille_vide')
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        direction = random.randint(1, 2)
        bateau = random.randint(1, 5)
        position = x, y
        exploree = set()
        nb_coups = 0

        while (not (self.grille.eq(grille_vide))):
            if (self.grille.peut_placer(bateau, position, direction)):
                exploree.add((x, y))
                nb_coups += 1
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                while ((x, y) in exploree):
                    x = random.randint(1, 10)
                    y = random.randint(1, 10)
                direction = random.randint(1, 2)
                bateau = random.randint(1, 5)
                position = x, y

            else:
                exploree.add((x, y))
                nb_coups += 1
                id = self.grille.grille[x - 1][y - 1]
                self.grille.grille[x - 1][y - 1] = 0
                x -= 1
                y -= 1
                #cases_bat = set()
                for i in range(10):
                    if (self.grille.grille[x][i] == bateau):
                        #cases_bat.add((x, i))
                        self.grille.grille[x][i] = 0
                        nb_coups += 1
                    elif (self.grille.grille[i][y] == bateau):
                        #cases_bat.add((i, y))
                        self.grille.grille[i][y] = 0
                        nb_coups += 1
                x = random.randint(1, 10)
                y = random.randint(1, 10)
                direction = random.randint(1, 2)
                bateau = random.randint(1, 5)
                position = x, y
        print("Nombre de coups en version heuristique : ")
        return nb_coups

    # Version probabiliste simplifiee
    """Fonction intermédiaire permettant de placer le nombre de combinaisons de bateaux possibles                                        pour une case donnée et un bateau donné dans une grille"""

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

    """
        1/ création de la grille avec la somme de toutes les probabilités pour chaque bateau.
        
          2/ Implémentation similaire à la version heuristique, en commençant par les cases avec la plus grande probabilité de contenir un bateau tout en modifiant les probabilités dans les cases en fonction du résultat du coup :                       
        si la case est vide, on enlève 1 à la probabilité de présence de tous les bateaux dans la case (-5), si on touche un bateau, on ne touche pas aux probabilités et mais on parcourt les cases adjacentes pour couler le bateau, et en le coulant, on enlève 1 à la probabilité de tous les autres bateaux dans la case (-4).
        
        On remplit un ensemble avec les coordonnées à explorer dans l'ordre (coordonnées avec la plus grande probabilité de contenir un bateau), et on modifie systématiquement cet ensemble avec les nouvelles probabilités de contenir un bateau dans les cases à chaque tour.
        """

    def joue_proba_simplifiee(self, liste_bateaux):
        mat_total = Grille("grille_proba")
        for b in liste_bateaux:
            matb = Bataille.genere_mat_nb_possibilites(b)
            for i in range(10):
                for j in range(10):
                    mat_total.grille[i][j] += matb[i][j]

        nb_coups = 0
        bateaux_restants = set(liste_bateaux)
        grille_vide = Grille('grille_vide')

        while bateaux_restants:
            # on recalcule les coordonnées à chaque tour
            coordonnee = coordonnees_triee(mat_total.grille)

            for i, j in coordonnee:
                nb_coups += 1
                if self.grille.grille[i][j] == 0:
                    # Case vide
                    mat_total.grille[i][j] -= 5
                else:
                    # bateau touché : on  parcourt la ligne et la colonne pour toucher toutes les cases et on modifie les probabilités de toutes les cases
                    id = self.grille.grille[i][j]
                    self.grille.grille[i][j] = 0
                    mat_total.grille[i][j] -= 4
                    for x in range(10):
                        for y in range(10):
                            if self.grille.grille[x][y] == id:
                                self.grille.grille[x][y] = 0
                                mat_total.grille[x][y] -= 4

                    # on retire le bateau coulé de la liste
                    bateaux_restants.discard(id)

                if self.grille.eq(grille_vide):
                    break
        print("Nombre de coups en version probabiliste : ")
        return nb_coups
