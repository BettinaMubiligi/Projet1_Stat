from grille import *
from bataille import *
import numpy as np

#Partie 1 : Modelisation et fonctions simples
liste_bateau = [1, 2, 3, 4, 5]

print("Partie 1")
g1 = Grille.genere_grille("grille 1")
g2 = Grille.genere_grille("grille 2")
g3 = Grille.genere_grille_2("grille 3")

print(g1.grille)
print("-------------------------------------")

print(g2.grille)
print("-------------------------------------")

print(g1.eq(g2))

#Partie 2 : Combinatoire du jeu
print("Partie 2")

#Q4, remarque : la fonction tourne trop longtemps quand la longueur de la liste de bateaux dépasse 3 bateaux
print(grilles_egales(g3))

print("------------------------------")

#Q2
print("Nb de placements possible de ce bateau dans une grille: " +
      str(nb_placements_possibles_bateau(5)))
print("------------------------------")

#Q3
print("Nb placements possibles sans chevauchements: " +
      str(nb_placements_possibles_liste_sans_chev([1, 2, 3, 4, 5])))
print("------------------------------")

print("Nb placements possibles avec chevauchements: " +
      str(nb_placements_possibles_liste_chev([1, 2, 3, 4, 5])))
print("------------------------------")

#Q5 - Pas sûres du résultat
print(
    "Approximation du nombre de grilles pour la liste avec la probabilité: " +
    str(nb_total_grilles([1, 2, 3, 4, 5])))
print("------------------------------")

#Partie 3 : Modélisations probabiliste du jeu
print("Partie 3")
#Version aléatoire

b1 = Bataille("bat1")
b1.grille.affiche()
#print(str(b1.joue_aleatoire()))
b1.affiche_mat_nbTirs_aleatoire()
#Version Heuristique

b2 = Bataille("bat2")
b2.grille.affiche()
b2.affiche_mat_nbTirs_heuristique()

#Version probabiliste simplifiée

#Matrices contenant les probabilités de présence d'un bateau pour chaque bateau et chaque case
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
b3.grille.affiche()
b3.affiche_mat_nbTirs_probabiliste(liste_bateau)

# Exemple de test des simulations - complémentaire:
"""
b4 = Bataille("grille 4")
Bataille.simulation_distribution(1000)

b5 = Bataille("grille 5")
Bataille.simulation_distribution_heuristique(1000)

b6 = Bataille("grille 6")
Bataille.simulation_distribution_probabiliste(1000)
"""
