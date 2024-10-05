from grille import *
from bataille import *
import numpy as np
"""
g1 = Grille("grille1")
g2 = Grille("grille2")
g3 = Grille.genere_grille("grille 3")
"""
#grille.place(4,(4,5),1)
#print(grille.grille)
"""
g1.place(5, (2, 3), 2)
g2.place(5, (2, 3), 2)

g1.place(4, (1, 4), 1)
g2.place(4, (1, 4), 1)
"""
#g1.place_alea(2)
"""
print(g2.grille)

print(g1.eq(g2))

print(g2.liste)
"""
#print(g3.grille)

#print(g1.__getvalue__(2,3))

#g1.affiche()
""" print("----------")

print(grille.place_alea(2))

print("----------")


#grille1=Grille("grille 1")


#grille1.place(4,(4,5),1)
#grille1.place(5,(2,3),2)

#print(grille1.grille)
#print("----------")

#print(grille.eq(grille1))
print("----------")

#print(Grille.genere_grille().grille)

#grille.affiche()

grille2 = Grille.genere_grille("grille 2")
#print(grille2.grille)

grille2.affiche()

#print(peut_placer(grille,5,(5,8),1))
#print(peut_placer(grille,5,(2,3),1))

#grille1 = place(grille,4,(4,5),1)
#grille = place(grille,3,(3,8),2)
print("------------------")
print(nb_placements_possibles_bateau(5))

print("----------------")
print ("Nb placements possibles : " + str(nb_placements_possibles_liste_sans_chev([1,4,5])))
"""
grille2 = Grille.genere_grille_2("grille 2")
#print(grille2.grille)
grille2.affiche()
print("----------------")
print(grilles_egales(grille2))
"""
print(Bataille.genere_mat_nb_possibilites(1))
print("----------------")
print(Bataille.genere_mat_nb_possibilites(2))
print("----------------")
print(Bataille.genere_mat_nb_possibilites(3))
print("----------------")
print(Bataille.genere_mat_nb_possibilites(4))
print("----------------")
print(Bataille.genere_mat_nb_possibilites(5))
"""
""" b1 = Bataille("bat")
liste_bateau = [1, 2, 3, 4, 5]
print(b1.joue_proba_simplifiee(liste_bateau))"""
#print(place(grille,4,(4,5),1))
#print("----------------")
#print(place(grille,3,(3,8),2))
#print("----------------")

#print(place(grille,3,(3,8),2))
liste_bateau = [1, 2, 3, 4, 5]
print(str(nb_total_grilles(liste_bateau)))
"""
bat_test = Bataille("Bataille test")
bat_test.grille.affiche()
print(bat_test.joue_aleatoire())
bat_test.grille.affiche()

print(bat_test.joue_proba_simplifiee(liste_bateau))
bat_test.grille.affiche()"""
