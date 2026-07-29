# Fonctions

Ce document résume les fonctions abordées dans chaque exercice.

## `add` / `sub` / `scl` (vector.py)

Un vecteur est une flèche partant de l'origine.

- **`add`** ([vector.py:52-62](../vector.py#L52-L62)) : additionne les deux vecteurs coordonnée par coordonnée, en place (`self._value[i] += v.value[i]`). Géométriquement, on place la queue du second vecteur sur la pointe du premier ; la flèche résultante va de l'origine à la pointe finale (règle du parallélogramme).
- **`sub`** ([vector.py:64-72](../vector.py#L64-L72)) : même principe avec une soustraction (`-=`). Donne la flèche qui va de la pointe de `v` vers la pointe de `u` — c'est le déplacement entre les deux points.
- **`scl`** ([vector.py:74-78](../vector.py#L74-L78)) : multiplie chaque coordonnée par le scalaire `a` (`self._value[i] *= a`). Étire (`|a|>1`), rétrécit (`|a|<1`) ou inverse (`a<0`) le vecteur le long de sa propre droite, sans changer sa direction sinon.

Les trois vérifient d'abord que les tailles (et pour `add`/`sub`, les types) correspondent, et s'exécutent en O(n) temps / O(1) espace puisqu'elles modifient `self` en place plutôt que d'allouer un nouveau vecteur.

## Combinaison linéaire — `linear_combination` (ex01.py)

`linear_combination(u, coefs)` met à l'échelle chaque vecteur de `u` par le coefficient correspondant dans `coefs`, puis additionne le tout, coordonnée par coordonnée (via `fma`, un multiply-add maison : `a*b + c`).

- Vérifie que les listes ne sont pas vides, ont la même longueur, et que tous les vecteurs ont la même taille.
- Boucle externe sur les coordonnées `i` (0 à `size()-1`), boucle interne sur les vecteurs `j` : accumule `vector.value[i] * coefs[j]` pour chaque vecteur, donnant la coordonnée `i` du résultat.
- Complexité temps O(m×n) (m vecteurs, n coordonnées), espace O(n) (le résultat).

Géométriquement : on choisit des « directions » (les vecteurs de `u`) et on avance de distances différentes le long de chacune — le point d'arrivée est la combinaison. Avec la base standard `e1, e2, e3`, la combinaison `[10, -2, 0.5]` donne exactement le point `(10, -2, 0.5)` : c'est le principe même de l'expression des coordonnées d'un vecteur dans une base.

## Interpolation linéaire — `lerp` (ex02.py)

`lerp(u, v, t) = u*(1-t) + v*t`, générique : fonctionne sur des scalaires (`int`/`float`) et sur des `Vector`/`Matrix`.

- Vérifie que `u` et `v` sont du même type (sinon `TypeError`), et pour les Vector/Matrix, de même taille et même type d'éléments (sinon `ValueError`).
- Cas Vector/Matrix : modifie `u` **en place**, élément par élément — `u.value[i] = u.value[i]*(1-t) + v.value[i]*t`.
- Cas scalaire : calcule et retourne une nouvelle valeur, sans toucher à `u`.
- Point à noter : cette asymétrie (mutation en place pour Vector/Matrix, calcul pur pour les scalaires) peut surprendre un appelant qui attend une fonction sans effet de bord.

Géométriquement, `lerp` parcourt le segment de droite reliant `u` à `v`, paramétré par `t` : `t=0` donne `u`, `t=1` donne `v`, `t=0.5` le milieu. C'est un cas particulier de combinaison linéaire où les deux coefficients somment toujours à 1 — c'est cette contrainte qui garde le résultat *sur la droite* entre les deux points plutôt que n'importe où dans le plan qu'ils engendrent.

## Conjugué et produit scalaire — `_conj` / `dot` (vector.py)

`_conj(x)` appelle `x.conjugate()` si la méthode existe (cas `Complex` : flip du signe de la partie imaginaire), sinon renvoie `x` inchangé (no-op sur `int`/`float`).

`dot(v)` calcule `Σ uᵢ·conj(vᵢ)` plutôt que `Σ uᵢ·vᵢ`. Sur les réels le conjugué est un no-op, donc la formule redevient le produit scalaire classique. Sur les complexes, ce conjugué est nécessaire : sans lui, `v.dot(v)` pourrait être négatif ou non réel (ex : `v=[i]` donnerait `i*i=-1`), ce qui rendrait la notion de « longueur au carré » incohérente. Avec le conjugué, `v.dot(v)` est toujours réel et non négatif — d'où son usage dans `norm()` pour pouvoir en prendre la racine carrée en toute sécurité.

## Les trois normes — vector.py

- **`norm_1`** (Manhattan/taxicab) : `Σ |xᵢ|`, somme des magnitudes des coordonnées.
- **`norm`** (Euclidienne) : `sqrt(dot(self, self))` — utilise `_to_real` pour extraire la partie réelle avant la racine carrée, nécessaire car `dot` peut renvoyer un type `Complex`.
- **`norm_inf`** (sup) : `max(|xᵢ|)`, la magnitude de la plus grande coordonnée seule.

Toujours ordonnées : `norm_inf ≤ norm ≤ norm_1`.

## Cosinus — `angle_cos` (ex05.py)

`angle_cos(u, v) = u.dot(v) / (u.norm() * v.norm())` isole directement le `cos(θ)` de la formule du produit scalaire (`u·v = |u||v|cos(θ)`) — en divisant par les deux longueurs, il ne reste que la relation *directionnelle* : `1` = même direction, `0` = perpendiculaires, `-1` = direction opposée.

- Vérifie que `u` et `v` sont bien des `Vector`, et qu'aucun des deux n'est le vecteur nul ([ex05.py:14-15](../ex05.py#L14-L15)) — sinon la division par une norme nulle serait indéfinie.
- C'est pourquoi `angle_cos(Vector([2,1]), Vector([4,2]))` donne exactement `1.0` : `(4,2)` est simplement `(2,1)` mis à l'échelle, même direction, donc le cosinus indique « direction identique » indépendamment de la différence de longueur.
- Complexité O(n) temps (dominée par `dot`/`norm`), O(1) espace propre à la fonction.

## Produit vectoriel — `cross_product` (ex06.py)

Défini uniquement en 3D ([ex06.py:15](../ex06.py#L15) : vérifie que les deux vecteurs ont exactement 3 dimensions). `u × v` produit un **nouveau vecteur**, pas un scalaire, avec deux propriétés géométriques :

1. **Direction** : perpendiculaire à `u` et à `v` (normale au plan qu'ils engendrent), selon la règle de la main droite.
2. **Magnitude** : `|u×v| = |u||v|sin(θ)`, égale à l'*aire du parallélogramme* formé par `u` et `v`.

La formule ([ex06.py:18-21](../ex06.py#L18-L21)) calcule chaque coordonnée du résultat par une combinaison croisée fixe des coordonnées de `u` et `v` (ex : `result[0] = u[1]*v[2] - u[2]*v[1]`) — un nombre d'opérations constant, d'où une complexité O(1) temps et espace.

Ainsi `cross_product(Vector([0,0,1]), Vector([1,0,0]))` donnant `[0,1,0]` a du sens : `axe-z × axe-x = axe-y` (règle de la main droite), et comme ce sont des vecteurs unitaires perpendiculaires, le parallélogramme est un carré unité, d'aire 1. Quand `u` et `v` sont parallèles (par exemple `[1,1,1]` × `[1,1,1]`), le « parallélogramme » s'effondre en une ligne — aire nulle — d'où le vecteur nul en résultat.

## Produit matriciel — matrix.py

Les matrices sont stockées en **liste plate, column-major** ([matrix.py:19-20](../matrix.py#L19-L20)) : tous les éléments de la colonne 0 d'abord, puis colonne 1, etc. `size()` renvoie `(nombre de lignes, nombre total d'éléments)` — donc le nombre de colonnes se calcule par `size()[1] // size()[0]`.

L'élément `(ligne, colonne)` se trouve à l'index plat `colonne * lignes + ligne`. Cette formule revient dans plusieurs fonctions :

- **`mul_mat`** ([matrix.py:106](../matrix.py#L106)) : la boucle externe `for i in range(mat.size()[1] // mat.size()[0])` itère sur chaque **colonne** de `mat`, puisque le produit matriciel produit une colonne de résultat par colonne de `mat`.

## Produit matrice-vecteur — `mul_vec` (matrix.py)

`mul_vec(vec)` ([matrix.py:87-98](../matrix.py#L87-L98)) calcule `self × vec`, produisant un nouveau `Vector`.

- `column = shape[1] // shape[0]` donne le nombre de colonnes de `self` ; vérifie que `vec` a bien cette taille (sinon `ValueError`) — le nombre de colonnes de la matrice doit correspondre au nombre de coordonnées du vecteur.
- Boucle externe `i` sur les lignes de `self` (0 à `size()[0]-1`) : chaque itération produit une coordonnée du vecteur résultat.
- Boucle interne `j` : `range(i, size()[1], size()[0])` parcourt la ligne `i` en avançant de colonne en colonne (stride = nombre de lignes, cohérent avec le stockage column-major), en accumulant `self.value[j] * vec.value[j // size()[0]]` — c'est-à-dire le produit scalaire entre la ligne `i` de `self` et `vec`.
- `result.append(temp_result)` construit la coordonnée `i` du vecteur résultat.
- Complexité au maximum O(n·m) temps et espace (n lignes, m colonnes) — c'est un cas particulier de `mul_mat` où le "second membre" n'a qu'une seule colonne.

Géométriquement, `mul_vec` applique la transformation linéaire représentée par `self` au vecteur `vec` : chaque coordonnée du résultat est la projection de `vec` sur une ligne de la matrice.

## La trace — `trace` (matrix.py)

`trace()` ([matrix.py:118-127](../matrix.py#L118-L127)) additionne les éléments diagonaux d'une matrice **carrée** (sinon `TypeError`, [matrix.py:121-122](../matrix.py#L121-L122)) : `self.value[(i * rows) + i]` pour `i` de `0` à `colonnes-1`.

- La diagonale correspond à `ligne == colonne == i` ; avec la formule d'index column-major `colonne * lignes + ligne`, poser `ligne = colonne = i` donne directement `i * lignes + i`, d'où l'expression du code.
- Complexité O(n) temps (une seule boucle sur la diagonale).

Géométriquement/algébriquement, la trace est invariante par changement de base et intervient par exemple dans le calcul du polynôme caractéristique, ou comme somme des valeurs propres d'une matrice.

## Transposée — `transpose` (matrix.py)

`transpose()` ([matrix.py:130-140](../matrix.py#L130-L140)) construit une nouvelle matrice où lignes et colonnes sont échangées : l'élément `(ligne, colonne)` devient `(colonne, ligne)`.

- Boucle externe `i` sur les colonnes de la matrice d'origine, boucle interne `j` sur les lignes : `self.value[(i * rows) + j]` lit la colonne `i` de haut en bas (grâce au stockage column-major, c'est un accès séquentiel), et l'accumule dans `inner_list`.
- Chaque `inner_list` (une colonne de l'original) est ajoutée à `outer_list` comme une **ligne** — puisque `Matrix()` prend une liste de lignes en entrée ([matrix.py:19-20](../matrix.py#L19-L20)), donner les anciennes colonnes comme nouvelles lignes réalise exactement la transposition.
- Complexité O(n·m) temps et espace (une nouvelle matrice de même taille est construite).

Géométriquement, la transposée reflète la matrice le long de sa diagonale principale ; c'est aussi l'opération qui, combinée au produit scalaire, relie une matrice à son adjointe et intervient dans des propriétés comme la symétrie (`Aᵀ = A`).

## Forme échelonnée réduite — `row_echelon` (matrix.py)

Applique l'élimination de Gauss-Jordan pour obtenir la RREF, en place :

- **`normalize_row(row)`** : parcourt la ligne pour trouver la première colonne non nulle (le pivot), puis divise toute la ligne par cette valeur pour normaliser le pivot à 1.
- **`pivot(row, column, normalized)`** : pour chaque autre ligne ayant une valeur non nulle dans la colonne du pivot, soustrait un multiple de la ligne du pivot pour annuler cette colonne — rendant la forme *réduite* (zéros au-dessus et en dessous de chaque pivot), pas seulement échelonnée.
- Complexité : O(n·m²), soit O(n³) pour une matrice carrée ; espace O(n) (la liste `normalized` est jetée à chaque itération).

## Déterminant — `determinant` (matrix.py)

Calcule le déterminant via élimination de Gauss vers une forme triangulaire supérieure, puis multiplie la diagonale — le déterminant d'une matrice triangulaire est le produit de sa diagonale.

- `row_swap` suit le nombre d'échanges de lignes (chaque échange inverse le signe du déterminant).
- Si un pivot est nul, échange la ligne courante avec la **dernière** ligne de la matrice via `swap_row`.
- Élimine les valeurs en dessous de chaque pivot (opération qui ne change pas le déterminant).
- Résultat final = produit de la diagonale × `row_swap` (ou directement 0 si la diagonale contient un 0, matrice singulière).
- **Limite à noter** : l'échange de pivot nul ne prend que la *dernière* ligne, pas la première ligne disponible avec une valeur non nulle dans cette colonne — si la dernière ligne a aussi un 0 à cet endroit, l'élimination peut échouer (division par zéro).

## Inverse — `inverse` (matrix.py)

Utilise Gauss-Jordan sur la matrice augmentée `[A | I]`, mais représentée ici comme deux tableaux plats parallèles (`self.value` pour `A`, `identity` pour `I`) plutôt qu'une concaténation littérale — chaque opération de ligne est appliquée aux deux en parallèle.

1. Vérifie d'abord que le déterminant n'est pas nul (sinon `TypeError`) — comme `determinant()` modifie `self.value`, une copie est restaurée après l'appel.
2. **Élimination triangulaire inférieure** : même logique que `determinant()`, mais applique aussi chaque opération à `identity`.
3. **Élimination triangulaire supérieure** : même chose en sens inverse (colonnes et lignes décroissantes), annulant les valeurs au-dessus de chaque pivot.
4. **Normalisation des pivots** : divise chaque ligne par sa valeur diagonale, dans `self.value` et `identity` à la fois.
5. À la fin, `self.value` est devenu l'identité et `identity` est devenu `A⁻¹` — la fonction retourne `self.value = identity`.
- Complexité O(n³) temps, O(n²) espace (le second tableau).
- Même limite que `determinant()` concernant l'échange de pivot nul limité à la dernière ligne.

## Matrice de projection — `projection` (ex14.py)

Construit la matrice de projection perspective caméra → écran, pour normaliser les coordonnées en NDC (`[-1,1]` pour x/y, `[0,1]` pour z).

- `f = 1/tan(fov/2)` : longueur focale — un FOV plus large réduit `f`, compressant davantage x/y (effet grand angle).
- `range_inv = 1/(near - far)` : terme de normalisation réutilisé pour remapper z.
- La matrice (en notation lignes, convertie en column-major par `Matrix`) :
  - Ligne 0/1 : mise à l'échelle de x (par `ratio`, l'aspect ratio) et y par la focale.
  - Ligne 2 : remappe z de `[near, far]` vers `[0,1]`, calculée avec `fma` pour plus de précision numérique.
  - Ligne 3 `[0,0,-1,0]` : copie `-z` dans la composante `w` — c'est ce qui produit la division perspective (objets lointains divisés par une valeur plus grande, donc plus petits à l'écran).
