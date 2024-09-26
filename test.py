from grille import *
from bataille import *
import numpy as np

grille=Grille("grille")


#grille.place(4,(4,5),1)
#print(grille.grille)


grille.place(5,(2,3),2)
print(grille.grille)

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

print("----------------")
print(grilles_egales(grille2))

#print(place(grille,4,(4,5),1))
#print("----------------")
#print(place(grille,3,(3,8),2))
#print("----------------")

#print(place(grille,3,(3,8),2))
 """

bat_test = Bataille("Bataille test")
bat_test.grille.affiche()
print(bat_test.joue_heuristique())
bat_test.grille.affiche()
