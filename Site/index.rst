.. TER_DeepLearning documentation master file, created by
   sphinx-quickstart on Wed Mar  6 16:36:44 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Bienvenue sur le site de notre TER sur le Deep-learning
=======================================================

.. toctree::
   :maxdepth: 1


--------------------------------------------------------

.. toctree::
   :maxdepth: 1

Abstract
========

Since the arrival of multiple Machine Learning packages(such as Tensorflow or PyTorch for Python programming language)
that came with the large growth in performance we’ve recently seen in personal computer, more and more useful real life applications
of these system have see the light and allowed us to digitally solve a wide variety of automation issues.

Another one of the many sides of Machine Learning is the ability to solve puzzle games or brain teasers.
Research has shown that it is possible to adapt and solve different kinds of brain teasers, puzzle games (such as Rubik’s Cube)
through the help of Machine Learning. It is in this perspective that began our exploratory project, which goal was to find computerized ways
of solving those games using Deep Learning.

In order to achieve this goal, we started by learning how to use some Deep Learning libraries,
search for relevant differences between them and assess their usability. We also went into the gathering of existing methods,
applications of actual puzzle games implementations in order to get an overall idea of how it is done.

At last we designed our own application using Tensorflow to test whether those methods could be easily applied or not.
Results concerning our own application raised the fact that a more in depth knowledge on how to choose layers accordingly to the problem
is necessary to get the best performances out of our model. We did manage to get our system learning how to solve the handmade puzzle
but did not get the final sloving accuracy we were expecting (results are an overall of 1 out of 5 chances of getting the right move at a certain time in the game).
To conclude, we successfully implemented the "Shift it" game.

.. toctree::
   :maxdepth: 1

Résumé
======

Le "deep-learning" (sous-branche des techniques de "machine-learning") est une méthode de programmation en Intelligence Artificielle
qui s’est énormément développée ces dernières années avec l’augmentation de la puissance de calcul des ordinateurs.
C’est une méthode qui existait déjà il y a plus d’un demi-siècle, mais nécessitait une charge de calcul
beaucoup trop importante par rapport aux performances de l’époque.

Cette technique consiste à programmer des réseaux de neurones informatisés,
très largement inspirés du fonctionnement des réseaux de neurones humain, que l'on va entraîner sur des tâches diverses
(par exemple, être capable de différencier un chat d’un chien) avec la particularité que le programme va s’améliorer au cours du temps
et du traitement de nouvelles informations.

Pour la programmation des algorithmes de deep-learning, plusieurs bibliothèques logicielles existent,
comme par exemple les bibliothèques PyTorch, Keras ou Theano (qu'on peut utiliser avec le langage de Programmation Python).
Un premier axe de notre travail de TER a été de comparer ces bibliothèques sur différents critères, comparaison qu'on pourra trouver sur ce site.
Par la suite, un deuxième axe de notre TER a porté sur la résolution de casse-têtes par ces méthodes de deep-learning.

Pour ce faire, après avoir fait des recherches sur les différentes méthodes d’applications possibles,
nous avons construit un programme de résolution, basé sur un casse-tête nommé "Shift It".
Le principe de ce casse-tête est de trouver les mouvements permettant de regrouper les cases de même couleurs en groupes de cases adjacentes.
La grille utilisée pour l’entraînement est une grille de 5 par 5 composée uniquement de deux couleurs différentes pour des raisons de simplicité.


