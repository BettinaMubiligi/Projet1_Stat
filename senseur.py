from grille_proba_senseur import *
import numpy as np
import math
import random
import matplotlib.pyplot as plt

# Partie 4 : Senseur imparfait : a la recherche de l'USS Scorpion

class Senseur :
  def __init__(self,N):
    if (math.isqrt(N)**2!=N or N<=0):
      raise ValueError("N n'est pas un carre parfait ou N n'est pas un entier strictement positif")
    self.N=N
    self.quadrillage=np.zeros((math.isqrt(N),math.isqrt(N)), dtype=int)

  def place_objet_perdu(self):
    x = random.randint(0, math.isqrt(self.N)-1) #On va de 0 a N exclus pour ne pas sortir de la grille.
    y = random.randint(0, math.isqrt(self.N)-1)

    self.quadrillage[x][y]=1 # On place l'objet perdu parmi les N cases

    return self

  def cherche_objet_perdu_parcours_case_a_case(self):
    """Fonction qui parcourt la grille de 1 a N jusqu'a retrouver l'objet perdu"""
    grille_proba=grille_proba_init(self.N)
    xmax, ymax = np.unravel_index(grille_proba.argmax(), grille_proba.shape) #On recupere la position de la probabilite la plus haute
    cpt_maj_grille_proba=0
    while(self.quadrillage[xmax][ymax]!=1):
      grille_proba_maj(grille_proba, (xmax, ymax), self.N)
      xmax, ymax = np.unravel_index(grille_proba.argmax(), grille_proba.shape)
      cpt_maj_grille_proba+=1

    index = xmax*math.isqrt(self.N)+ymax+1
    print ("L'objet se trouvait a la case "+str(index)+" et a ete trouve au bout de "+str(cpt_maj_grille_proba) + " essais en parcourant de 1 a N.")
    return index

  def cherche_objet_perdu_parcours_milieu(self):
    """Fonction qui parcourt la grille depuis le centre jusqu'a ce qu'on retrouve l'objet perdu"""
    grille_proba=grille_proba_init(self.N)
    x_centre = math.isqrt(self.N)//2
    y_centre = math.isqrt(self.N)//2
    cpt_maj_grille_proba=0
    deplacements_possibles=[(0,0)]

    for d in range (1, math.isqrt(self.N)):
      for deplacement_x in range (-d, d+1): # Deplacement sur les colonnes
        deplacements_possibles.append((deplacement_x,d)) 
        if deplacement_x!=-d:
          deplacements_possibles.append((deplacement_x, -d))
      for deplacement_y in range (-d+1, d) : #Deplacement sur les lignes
        deplacements_possibles.append((d, deplacement_y))  
        deplacements_possibles.append((-d, deplacement_y)) 

    for dir_x, dir_y in deplacements_possibles :
      x,y = x_centre+dir_x, y_centre+dir_y
      if (0 <= x < math.isqrt(self.N)) and (0 <= y < math.isqrt(self.N)) :
        grille_proba_maj(grille_proba, (x,y), self.N)
        cpt_maj_grille_proba+=1

        if self.quadrillage[x][y]==1:
          index = x*math.isqrt(self.N)+y+1
          print ("L'objet se trouvait a la case "+str(index)+" et a ete trouve au bout de "+str(cpt_maj_grille_proba) + " essais en parcourant depuis le milieu.")
          return index
  
  def cherche_objet_perdu_parcours_bord(self):
    """Fonction qui parcourt la grille en partant de la case en haut a gauche en escargot (donc parcours des bords) jusqu'a retrouver l'objet perdu"""
    grille_proba = grille_proba_init(self.N)
    cpt_maj_grille_proba = 0

    haut, bas, gauche, droite = 0, math.isqrt(self.N)-1, 0, math.isqrt(self.N)-1

    while haut <= bas and gauche <= droite:
        # Parcours de gauche a droite en haut
        for x in range(gauche, droite + 1):
            grille_proba_maj(grille_proba, (haut, x), self.N)
            cpt_maj_grille_proba += 1
            if self.quadrillage[haut][x] == 1:
                index = haut * math.isqrt(self.N) + x + 1
                print("L'objet se trouvait à la case " + str(index) + " et a été trouvé au bout de " + str(cpt_maj_grille_proba) + " essais en parcourant depuis les bords.")
                return index
        haut+=1

        # Parcours de haut en bas a droite
        for y in range(haut, bas + 1):
            grille_proba_maj(grille_proba, (y, droite), self.N)
            cpt_maj_grille_proba += 1
            if self.quadrillage[y][droite] == 1:
                index = y * math.isqrt(self.N) + droite + 1
                print("L'objet se trouvait à la case " + str(index) + " et a été trouvé au bout de " + str(cpt_maj_grille_proba) + " essais en parcourant depuis les bords.")
                return index
        droite -= 1

        if haut <= bas:
            # Parcours de droite a gauche en bas
            for x in range(droite, gauche - 1, -1):
                grille_proba_maj(grille_proba, (bas, x), self.N)
                cpt_maj_grille_proba += 1
                if self.quadrillage[bas][x] == 1:
                    index = bas * math.isqrt(self.N) + x + 1
                    print("L'objet se trouvait à la case " + str(index) + " et a été trouvé au bout de " + str(cpt_maj_grille_proba) + " essais en parcourant depuis les bords.")
                    return index
            bas -= 1

        if gauche <= droite:
            # Parcours de bas en haut a gauche
            for y in range(bas, haut - 1, -1):
                grille_proba_maj(grille_proba, (y, gauche), self.N)
                cpt_maj_grille_proba += 1
                if self.quadrillage[y][gauche] == 1:
                    index = y * math.isqrt(self.N) + gauche + 1
                    print("L'objet se trouvait à la case " + str(index) + " et a été trouvé au bout de " + str(cpt_maj_grille_proba) + " essais en parcourant depuis les bords.")
                    return index
            gauche += 1
