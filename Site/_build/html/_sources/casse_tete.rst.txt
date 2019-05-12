.. title:: Notre programme

Introduction
============

~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Notre but aura été de trouver les différentes méthodes de résolution de casse-têtes par algorithmes de deep-learning,
c’est à dire créer un outil utilisant le deep-learning et l’entraîner sur des données
correspondant à des situations que l’on peut rencontrer dans un casse-tête.

Il est avant tout important de noter que ce travail est un sujet de recherche.
Quand nous avons commencé la réalisation de ce projet, nous n’avions aucune idée de où cela allait nous mener.

Nos bases concernant ces système d’apprentissage étant quasi-inexistantes au commencement de ce projet,
il a été nécessaire de tenter de comprendre les différents modules mis à notre disposition
en réalisant des tutoriels de manipulation proposés par les équipes de développement ou
encore d’autres personnes proposant une explication guidée de l’utilisation de telle ou telle bibliothèque.
Vous pourrez retrouver tous les liens dans la `bibliographie <bibliographie.html>`_.
Il est aussi important de noter que certains modules complémentaires sont devenus indispensable
lors de l’utilisation de ces bibliothèques de Réseaux de Neurones et ont donc nécessité que l’on s’y intéresse
et apprenne à les manipuler (Matplotlib et NumPy notamment).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

La méthode d’implémentation
===========================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Pour créer notre propre algorithme de Deep-Learning nous avons commencé par choisir
la méthode suivant laquelle nous allions fournir nos données à l’algorithme.
Comme mentionné dans `l'état de l'art <historique.html>`_ cette étape dans la création d’une méthode d’apprentissage par Deep-Learning est très importante.
Pour ce faire, nous nous sommes basé sur l’implémentation de Jeremy Pinto (`github de son projet <https://github.com/jerpint/rubiks_cube_convnet>`_)
pour concevoir notre générateur de données.

Son implémentation consiste en générer des partie aléatoires de Rubik’s cube en partant d’un état résolu
puis mélangé un certain nombre de fois (10 dans son cas). Après quoi il utilise le chemin vers l’état mélangé *Scrambled state*
pour trouver le chemin inverse vers la résolution.

En partant de l’état mélangé et en appliquant le premier mouvement du chemin vers la résolution,
il obtient l’état suivant de la matrice vers résolution, puis construit des pairs
(matrice (6x3x3 - 6 faces de 3 cellules en hauteur et 3 cellules en largeur) - mouvement),
la matrice correspondant à l’état mélangé du cube et le mouvement à celui qu’il faut effectuer pour atteindre un état de résolution plus proche du cube résolu.

Pour plus de clarté, voici le pseudo code du déroulement de la génération des données :

.. literalinclude:: ../Site/data/generate_data.pseudoc

Le but de son algorithme est de pouvoir entraîner la machine à, pour une certaine configuration du cube,
prédire le mouvement à effectuer pour se rapprocher de l’état résolu.
Il effectue donc ici un apprentissage supervisé en fournissant à chaque fois un état du cube
et son mouvement associé puis en demandant à son réseau de neurone de prédire le prochain mouvement à faire.
La rétropropagation se fait alors sur la comparaison entre le mouvement prédit et celui fourni.

Après 12h d’entraînement de son réseau de neurone, il parvient à obtenir un modèle capable de résoudre
avec un bon taux de réussite un Rubik’s cube mélangé 6 fois (6 pas de différence avec l’état résolu).
Le modèle n’est pas parfait et au delà de 6 mouvements aléatoires,
le NN ne parvient plus vraiment à trouver les solutions comme on peut le voir ci dessous.

.. image:: ../Site/pictures/cube_solving.gif
    :scale: 65%
    :align: center

Etant donné cette implémentation est globalement la seule et unique
que nous avons pu relever au travers de nos recherches,
le choix de la méthode de construction de notre propre réseau de neurone
n’en a finalement pas été réellement un.

