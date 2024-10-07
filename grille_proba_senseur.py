import math
import numpy as np

def grille_proba_init(N):
    grille=np.zeros((math.isqrt(N), math.isqrt(N)), dtype=float)
    for i in range (math.isqrt(N)):
      for j in range (math.isqrt(N)):
        grille[i][j]=1/N #On met a jour la probabilite sur toutes les cases
    return grille
  
def grille_proba_maj(grille, position, N):
    x, y = position
    grille[x][y] = 0 # On elimine la case visitee (qui n'est pas egale a 1 donc qui ne contient pas l'objet)
    cpt_non_zero = np.count_nonzero(grille) # Compte le nombre de cases qui ne sont pas egales a 0
    if cpt_non_zero > 0:
        for i in range(math.isqrt(N)):
            for j in range(math.isqrt(N)):
                if grille[i][j] != 0: # Si la case n'est pas deja visitee, on maj sa probabilite
                    grille[i][j] = 1/cpt_non_zero 
    return grille