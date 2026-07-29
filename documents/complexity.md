# Complexité temporelle et spatiale des fonctions

Ce document résume, pour chaque exercice, la complexité en temps et en
espace des fonctions implémentées, ainsi que la justification de pourquoi
elles respectent la limite fixée par le sujet.

## Exercice 00 — `add`, `sub`, `scl` (Vector et Matrix)

**Limite du sujet : O(n) en temps, O(n) en espace** (n = nombre d'éléments).

- Une seule boucle parcourt les n éléments (n = coordonnées pour un vecteur,
  n = lignes × colonnes pour une matrice stockée à plat).
- Chaque itération fait une opération scalaire en temps constant (`+=`,
  `-=` ou `*=`), donc le temps total est **O(n)**.
- La mise à jour se fait **en place** sur `self._value` : aucune nouvelle
  liste n'est créée, donc l'espace supplémentaire est **O(1)**, bien en
  dessous de la limite O(n).
- Les vérifications de taille/type avant la boucle sont O(1) (comparaison
  de tuples/valeurs déjà en cache).

## Exercice 01 — `linear_combination`

**Limite du sujet : O(n) en temps, O(n) en espace** (n = nombre total
d'éléments scalaires = taille du vecteur × nombre de vecteurs).

- Boucle imbriquée : la boucle externe parcourt les coordonnées, la boucle
  interne parcourt les vecteurs. Chaque paire `(i, j)` correspond à un
  élément scalaire distinct, visité une seule fois avec un travail O(1)
  (`fma`). Le total est donc exactement égal au nombre total d'éléments
  d'entrée, soit **O(n)** selon la définition du sujet (et non O(n²), car
  il n'y a jamais de comparaison entre éléments d'un même ensemble).
- `accumulator` est un scalaire réutilisé à chaque itération externe (pas
  une liste) : **O(1)** d'espace supplémentaire, seul `result` (taille du
  vecteur de sortie) contribue en O(n).

## Exercice 02 — `lerp`

**Limite du sujet : O(n) en temps, O(1) en espace.**

- Vecteur/Matrice : une seule boucle sur n éléments, écriture directe dans
  `u.value[i]` (en place) → **O(n)** temps, **O(1)** espace.
- Scalaire : deux multiplications et une addition, aucune boucle → **O(1)**
  temps et espace.
- Le piège évité : construire une nouvelle liste par compréhension aurait
  coûté O(n) en espace ; ici la mutation en place garde l'espace à O(1).

## Exercice 03 — `dot`

**Limite du sujet : O(n) en temps, O(1) en espace.**

- Une seule boucle sur n coordonnées, chaque itération fait un appel O(1)
  à `_conj`, une multiplication et une accumulation → **O(n)** temps.
- `result` est un unique scalaire réutilisé, jamais de liste intermédiaire
  de produits → **O(1)** espace.

## Exercice 04 — `norm_1`, `norm`, `norm_inf`

**Limite du sujet : O(n) en temps, O(1) en espace.**

- `norm_1` : une boucle, accumulation scalaire → O(n) / O(1).
- `norm` : appelle `dot(self)` (O(n)/O(1)) puis fait une racine carrée en
  O(1) → total O(n) / O(1).