Nous avons donc commencé par construire notre propre jeu,
puzzle numérique sur lequel entraîner notre réseau de neurones
tout en prenant compte du fait qu’il allait devoir communiquer
d’une certaine manièreavec d’autre programmes de Machine Learning.

Le jeu que nous avons décidé de reproduire se nomme le Shift It.
C’est un jeu qui fut développé à l’origine sous Android mais qui à l’instant n'est plus disponible
sur les plateformes de téléchargement principales (Google Play Store) bien qu'il soit toujours possible
de le récupérer sous forme de fichier .apk sur certains hébergeurs.

~~~~~~~~~~~

Le Shift It
===========

~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Le Shift It se joue avec une grille comportant des carrés de plusieurs couleurs.
Le but est d’avoir une grille où toutes les cases de la même couleur formes une seul zone.
Il faut donc autant de zones que de couleurs et que chaque case soit adjacente avec au moins une autre case de la même couleur.

Voici un visuel du jeu :


Exemple du Shift It sur Android
*******************************

Notre version du Shift It est composé d’une grille de taille et de nombre de couleurs modifiables
(pour l’instant le nombre de couleurs à été bloqué à 2). Pour l’apprentissage de notre modèle,
nous nous sommes fixé une taille de 5x5 et uniquement 2 couleurs différents.
Des configurations plus compliqués d’entraînement seront envisageables dans le futur.

Nous avons commencé par créer une classe Python, correspondant à la partie fonctionnelle du jeu,
doté d’attributs permettants de stocker la hauteur et la largeur de la grille en plus de la grille elle-même
ainsi que le chemin de mouvements nécessaire à effectuer depuis l’état actuel pour obtenir l’état de résolution.
Elle conserve aussi une sauvegarde de son état résolu ainsi qu’un solveur qui utilise le modèle généré grâce au Deep Learning.

Les principales fonctionnalités du programme sont les suivantes :

* generate() : permet de générer aléatoirement une grille de jeu résolue.
* shuffle(n) : permet de sélectionner aléatoirement des mouvements et les appliquer,
  le paramètre n correspond au nombre de mouvements aléatoire appliqués.
  Cette méthode renvoie le chemin inverse de celui qui a été fait en mélangeant.
* shift(key) : permet d’effectuer le mouvement de la ligne ou de la colonne déterminé par la valeur key.
* solve_with_IA(limit) : permet de faire fonctionner le réseau de neurone sur l’état actuel de la grille
  pour prédire le mouvement à faire. Le paramètre limit correspond au nombre maximum de mouvement
  que doit prédire le réseau (s’avère plutôt utile lorsque le modèle ne parvient pas à atteindre
  la résolution - ce qui arrive 99% du temps)
* reset() : permet de remettre la grille à son état résolu mais sans générer une nouvelle configuration.

Ainsi que les principales propriétés :

* width : largeur
* height : hauteur
* state: booléen indiquant si le jeu est résolu ou non
* moves : la liste des mouvements possibles en fonction de la grille

Les mouvements possibles sont représentés par des chaînes de caractères de longueur 2 ou 1.
Elles sont composées d’un entier désignant la ligne ou la colonne à faire défiler ainsi
que du caractère "‘" (apostrophe) désignant le sens de défilement.
Si le défilement est dans le sens normal (haut en bas pour la colonne et de gauche à droite pour la ligne)
alors la chaîne de caractères est uniquement composée du numéro de la ligne ou colonne.
Ce numéro désignant la ligne ou la colonne est un entier pair si l’élément sélectionné est une ligne et,
à l’inverse, est impair si c’est une colonne. La première ligne de la grille sera numéroté 0,
la deuxième ligne sera numéroté 2 et la troisième colonne sera numéroté 5 par exemple.
Ainsi le mouvement désigné par 9’ correspondra à un défilement de bas en haut de la dernière colonne de la grille.
Alors sur une grille de NxM, il y aura (N+M)x2 mouvements possibles soit 20 dans une configuration de 5 par 5.

