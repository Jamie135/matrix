# Vector

Ce document résume les opérations vectorielles implémentées dans [`vector.py`](../vector.py), [`ex01.py`](../ex01.py), [`ex02.py`](../ex02.py), [`ex05.py`](../ex05.py) et [`ex06.py`](../ex06.py), avec ce que chacune représente géométriquement.

## `add` / `sub` / `scl` — vector.py

Un vecteur est une flèche partant de l'origine.
- **`add`** : on place la queue du second vecteur sur la pointe du premier, la flèche résultante va de l'origine à la pointe finale (règle du parallélogramme).
- **`sub`** : donne la flèche qui va de la pointe de `v` vers la pointe de `u` — c'est le déplacement entre les deux points.
- **`scl`** : étire (`|a|>1`), rétrécit (`|a|<1`) ou inverse (`a<0`) le vecteur le long de sa propre droite, sans changer sa direction sinon.

## Combinaison linéaire — ex01.py

`linear_combination(u, coefs)` = on met à l'échelle chaque vecteur puis on les additionne tous. Géométriquement : on choisit un ensemble de « directions » (les vecteurs `u`) et on avance de distances différentes le long de chacune — le point d'arrivée est la combinaison. Avec la base standard `e1, e2, e3`, la combinaison `[10, -2, 0.5]` correspond exactement au point `(10, -2, 0.5)` — c'est le principe même de l'expression des coordonnées d'un vecteur dans une base.

## Interpolation linéaire (lerp) — ex02.py

`lerp(u, v, t) = u*(1-t) + v*t` parcourt le segment de droite reliant le point `u` au point `v`, paramétré par `t`. `t=0` donne `u`, `t=1` donne `v`, `t=0.5` donne le milieu. C'est un cas particulier de combinaison linéaire où les deux coefficients somment toujours à 1 — cette contrainte est ce qui garde le résultat *sur la droite* entre les deux points, plutôt que n'importe où dans le plan qu'ils engendrent.

## Produit scalaire (dot product) — vector.py

`u.dot(v) = Σ uᵢ·conj(vᵢ)`. Géométriquement, `u·v = |u||v|cos(θ)` — cela mesure à quel point `u` et `v` pointent dans la même direction, à l'échelle de leurs longueurs. Le signe indique la relation :
- positif → angle < 90° (direction globalement similaire)
- zéro → perpendiculaires
- négatif → angle > 90° (direction globalement opposée)

Autre image utile : `u·v` est `|u|` fois la *longueur signée de la projection de v sur u*. Le conjugué appliqué à `v` (fonction `_conj`) garantit que `u.dot(u)` reste toujours un réel non négatif, même pour des vecteurs à valeurs complexes — sinon la notion de « longueur » n'aurait pas de sens.

## Les trois normes — vector.py

Les trois répondent à « quelle est la taille de ce vecteur ? » mais définissent « taille » différemment — on peut se représenter la *boule unité* (l'ensemble des vecteurs de norme 1) pour chacune :

- **`norm_1`** (Manhattan/taxicab) : somme des `|coordonnée|`. C'est la distance si on ne peut se déplacer que le long des axes (comme marcher dans une ville en quadrillage). Boule unité = losange.
- **`norm`** (Euclidienne, `sqrt(dot(u,u))`) : distance « à vol d'oiseau », celle qu'on mesurerait avec une règle. Boule unité = cercle/sphère.
- **`norm_inf`** (norme sup) : la magnitude de la plus grande coordonnée seule. Boule unité = carré (aligné sur les axes). Répond à « dans la pire direction unique, jusqu'où faut-il aller ? »

Ces trois normes sont toujours ordonnées : `norm_inf ≤ norm ≤ norm_1`.

## Cosinus — ex05.py

`angle_cos(u,v) = u·v / (|u||v|)` isole directement le `cos(θ)` de la formule du produit scalaire ci-dessus — on retire les longueurs et il ne reste que la relation *directionnelle* : `1` = même direction, `0` = perpendiculaires, `-1` = direction opposée. C'est pourquoi `angle_cos(Vector([2,1]), Vector([4,2]))` donne exactement `1.0` : `(4,2)` est simplement `(2,1)` mis à l'échelle, même direction, donc le cosinus indique « direction identique » indépendamment de la différence de longueur.

## Produit vectoriel (cross product) — ex06.py

Défini uniquement en 3D. `u × v` produit un *nouveau vecteur*, pas un scalaire, avec deux propriétés géométriques :
1. **Direction** : perpendiculaire à `u` et à `v` (normale au plan qu'ils engendrent), selon la règle de la main droite.
2. **Magnitude** : `|u×v| = |u||v|sin(θ)`, qui est égale à l'*aire du parallélogramme* formé par `u` et `v`.

Ainsi `cross_product(Vector([0,0,1]), Vector([1,0,0]))` donnant `[0,1,0]` a du sens : `axe-z × axe-x = axe-y` (règle de la main droite), et comme ce sont des vecteurs unitaires perpendiculaires, le parallélogramme est un carré unité, d'aire 1. Quand `u` et `v` sont parallèles (par exemple `[1,1,1]` × `[1,1,1]`), le « parallélogramme » s'effondre en une ligne — aire nulle — d'où le vecteur nul en résultat.
