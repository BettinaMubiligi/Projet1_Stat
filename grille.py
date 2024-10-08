import numpy as np
import random
import matplotlib.pyplot as plt

taillebat = {1: 5, 2: 4, 3: 3, 4: 3, 5: 2}


class Grille:

    def __init__(self, nom):
        self.grille = np.zeros((10, 10), dtype=int)
        self.name = nom
        self.liste = []

    def __getvalue__(self, i, j):
        #faut faire -1 car on raisonne de 1 à 10 mais accéder à des cases c'est de 0 à 9
        return self.grille[i - 1][j - 1]

    # Partie 1 : Modelisation et fonctions simples

    def peut_placer(self, bateau, position, direction):
        taille = taillebat[bateau]  #avec son id qui est bateau, on a la taille
        x, y = position  # On suppose que l'utilisateur va rentrer des valeurs entre 1 et 10 et non 0 et 9

        # Placement horizontal
        if direction == 1:
            #cas débordement
            if y + taille > 10:
                print("Position (" + str(x + 1) + "," + str(y + taille + 1) +
                      ") : sort de la grille")
                return False
            #vérifie si les cases sont libres -> 0
            for i in range(taille):
                if self.grille[x - 1][y + i - 1] != 0:
                    print("Position (" + str(x + 1) + "," +
                          str(y + taille + 1) + ") occupée")
                    return False
        # Placement vertical
        elif direction == 2:
            #cas débordement
            if x + taille > 10:
                print("Position (" + str(x + taille + 1) + "," + str(y + 1) +
                      ") : sort de la grille")
                return False
            #vérifier que c'est libre
            for i in range(taille):
                if self.grille[x + i - 1][y - 1] != 0:
                    print("Position (" + str(x + taille + 1) + "," +
                          str(y + 1) + ") occupée")
                    return False
        return True

    def place(self, bateau, position, direction):
        ligne, colonne = position
        if self.peut_placer(bateau, position, direction):
            if direction == 1:
                for i in range(taillebat[bateau]):
                    self.grille[ligne - 1][colonne + i - 1] = bateau
                    self.liste.append((ligne, colonne + i))
            if direction == 2:
                for i in range(taillebat[bateau]):
                    self.grille[ligne + i - 1][colonne - 1] = bateau
                    self.liste.append((ligne + i, colonne))
        return self.grille

    def place_alea(self, bateau):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        dir = random.randint(1, 2)

        while not (self.peut_placer(bateau, (x, y), dir)):
            x = random.randint(1, 10)
            y = random.randint(1, 10)
            dir = random.randint(1, 2)
      
        self.place(bateau, (x, y), dir)

        return self.grille

    def affiche(self):
        plt.imshow(self.grille)
        plt.axis('on')
        plt.title(self.name)
        plt.grid(True)
        plt.xticks(np.arange(0, 10, step=1) - 0.5, np.arange(1, 11))
        plt.yticks(np.arange(0, 10, step=1) - 0.5, np.arange(1, 11))
        plt.show()

    def eq(self, grille):
        for i in range(10):
            for j in range(10):
                if (self.__getvalue__(i, j) != grille.__getvalue__(i, j)):
                    return False
        return True

    def genere_grille(name):
        grille = Grille(name)
        for i in range(1, 6):
            grille.place_alea(i)
        return grille


# Genere une grille de 2 bateaux

    def genere_grille_2(name):
        grille = Grille(name)
        for i in range(1, 3):
            grille.place_alea(i)
        return grille

    def connexe(self, bateau, position):
        """fonction pour connaître toutes les cases d'un bateau 
        en particulier en connaissant seulement une seule de ses cases"""
        x, y = position  #On suppose que les coordonnees sont entre 1 et 10 et non 0 et 9.
        x -= 1
        y -= 1
        cases_bat = set()
        for i in range(10):
            if (self.grille[x][i] == bateau):
                cases_bat.add((x, i))
                self.grille[x][i] = 0
            elif (self.grille[i][y] == bateau):
                cases_bat.add((i, y))
                self.grille[i][y] = 0
        return self

    # Partie 2 : Combinatoire du jeu


def nb_placements_possibles_bateau(id):
    #nb possibilités pour 1 bateau donné dans une grille vide
    grille_vide = Grille("Grille vide")
    taille = taillebat[id]
    return ((np.size(grille_vide.grille, 0) - taille + 1) *
            np.size(grille_vide.grille, 1) * 2)


def nb_placements_possibles_liste_chev(liste_bateaux):
    grille_vide = Grille("Grille vide")
    nb_possibilites = 0
    for bateau in liste_bateaux:
        nb_possibilites += nb_placements_possibles_bateau(bateau)
    return nb_possibilites


def nb_placements_possibles_liste_sans_chev(liste_bateaux):
    grille_vide = Grille("Grille vide")
    if (len(liste_bateaux) == 0):
        return 1
    nb_possibilites = nb_placements_possibles_bateau(liste_bateaux[0])
    dir = 1
    grille_vide.place_alea(liste_bateaux[0])
    for bateau in liste_bateaux[1:]:
        for i in range(10):
            for j in range(10):
                for dir in range(1, 2):
                    if grille_vide.peut_placer(bateau, (i, j), dir):
                        nb_possibilites += 1
        grille_vide.place_alea(bateau)
    return nb_possibilites


#Q4, remarque : la fonction tourne trop longtemps
def grilles_egales(self):
    cpt = 0
    while (not (self.eq(Grille.genere_grille_2("test")))):
        cpt += 1
    print("Nombre de grilles generees : ")
    return cpt


#5: Pas sûres du résultat


def nb_total_grilles(liste_bateaux):
    return nb_placements_possibles_liste_chev(
        liste_bateaux) / nb_placements_possibles_liste_sans_chev(liste_bateaux)


#Pour la Partie 3 : Version probabiliste simplifiée
#Fonction qui prends la matrice avec toutes les probabilités pour chaque bateau et chaque cases en argument et renvoie un ensemble contenant les coordonnées triées selon les probabilités de contenir un bateau à la case correspondante


def coordonnees_triee(mat_total):
    # on cree une liste de tuple de toutes les coordonnées avec leurs valeurs et on la trie
    coordonnees = []
    for i in range(10):
        for j in range(10):
            coordonnees.append((mat_total[i][j], (i, j)))

    for i in range(len(coordonnees)):
        max = i
        for j in range(i + 1, len(coordonnees)):
            if coordonnees[j][0] > coordonnees[max][0]:
                max = j
        coordonnees[i], coordonnees[max] = coordonnees[max], coordonnees[i]

    # on garde seulement les coordonnées (sans les valeurs)
    coordonnees_triee = [coord for _, coord in coordonnees]

    return coordonnees_triee