- `norm_inf` : utilise `max(... for ...)` avec un **générateur**, pas une
  liste — les valeurs sont consommées une par une sans jamais matérialiser
  une liste de taille n → O(n) / O(1). (Une compréhension de liste aurait
  fait grimper l'espace à O(n).)

## Exercice 05 — `angle_cos`

**Limite du sujet : O(n) en temps, O(1) en espace.**

- Quatre passages séquentiels en O(n) chacun (vérification de vecteur nul
  ×2 via générateurs, `dot`, deux `norm`) : additionnés, pas imbriqués,
  donc toujours **O(n)** au total.
- Chaque passage réduit n valeurs à un seul scalaire ; la division finale
  ne combine que des scalaires → **O(1)** espace.

## Exercice 06 — `cross_product`

**Limite du sujet : O(1) en temps, O(1) en espace** (le produit vectoriel
n'est défini que pour des vecteurs à 3 dimensions, donc la taille n'est
jamais une variable — c'est une constante fixe).

- Aucune boucle : le résultat est calculé par exactement 3 expressions,
  chacune combinant 2 multiplications et 1 soustraction sur des indices
  fixes (0, 1, 2) → un nombre d'opérations fixe, indépendant de toute
  entrée variable → **O(1)** temps.
- `result` est une liste de taille fixe (toujours 3 éléments) → **O(1)**
  espace, pas de structure qui grandirait avec une taille n quelconque.
- Les vérifications (`isinstance`, `size() != 3`) sont également O(1)
  (comparaison de longueur déjà mise en cache).
- Le commentaire du code ([ex06.py:16](matrix/ex06.py#L16)) confirme
  explicitement ce raisonnement : "fixed number of operations regardless
  of input."

## Exercice 07 — `mul_vec`, `mul_mat`

**Limites du sujet :**
- `mul_vec` : O(n·m) temps, O(n) espace.
- `mul_mat` : O(n·m·p) temps, O(nm + mp + np) espace.

- `mul_vec` : boucle externe sur les n lignes, boucle interne sur les m
  colonnes, travail O(1) par élément → **O(nm)** temps. Seul `result`
  (taille n, la sortie) grandit ; `temp_result` est un scalaire réutilisé
  → **O(n)** espace.
- `mul_mat` : trois boucles imbriquées (p × n × m), travail O(1) par
  étape → **O(nmp)** temps. Les trois matrices vivantes en même temps
  (entrée self, entrée mat, sortie result) totalisent **O(nm + mp + np)**
  espace, sans structure intermédiaire supplémentaire.

## Exercice 08 — `trace`

**Limite du sujet : O(n) en temps, O(1) en espace** (matrice carrée n×n).

- La boucle ne visite que les n éléments diagonaux (grâce à l'indexation
  à plat `i * taille + i`), jamais les n² éléments complets → **O(n)**
  temps (meilleur que O(n²)).
- `result` est un scalaire accumulé en place → **O(1)** espace.

## Exercice 09 — `transpose`

**Limite du sujet : O(n·m) en temps, O(n·m) en espace.**

- Boucle imbriquée visitant chacun des n×m éléments exactement une fois,
  travail O(1) par élément → **O(nm)** temps.
- Une nouvelle matrice de même taille doit être produite (impossible de
  transposer en place tout en gardant l'originale), donc **O(nm)** espace
  est le coût minimal incompressible de la sortie elle-même.

## Exercice 10 — `row_echelon`

**Limite du sujet : O(n³) en temps, O(n²) en espace** (matrice carrée).

- `normalize_row` : O(n) (une ligne). `pivot` : O(m·n) (toutes les autres
  lignes × colonnes). Appelées une fois par ligne (m fois) → **O(n³)**
  pour une matrice carrée (conforme au commentaire du code).
- Toutes les opérations mutent `self.value` en place ; `normalized` est
  recréé et jeté à chaque itération (O(n) temporaire, jamais cumulé) →
  espace bien en dessous de la limite **O(n²)**.

## Exercice 11 — `determinant`

**Limite du sujet : O(n³) en temps, O(n²) en espace.**

- Élimination vers la forme triangulaire supérieure : trois boucles
  imbriquées (i, j, k), chacune O(n) → **O(n³)** temps. La phase finale de
  multiplication de la diagonale est O(n²) mais dominée par l'élimination.
- Tout se fait en place sur `self.value` ; seul un vecteur temporaire O(n)
  est utilisé lors des échanges de lignes → espace **O(n²)** ou mieux (pas
  de copie complète de la matrice).

## Exercice 12 — `inverse`

**Limite du sujet : O(n³) en temps, O(n²) en espace.**

- Quatre phases séquentielles, chacune O(n³) (déterminant, élimination
  inférieure, élimination supérieure, normalisation des pivots) : sommées
  (pas imbriquées) → **O(n³)** total, comme indiqué dans le commentaire du
  code.
- Deux tableaux à plat de taille n² (`self.value` et `identity`) plus une
  copie ponctuelle pour la vérification du déterminant : facteur constant
  de n², donc **O(n²)** espace — aucune matrice augmentée explicite n'est
  construite, ce qui évite un coût supplémentaire.

## Exercice 13 — `rank`

**Limite du sujet : O(n³) en temps, O(n²) en espace.**

- Domine par l'appel à `row_echelon()` (O(n³)). Le comptage des lignes
  nulles ajoute seulement O(n²) (une passe par ligne, générateur `all`
  sans liste intermédiaire) → total **O(n³)** temps.
- `check_zero_row` n'utilise qu'un compteur scalaire et un générateur
  paresseux, donc **aucun espace supplémentaire** n'est ajouté au-delà de
  ce que `row_echelon` utilise déjà → **O(n²)** au total.
