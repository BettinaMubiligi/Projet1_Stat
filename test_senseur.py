from senseur import *

s1 = Senseur(100)

s1.place_objet_perdu()
print(s1.quadrillage)
print("-----------")

s1.cherche_objet_perdu_parcours_case_a_case()
print("-----------")
s1.cherche_objet_perdu_parcours_milieu()
print("-----------")
s1.cherche_objet_perdu_parcours_bord()
