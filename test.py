from grille import *
from bataille import *
import numpy as np

#Partie 1 : Modelisation et fonctions simples
print("Partie 1")
g1 = Grille.genere_grille("grille 1")
g2 = Grille.genere_grille("grille 2")

print(g1.grille)
print(g2.grille)
print(g1.eq(g2))
g1.affiche()
g2.affiche()

#Partie 2 : Combinatoire du jeu
print("Partie 2")

print("------------------------------")

print("Nb de placeents possible d'un bateau dans une grille: " +
      str(nb_placements_possibles_bateau(5)))
print("------------------------------")

print("Nb placements possibles sans chevauchements: " +
      str(nb_placements_possibles_liste_sans_chev([1, 2, 3, 4, 5])))
print("------------------------------")

print("Nb placements possibles avec chevauchements: " +
      str(nb_placements_possibles_liste_chev([1, 2, 3, 4, 5])))
print("------------------------------")

print(
    "Approximation du nombre de grilles pour la liste avec la probabilité: " +
    str(nb_total_grilles([1, 2, 3, 4, 5])))
print("------------------------------")
#Q4, remarque : la fonction tourne trop longtemps
#print(grilles_egales(g2))

print("------------------------------")

liste_bateau = [1, 2, 3, 4, 5]
#print(str(nb_total_grilles(liste_bateau)))
"""
#Partie 3 : Modélisations probabiliste du jeu
print("Partie 3")

b1 = Bataille("bat1")
b1.grille.affiche()
liste_bateau = [1, 2, 3, 4, 5]
#Version aléatoire
print(str(b1.joue_aleatoire()))
b1.grille.affiche()

#Version Heuristique

b2 = Bataille("bat2")
b2.grille.affiche()
print(b2.joue_aleatoire())
b2.grille.affiche()

#Version probabiliste simplifiée

print(Bataille.genere_mat_nb_possibilites(1))
print("-------------------------------------")
print(Bataille.genere_mat_nb_possibilites(2))
print("--------------------------------------")
print(Bataille.genere_mat_nb_possibilites(3))
print("-------------------------------------")
print(Bataille.genere_mat_nb_possibilites(4))
print("-------------------------------------")
print(Bataille.genere_mat_nb_possibilites(5))
print("-------------------------------------")

b3 = Bataille("bat3")
print(b3.joue_proba_simplifiee(liste_bateau))
b3.grille.affiche()
"""