Notre code est accessible au lien suivant : `GitHub <https://github.com/Staphir/TER_DeepLearning_L3_MIASHS>`_

~~~~~~~~~~~~~~~~~~~~~~

L’entraînement de l’IA
======================

~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Afin d’entraîner notre programme d'intelligence artificielle, nous avions besoin de deux choses.
D’une part des données d’entrainements qui seront construites en utilisant l’implémentation de
notre Shift it et d’autre part du modèle dans lequel nous feront passer ces données.

La création des données d’entraînement :
****************************************

Pour construire un set de données utilisables par un modèle d’apprentissage,
nous nous sommes inspirés de la méthode de Jeremy Pinto et avons généré de la même manière
que lui des pairs grilles / mouvement, les grilles correspondant aux features et les mouvements aux labels.
Il est possible de passer directement le mouvement sous forme de chaîne de caractère
au système d’apprentissage mais dans notre cas nous avons simplifié cette information
en associant un indice à chaque mouvement. Ces sont ces indices qui sont fournis au système.

Premièrement, nous avons construit la méthode de génération de parties :

.. literalinclude:: ../Code/Jeux/Shiftit/train_shiftit_new.py
    :language: python
    :pyobject: generate_game

Cette méthode permet de créer un objet jeu (une instance de notre ShiftIt)
dans un état mélangé ainsi que le chemin vers succès associé (une liste de mouvements).
Ce couple d’élément est alors renvoyé par la méthode une fois qu’il est créé.

La méthode suivante consiste en, pour un couple d’éléments comme cités juste avant,
générer toutes les paires grille / mouvement comme expliqué plus tôt (algorithme en pseudocode).
De cette manière, si l’on mélange chacun des jeux en 10 coups, ils se verront tous associé
une liste de 10 pairs grille / mouvement correspondant aux états intermédiaires avec
les mouvements à effectuer pour passer à celui suivant.

.. literalinclude:: ../Code/Jeux/Shiftit/train_shiftit_new.py
    :language: python
    :pyobject: generate_game_data

Pour finir, la dernière méthode a été implémentée sous la forme d’un générateur Python
(`voir la documentation <https://wiki.python.org/moin/Generators>`_) et permet de renvoyer,
un nombre de fois définit par la variable *game_count*,
le traitement des éléments renvoyés par la première méthode au travers de la seconde.
Ainsi, nous créons un plus gros ensemble de pairs grille / mouvement
qui sont alors fournis séparément au modèle, avec d’un côté les grilles à partir desquelles
extraire les informations et prédire les mouvements et de l’autre, les mouvements correctes
vers lesquels les prédictions doivent tendre (utilisés pour la rétropropagation).

.. literalinclude:: ../Code/Jeux/Shiftit/train_shiftit_new.py
    :language: python
    :pyobject: data_generator

Le modèle d’entraînement
************************

Ici, le modèle d’entraînement fait référence à l’ensemble des couches utilisées
pour construire le réseau de neurone au complet, donc à l’*input layer*, l’*output layer*,
ainsi que les *hidden layers* qui viennent entre les deux.
Il est en généralement requis de dédier un temps relativement conséquent à son optimisation,
c’est à dire à savoir exactement quels types de layers implémenter et dans quel ordre.

Malheureusement, nous n’avons pas eu les connaissances nécessaires afin de pouvoir
mener cette étape à bien et de ce fait avons dû utiliser (et modifier) les modèles proposés par Jeremy Pinto
ainsi que d’autres que l’on a pu rencontrer au travers de différents tutoriels trouvés sur le net.
Il est d’ailleurs fort probable que ce fut la raison pour laquelle notre modèle
n’était pas en mesure de résoudre correctement même la plus simple des configuration que nous lui fournissions…

Ci-dessous le modèle que nous avons utilisé :

.. literalinclude:: ../Code/Jeux/Shiftit/train_shiftit_new.py
    :language: python
    :lines: 168-187