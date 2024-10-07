from grille_proba_senseur import *
import numpy as np
import math
import random
import matplotlib.pyplot as plt

# Partie 4 : Senseur imparfait : a la recherche de l'USS Scorpion

class Senseur :
  def __init__(self,N):
    self.N=N
    self.quadrillage=np.zeros((math.isqrt(N),math.isqrt(N)), dtype=int) # On suppose N, carre parfait, pour avoir le bon nombre de cases

  def place_objet_perdu(self):
    x = random.randint(0, math.isqrt(self.N)-1) #On va de 0 a N exclus pour ne pas sortir de la grille.
    y = random.randint(0, math.isqrt(self.N)-1)

    self.quadrillage[x][y]=1 # On place l'objet perdu parmi les N cases

    return self

  def cherche_objet_perdu(self):
    grille_proba=grille_proba_init(self.N)
    xmax, ymax = np.unravel_index(grille_proba.argmax(), grille_proba.shape) #On recupere la position de la probabilite la plus haute
    while(self.quadrillage[xmax][ymax]!=1):
      grille_proba_maj(grille_proba, (xmax, ymax), self.N)
      xmax, ymax = np.unravel_index(grille_proba.argmax(), grille_proba.shape)

    index = xmax*math.isqrt(self.N)+ymax+1
    print ("L'objet se trouvait a la case "+str(index))
    return index

    




    

    


    
    
