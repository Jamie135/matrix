# Projection

Ce document explique la fonction `projection` (module `matrix/ex14.py`), puis décrit comment tester la matrice obtenue avec l'outil `matrix_display`.

## La fonction de projection

Imagine ton œil (la « caméra ») posé à un point précis, regardant le long d'un axe, avec une fenêtre rectangulaire imaginaire devant lui — c'est ton écran. Tout ce que la caméra « voit » à travers cette fenêtre est aplati dessus. La matrice de projection n'est qu'une recette figée (une grille de 4x4 nombres) qui prend un point 3D `(x, y, z)` et l'écrase sur cette fenêtre 2D, d'une manière qui imite la perspective réelle : les objets plus loin paraissent plus petits, et tout converge vers un point de fuite.

Voici `ex14.py:28-33` décortiqué morceau par morceau :

### Les entrées

- `fov` — champ de vision (*field of view*), l'angle (en radians) du « cône de vision » de la caméra, un peu comme la différence entre un objectif grand-angle et un objectif zoomé.
- `ratio` — rapport d'aspect de l'écran (largeur ÷ hauteur). 1.0 = écran carré.
- `near` / `far` — distances par rapport à la caméra. Tout ce qui est plus proche que `near` ou plus loin que `far` est éliminé (non affiché).

### `f = 1 / tan(fov/2)` (`ex14.py:23`)

C'est le « facteur de zoom ». Un grand FoV (comme 100°) rend `tan(fov/2)` grand, donc `f` est petit — les objets sont davantage compressés (vue large, objets petits). Un FoV étroit (40°) rend `f` grand — les objets sont zoomés et paraissent plus gros, comme avec un téléobjectif.

### La matrice elle-même

4 lignes, 4 colonnes. Chaque ligne fait un travail précis quand elle est utilisée pour transformer un point :

- **Ligne 1 : `[f/ratio, 0, 0, 0]`** — prend le `x` du point et le multiplie par `f/ratio`. Ça contrôle la compression gauche-droite. Diviser par `ratio` est ce qui étire/écrase l'image horizontalement quand l'écran n'est pas carré.
- **Ligne 2 : `[0, f, 0, 0]`** — prend `y` et le multiplie par `f`. Contrôle la compression haut-bas (pas de division par `ratio` — la verticale sert de référence).
- **Ligne 3 : `[0, 0, far/(near-far), (far*near)/(near-far)]`** — c'est la ligne de « profondeur ». Elle remappe la profondeur réelle (`z`, de `near` à `far`) vers une plage normalisée de 0 à 1, que l'outil d'affichage utilise pour savoir ce qui est devant/derrière, et pour décider ce qui est trop proche/trop loin pour être affiché.
- **Ligne 4 : `[0, 0, -1, 0]`** — recopie simplement `-z` dans un emplacement restant (appelé `w`). Tout le reste du point (les résultats des lignes 1 à 3) est ensuite divisé par cette valeur `w`. Cette division est *l'astuce* qui crée la perspective — les points deux fois plus loin se retrouvent avec un `w` deux fois plus grand, donc leurs résultats x/y sont réduits deux fois plus, ce qui les fait paraître deux fois plus petits. C'est littéralement l'effet « les objets lointains paraissent plus petits », obtenu avec une seule division.

En résumé : FoV/ratio contrôlent les lignes 1-2 (à quel point les objets sont zoomés et étirés latéralement), near/far contrôlent la ligne 3 (où les objets sont éliminés en profondeur), et la ligne 4 est le mécanisme fixe qui crée réellement la perspective (la taille qui diminue avec la distance).

## Tester avec `matrix_display`

`ex14.py` peut écrire directement une matrice au format attendu par l'outil (`matrix_display/proj`) :

```bash
cd matrix
python3 ex14.py <fov_degrés> <ratio> <near> <far> [chemin_de_sortie]
```

Par défaut, le fichier est écrit dans `matrix_display/proj`. Il suffit ensuite de lancer `./matrix_display/display` pour visualiser le résultat.

### 1. Tester plusieurs FoV (100°, 70°, 40°)

```bash
python3 ex14.py 100 1.777 0.5 100.0
./matrix_display/display
python3 ex14.py 70 1.777 0.5 100.0
./matrix_display/display
python3 ex14.py 40 1.777 0.5 100.0
./matrix_display/display
```

**Attendu :** un FoV plus faible doit réduire l'angle de vue (effet zoom/téléobjectif) — le logo apparaît plus grand et le champ visible plus étroit à 40° qu'à 100°.

### 2. Tester plusieurs ratios

```bash
python3 ex14.py 100 1.0 0.5 100.0
./matrix_display/display
python3 ex14.py 100 1.7778 0.5 100.0   # 16/9
./matrix_display/display
python3 ex14.py 100 0.5 0.5 100.0
./matrix_display/display
```

**Attendu :** changer le ratio doit déformer l'image (étirement ou écrasement horizontal du logo).

### 3. Tester plusieurs combinaisons near/far (`near < far`)

```bash
python3 ex14.py 100 1.777 1.0 10.0
./matrix_display/display
python3 ex14.py 100 1.777 5.0 50.0
./matrix_display/display
```

**Attendu :** des valeurs différentes de `near`/`far` doivent changer la distance à laquelle les objets disparaissent de l'écran (clipping plus ou moins proche/lointain).

## Questions pour l'étudiant

Pour vérifier la compréhension, on peut demander d'expliquer ce que représente chaque composant de la matrice :

- Que représente `f = 1/tan(fov/2)` et pourquoi varie-t-il en sens inverse du FoV ?
- Pourquoi seule la ligne 1 est divisée par `ratio`, et pas la ligne 2 ?
- Que fait concrètement la ligne 3, et pourquoi dépend-elle à la fois de `near` et de `far` ?
- Pourquoi la ligne 4 (`[0, 0, -1, 0]`) est-elle nécessaire pour obtenir un effet de perspective, et que se passe-t-il si on la remplace par `[0, 0, 0, 1]` (projection orthographique, sans perspective) ?
