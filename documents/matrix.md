# Matrix

Ce document résume l'implémentation d'une classe `Matrix` générique (module `matrix/matrix.py`), avec les opérations classiques d'algèbre linéaire : addition, soustraction, mise à l'échelle, multiplication, trace, transposée, forme échelonnée réduite, déterminant, inverse et rang.

## Vue d'ensemble géométrique

Une matrice représente une transformation linéaire de l'espace. Chaque opération ci-dessous peut se lire aussi bien comme un calcul algébrique que comme une action géométrique sur cet espace.

### Trace
Somme des éléments de la diagonale d'une matrice carrée.

**Sens géométrique :** elle mesure le taux de variation infinitésimal du volume induit par la transformation — c'est la dérivée du déterminant au voisinage de l'identité. Elle correspond aussi à la somme des valeurs propres : une indication de l'expansion nette que la transformation produit selon les directions qu'elle étire ou compresse.

### Transposée
Échange lignes et colonnes : `Mᵀ[i][j] = M[j][i]`.

**Sens géométrique :** si `M` envoie des vecteurs d'un espace vers un autre, `Mᵀ` agit dans la direction opposée entre les espaces duaux (elle transforme la façon dont `M` agit sur les vecteurs en la façon dont elle agit sur les formes linéaires/covecteurs). Elle est essentielle pour les matrices orthogonales (rotations, réflexions), où `Mᵀ = M⁻¹`.

### Forme échelonnée (réduite)
Obtenue par élimination de Gauss-Jordan : la matrice est réduite en escalier, avec des pivots à 1 et des zéros ailleurs dans les colonnes pivots.

**Sens géométrique :** chaque ligne représente une contrainte linéaire (un hyperplan). Les opérations sur les lignes ne changent ni l'ensemble des solutions du système, ni l'espace engendré par les lignes — elles simplifient seulement la description, révélant le nombre de contraintes réellement indépendantes.

### Déterminant
Calculé ici par décomposition de type LU (réduction en matrice triangulaire supérieure, produit de la diagonale, correction du signe selon les permutations de lignes).

**Sens géométrique :** le facteur d'échelle **signé** du volume induit par la transformation. Le cube unité, une fois transformé, a un volume `|det(M)|`. Le signe indique si l'orientation de l'espace est préservée (positif) ou inversée, comme un miroir (négatif). Un déterminant nul signifie que la transformation écrase l'espace dans une dimension inférieure (plan, droite ou point).

### Inverse
Calculé par élimination de Gauss-Jordan sur la matrice augmentée `[A | I]`, en réduisant `A` vers `I` pendant que les mêmes opérations transforment `I` en `A⁻¹`. Nécessite `det(A) ≠ 0`.

**Sens géométrique :** la transformation qui annule exactement l'effet de `M`. Elle n'existe que si `M` ne fait perdre aucune dimension (déterminant non nul) — on ne peut pas « annuler » un écrasement de l'espace, car de l'information (une dimension entière) a été perdue.

### Rang
Obtenu en réduisant la matrice sous forme échelonnée puis en comptant les lignes non nulles.

**Sens géométrique :** la dimension de l'espace réellement engendré par l'image de la transformation (nombre de directions indépendantes parmi les lignes/colonnes). Une matrice carrée de rang plein transforme l'espace en un espace de même dimension (elle est inversible) ; une matrice de rang déficient écrase l'espace dans un sous-espace de dimension inférieure.

## Lien entre ces notions

Trace et déterminant se déduisent tous deux des valeurs propres (respectivement somme et produit) et décrivent **comment** une transformation déforme l'espace. Le rang et la forme échelonnée décrivent **combien** de dimensions survivent à cette transformation. Un déterminant non nul est précisément la condition pour que le rang soit plein et que l'inverse existe — trois façons différentes de dire qu'aucune dimension n'est perdue.
