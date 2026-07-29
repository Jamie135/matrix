# Complex

Ce document résume la classe `Complex` implémentée dans [`complex.py`](../complex.py), qui fournit un type de nombre complexe `a + bi` utilisable comme corps de scalaires `K` pour `Vector`/`Matrix` (bonus de l'ex15). Aucune bibliothèque mathématique n'est utilisée : tout est dérivé à la main à partir de l'algèbre des nombres complexes.

## Représentation

Un nombre complexe `z = a + bi` est stocké comme deux flottants, `re` (a) et `im` (b) — un point du plan complexe, avec l'axe des réels et l'axe des imaginaires.

## `_coerce`

Permet de mélanger `Complex` avec des `int`/`float` classiques, en traitant un réel `r` comme `r + 0i` — c'est l'inclusion naturelle des réels dans les complexes (ℝ ↪ ℂ). Ainsi `Complex(1, 2) + 3` fonctionne comme si `3` était `3 + 0i`.

## `conjugate`

Le conjugué de `a + bi` est `a − bi` : une réflexion par rapport à l'axe des réels. C'est l'ingrédient clé utilisé plus loin pour la division, afin de « rationaliser » le dénominateur.

## `add` / `sub` / `neg`

L'addition et la soustraction se font composante par composante : `(a+bi) ± (c+di) = (a±c) + (b±d)i`. Géométriquement, c'est la même règle du parallélogramme que pour les vecteurs, puisque ℂ ressemble ici à ℝ². `neg` donne l'inverse additif de chaque élément.

## `mul`

La multiplication complexe standard, obtenue en développant `(a+bi)(c+di)` et en utilisant `i² = -1` :

```
(a+bi)(c+di) = ac + adi + bci + bdi²
             = (ac - bd) + (ad + bc)i
```

D'où partie réelle `ac - bd` et partie imaginaire `bc + ad`. Géométriquement, multiplier par `c+di` revient à faire tourner et à mettre à l'échelle : l'angle s'additionne et les modules se multiplient.

## `truediv`

On divise en multipliant numérateur et dénominateur par le conjugué du diviseur :

```
(a+bi)/(c+di) = (a+bi)(c-di) / ((c+di)(c-di)) = (a+bi)(c-di) / (c²+d²)
```

En développant le numérateur, on obtient partie réelle `ac+bd`, partie imaginaire `bc-ad`, le tout divisé par `c²+d² = |c+di|²` (le module au carré du diviseur, appelé `denom` dans le code). La division est indéfinie quand `denom == 0`, c'est-à-dire quand on divise par `0 + 0i`.

## `radd` / `rsub` / `rmul` / `rtruediv`

Ces méthodes « miroir » permettent à des expressions comme `3 + Complex(1, 2)` de fonctionner : quand l'opérande de gauche est un nombre classique et que son propre `__add__` etc. renvoie `NotImplemented`, Python retente l'opération via ces méthodes du côté droit.

## `abs`

Le module `|z| = √(a² + b²)`, c'est-à-dire la distance euclidienne entre `z` et l'origine dans le plan complexe. C'est ce que les fonctions de norme de `Vector`/`Matrix` utilisent comme « magnitude » d'un scalaire lorsque `K = Complex`.

## `eq` / `hash`

Deux complexes sont égaux si et seulement si leurs parties réelle et imaginaire coïncident. `hash` est dérivé du couple `(re, im)`, pour rester cohérent avec `eq` et permettre l'usage de `Complex` dans des ensembles ou des dictionnaires.

## `repr`

Affiche `(a+bi)` ou `(a-bi)` selon le signe de la partie imaginaire.

## Résumé

`Complex` fournit exactement la structure nécessaire — un corps commutatif (addition, soustraction, multiplication, division) muni d'une norme (`abs`) — pour que `K = Complex` satisfasse ce qu'attend le code générique de `Vector`/`Matrix` : combinaisons linéaires, produits scalaires, normes.

## Utilisation dans les exercices (ex00 à ex13)

Le code de `Vector`/`Matrix` est générique sur `K` : il n'existe aucune branche spécifique à `Complex`. C'est uniquement parce que `Complex` surcharge `+`, `-`, `*`, `/`, `abs()` etc. que ces exercices fonctionnent tels quels avec `K = Complex`.

### ex00 — add, sub, scl

`add`/`sub` appellent `Complex.__add__`/`__sub__` : addition/soustraction composante par composante. `scl` appelle `Complex.__mul__` sur chaque élément ; avec un scalaire `Complex(0,1)` (= `i`), c'est la multiplication complexe complète. Exemple : `Complex(2,1) * Complex(0,1)` → `re = 2*0 - 1*1 = -1`, `im = 1*0 + 2*1 = 2` → `(-1+2i)`.

### ex01 — combinaison linéaire

`fma(a, b, c) = (a * b) + c` enchaîne `__mul__` puis `__add__`. Avec `K = Complex`, chaque étape est une multiplication complexe suivie d'une addition. L'accumulateur démarre à l'`int` `0`, coercé en `Complex(0,0)` par `_coerce` dès la première addition.

### ex02 — interpolation linéaire (lerp)

`u*(1-t) + v*t` où `t` est un `float` réel. Comme `t` est coercé en `Complex(t, 0)`, la formule de multiplication complexe se simplifie : `(a+bi)*(t+0i) = at + bti`, donc multiplier par un scalaire réel revient juste à mettre `re` et `im` à l'échelle par `t` (pas de terme croisé, puisque la partie imaginaire du scalaire est nulle).

### ex03 — produit scalaire (dot)

Ce n'est pas une simple somme de produits : `dot` est sesquilinéaire, il conjugue les composantes du second vecteur avant de multiplier (`self._value[i] * _conj(v.value[i])`). Cela garantit que `v.dot(v)` est toujours réel et positif, ce qui correspond à ce qu'on attend d'une « longueur » même en complexe. Exemple : `i = Complex(0,1)`, `dot([i], [i]) = i * conj(i) = i * (-i) = (0+1i)*(0-1i)` → `re = 0*0 - 1*(-1) = 1`, `im = 1*0 + 0*(-1) = 0` → `(1.0+0.0i)`.

### ex04 — normes

`norm_1` et `norm_inf` utilisent `abs()`, c'est-à-dire `Complex.__abs__` = le module `√(a²+b²)`. `norm`, elle, passe par `dot(self, self)` (donc par la conjugaison de ex03), ce qui donne toujours un résultat réel (`a²+b²` avec partie imaginaire nulle) ; `_to_real` en extrait la partie réelle avant la racine carrée.

### ex05 — cosinus de l'angle

`angle_cos = u.dot(v) / (u.norm() * v.norm())`. Le numérateur est un `Complex` (dot sesquilinéaire), le dénominateur est un `float` réel (produit de deux normes). La division `Complex / float` passe par `Complex.__truediv__`, qui coerce le `float` en `Complex(t, 0)` : la formule se simplifie alors en une simple division de `re` et `im` par `t`.

### ex06 — produit vectoriel (cross product)

Contrairement à `dot`, ici **pas de conjugaison** : uniquement des `__mul__` et `__sub__` complexes classiques, appliqués à la formule usuelle `u1*v2 - u2*v1`, etc.

### ex07 — application linéaire, multiplication matricielle

`mul_vec`/`mul_mat` sont des sommes de produits `Complex * Complex` accumulées via `+=`, sans conjugaison ni logique spécifique — exactement les mêmes surcharges `__mul__`/`__add__` que partout ailleurs, juste appliquées ligne par colonne (produit matriciel standard).

### ex08 — trace

Simple somme des éléments diagonaux via `Complex.__add__` répété ; aucune multiplication n'intervient.

### ex09 — transposée

Aucune arithmétique sur les valeurs `Complex` : la transposée ne fait que réarranger leur position (`M[i][j] → M[j][i]`), chaque valeur étant recopiée telle quelle. Ce n'est que la transposée mathématique, pas la transposée conjuguée (adjointe hermitienne) : les parties imaginaires ne sont jamais inversées.

### ex10 — forme échelonnée réduite (row echelon)

Deux opérations complexes : la **normalisation** du pivot (`value /= denom`, via `Complex.__truediv__`) pour le ramener à `1`, puis l'**élimination** des autres lignes par `deduct = value * normalized[col]` suivi de `value -= deduct * normalized[k]` (multiplication puis soustraction complexes).

### ex11 — déterminant

Basé sur une décomposition LU : les mêmes opérations de division/multiplication/soustraction complexes que ex10 réduisent la matrice sous forme triangulaire supérieure, puis le déterminant est le produit des éléments diagonaux via `Complex.__mul__` répété (plus un facteur `±1` réel si des lignes ont été échangées).

### ex12 — inverse

Élimination de Gauss-Jordan sur `[A | I]` : mêmes opérations complexes que ex10/ex11, appliquées en parallèle à la matrice et à une matrice identité. Exemple notable : pour une matrice diagonale, l'inversion revient à diviser `1` par chaque élément diagonal — `1 / (0+1i) = 0-1i`, c'est-à-dire l'identité classique `1/i = -i`, qui découle directement de la formule de division complexe.

### ex13 — rang (rank)

`rank` ne fait aucun calcul `Complex` par elle-même : elle appelle d'abord `row_echelon()` (ex10), qui effectue toute l'arithmétique complexe (division du pivot, multiplication/soustraction pour éliminer les autres lignes). Une fois la matrice sous forme échelonnée, `rank` se contente de compter les lignes non nulles : `check_zero_row` teste `self.value[k] == 0` pour chaque élément d'une ligne, ce qui appelle `Complex.__eq__` (égalité si `re` et `im` coïncident tous les deux, voir plus haut). Le rang est alors `nb_lignes - nb_lignes_nulles`.

Exemple, [ex13.py:32](../ex13.py#L32) : `M = [[1+0i, 2+0i], [2+0i, 4+0i]]`. Après `row_echelon`, la deuxième ligne est un multiple complexe de la première (`deduct = 2+0i`), donc elle s'annule entièrement : `[1+0i, 2+0i]` puis `[0+0i, 0+0i]`. `check_zero_row` détecte une ligne nulle sur deux, d'où `rank = 2 - 1 = 1`, ce qui correspond au commentaire `# 1`.
