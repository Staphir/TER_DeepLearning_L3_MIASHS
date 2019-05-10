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

Cette méthode est globalement la seule et unique implémentation

Après avoir étudié cette exemple appliqué au rubik’s cube, nous avons voulu faire de même avec un autre casse-tête, le Shift It.
Il a donc fallu que nous programmons le nôtre tout en réfléchissant à des fonctions permettants l’implémentation de l’algorithme de Deep-Learning.

~~~~~~~~~~~

Le Shift It
===========

~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Le Shift It se joue avec une grille comportant des carrés de plusieurs couleurs.
Le but est d’avoir une grille où toutes les cases de la même couleur formes une seul zone.
Il faut donc autant de zones que de couleurs et que chaque case soit adjacente avec au moins une autre case de la même couleur.
Voici un exemple du jeu sur Android :

.. code-block:: html
    :file: ../Site/_templates/youtube_link.html

.. image:: pictures/Shiftit_GUI2.gif
    :scale: 50%
    :align: center