# Projet1_Stat

**Rapport de Projet 1 - Emma, Clarisse, Bettina**

**Réponses aux questions**

**Partie 2 - Combinatoire du Jeu**

*Q.1*

Puisque l'on dispose d'une grille de taille 10 * 10 cases, soit 100 cases, on doit regarder le nombre de manières de placer 1 bateau (avec un nombre de cases données) sur une ligne horizontale
puis verticale, sur 10 cases chacune.
Pour placer le bateau 1, le porte-avions, qui prends 5 cases, on enlève le nombre de cases du bateau au nombre total de la ligne et on rajoute 1, soit 10-5+1 = 6, donc il y a 6 manieres de placer le
bateau dans une ligne, fois 10 lignes, fois deux (lignes horizontales et verticales), soit 6 * 10 * 2 = 120 manières de placer le porte-avions dans la grille.
En suivant le même raisonnement pour le reste des bateaux, on obtient pour le bateau 2 (croiseurs) à 4 cases : 7 * 10 * 2= 140,  le bateau 3 (contre-torpilleurs) à 3 cases : 8 * 10 * 2 = 160, de même pour 
 le bateau 4 (sous-marin) à 3 cases, et enfin il y a 9 * 10 * 2 = 180 manières de placer le bateau 5, le torpilleur dans la grille.
 La borne supérieure simple du nombre de configurations possibles pour la liste complète de bateaux sur une grille de taille 10 sera égale à 120 * 140 * 160 * 160 * 180 ce qui est égal à environ 77 milliards de configurations.

*Q.2*

La fonction qui permet de calculer le nombre de façons de placer un bateau donné sur une grille vide est nb_placements_possibles_bateau(id) avec id le numéro du bateau, nous renvoie les même valeurs que celles trouvées lors du calcul théorique, soit 120 pour le bateau 1, 140 pour le bateau 2, 160 pour les bateaux 3 et 4 et 180 pour le bateau 5.

*Q.3*

En implémentant la fonction qui permet de calculer le nombre de façon de placer une liste de bateaux sur une grille vide, on observe que le nombre de placements possible varie selon les chevauchements : pas de chevauchements implique un nombre de placements inférieur à au cas où ils seraient permis. Ce nombre dépend également de la taille des bateaux de la liste. 

*Q.4*

La probabilité de tirer une grille donnée = 1 / le nombre de grilles total si on considère toutes les grilles comme équiprobables. 
Remarque : notre fonction  grilles_egales(grille) qui génère des grilles aléatoirement jusqu’à ce que la grille générée soit égale à la grille passée en paramètre a un temps d'exécution très élevé si on prends des grilles contenant plus de 3 bateaux.

*Q.5*

D'après la question 4), le nombre de grilles total pour une liste de bateaux = 1/ la probabilité de tirer une grille donnée pour cette liste de bateaux, approximativement.
Pour trouver cette probabilité, il faut calculer le nombre de grilles valides générées avec la liste de bateaux / le nombre d'essais total.
Donc le nombre de grilles total = nb essais total/nb grilles valides générées.
Ici, les grilles 'valides' sont les grilles possibles, sans débordements et chevauchements, soit les grilles pour lesquelles la foncion peut_placer(grille, bateau, position, direction) était à true pour tous les bateaux de la liste. 


**Partie 3 - Modélisation probabiliste du jeu**

*Version aléatoire*

Nos hypothèses sont les suivantes pour le calcul l’espérance du nombre de coups joués avant de couler tous les bateaux si chaque coup est tiré aléatoirement :
- Il y a un bateau de chaque taille dans la grille
- La grille est de taille 10*10 soit 100 cases
- Il n'y a pas de chevauchements possibles entre les cases des bateaux
- Une case touchée l'est définitivement

  On pose une variable aléatoire X comptant le nombre d'épreuves de Bernoulli dépendantes (le nombre de coups joués ) de probabilité de succès p ∈ ]0,1[ chacunes , X permet donc de compter le nombre de coups nécessaires pour couler tous les bateaux de la grille, soit le nombre de coups pour toucher chaque case de la grille contenant un bateau. X est donc une somme de Xi, avec i le nombre de coups joués.
  Ces Xi suivent une loi géométrique de paramètre p, p étant la probabilité de toucher une case contenant un bateau,  avec donc une espérance E = 1/p.
  
  Il y a au total 5+4+3+3+2 = 17 cases occupées sur 100 qui contienent un bateau.
  Au premier coup, on aura 17 cases réellement occupées par un bateau sur 100 cases possibles, soit la probabilité p de toucher une case contenant un bateau pour X1 est p(X1) = 17/100 puis au second coup, il nous restera 16 cases réellement occupées sur 99 cases possibles, soit p(X2) = 16/99 puis p(X3) = 15/98 pour le troisième coup, etc, jusqu'à ce qu'il nous reste 1 case contenant un bateau sur 84 possibles, soit p(X=17)= 84/1.
  
  Ce qui nous donne une espérance E (X1)= 100/17 = 0.17 pour le premier coup, E (X2)= 99/16 pour le deuxième, etc.
  Donc l'espérance de E[X] = somme des espérances soit 100/17 + 99/16+ 98/15 etc ( environ 294)
  


*Version heuristique*

*Version probabiliste simplifiée*

**Partie 4 - Senseur Imparfait: à la recherche de l’USS Scorpion**

*Q.1* La loi de probabilite pour Y=1 est 1/N car il y a une seule case sur les N du quadrillage qui contient l'objet. La loi de probabilite pour Y=0 est N-1/N (ou 1-(1/N)) car le reste des N cases du quadrillage est vide.

Selon l'enonce de la partie 4, voici ce qu'il vient pour la loi de probabilite de Zi|Yi : 
 - p(Z=0|Y=0) = p(Z=0^Y=0)/p(Y=0) = 1
 - p(Z=1|Y=0) = p(Z=1^Y=0)/p(Y=0) = 0
 - p(Z=0|Y=1) = p(Z=0^Y=1)/p(Y=0) = 1-ps
 - p(Z=1|Y=1) = p(Z=1^Y=1)/p(Y=0) = ps


*Q.2* Dans le cas ou la detection n'a pas fonctionnee (Zk=0) alors que l'objet s'y trouvait (Yk=1), on peut exprimer la probabilite de la maniere suivante :
 p(Z=0|Y=1) = p(Z=0^Y=1)/p(Y=0) = 1-ps ?

*Q.3* 

πk = 

*Q.4* Pour πk, on met sa valeur a 0 et on augmente la probabilite sur toutes les autres cases car il y a une case en moins parmi les N dans laquelle l'objet aurait pu se trouver. Ce qui donne πi = 1/(N-nb_cases_zero)



