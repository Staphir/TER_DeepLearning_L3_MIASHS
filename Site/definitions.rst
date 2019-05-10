Définitions importantes
=======================

.. toctree::
   :maxdepth: 2

-----------------------

Certains termes et notions utilisés couramment en réseaux de neurones (Neural Network - NN) nécessitent d’être définis pour continuer au travers de ce projet.
La plupart du temps ce sont des termes qui dérivent de l’anglais ou alors des notions relativement simples mais qui méritent d’être explicitées.

* **Le dataset** : L’ensemble des données que l’on va utiliser pour tester / entraîner notre NN.
  Il est généralement divisé en 2 parties qui sont d’une part les données d’entraînement (Les training data qui servent à l’apprentissage du NN)
  et d’autre part les données de test (Les test data qui servent à vérifier le fonctionnement du NN) qui ne sont pas comprises dans les données d’entraînement.

..

* **Rétropropagation** : Fonction permettant d’adapter la solution suivant les résultats obtenus durant le passage dans le réseau.
  Avoir plusieurs passages (et donc plusieurs renvoies de la fonction de rétropropagation) permet au système de plus en plus tendre vers la vérité.

..

* **Une epoch** : Un unique envoie du jeu de données d’entraînement au système durant la phase d’apprentissage.
  La nécessité de plusieurs epochs résulte du fait que lors de l’apprentissage,
  la rétropropagation nécessite plusieurs passage sur une même donnée pour tendre vers une solution optimale.

..

* **Un batch** : Prenons l’exemple d’un très grand dataset lors de la phase d’apprentissage,
  le but ne va pas être de le donner en une seule fois au NN mais de le diviser en batchs pour simplifier son intégration.
  Ce sont donc des divisions du dataset. Le batch-size correspond au nombre d’éléments du dataset présent dans un batch.