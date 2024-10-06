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
Remarque : notre fonction  grilles_egales(grille)   qui génère des grilles aléatoirement jusqu’à ce que la grille générée soit égale à la grille passée en paramètre a un temps d'exécution très élevé.

*Q.5*
D'après la question 4), le nombre de grilles total pour une liste de bateaux = 1/ la probabilité de tirer une grille donnée pour cette liste de bateaux.
Pour trouver cette probabilité, il faut calculer le nombre de grilles valides générées avec la liste de bateaux / le nombre d'essais total.
Ici, les grilles 'valides' sont les grilles possibles, sans débordement et chevauchements, soit les grilles pour lesquelles la foncion peut_placer(grille, bateau, position, direction) était à true pour tous les bateaux de la liste.







