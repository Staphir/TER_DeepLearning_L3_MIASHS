.. title:: Bibliotèques python

Présentation de différentes bibliotèques
========================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Avans-propos
************

Avant de vous présenter les principales bibliothèques python permettant de faire du Deep-Learning,
il faut savoir qu’une bibliothèque scientifique appelé NumPy est utilisé
dans toutes les bibliothèques qui vont suivre. NumPy permet certes,
d’avoir un affichage graphique (d’images par exemple), mais
la principale utilité de NumPy pour le Deep-Learning réside dans la création
et la manipulation de matrice à n dimension (noté numpy.array).

`Page d'accueil NumPy <http://www.numpy.org/>`_

Keras
*********

**Description**

Sûrement la bibliotèque python la plus aimé car elle est simple d’utilisation sans pour autant brider les possibilités de programmation.
Seul point faible, la personnalisation est difficile à mettre en place.
Elle se programme sous forme de blocs, ce qui fait sa simplicité et réduit la longueur du code.
Les personnes utilisants Keras commencent à migrer vers TensorFlow qui est justement basé sur keras mais ajoute de nouvelles possibilitées.

`Page d'accueil Keras <https://keras.io/>`_

Theano
***********

**Description**

LA “sous-couche” des autres bibliotèques d’apprentissages de réseaux de neurones. Comme tous les autres utilise des Numpy.arrays

`Page d'accueil Theano <http://deeplearning.net/software/theano/index.html>`_

TensorFlow
**********

**Description**

TensorFlow est une bibliotèque open source développée  par une équipe de Google (Google Brain Team). Elle n'est pas seulement
utilisée par Google mais par beaucoup d'autres grandes entreprises (Twitter, Coca-Cola, Airbus...). Cette bibliotèque
peut être utilisée pour plusieurs plateformes (ordinateurs, telephones, internet et cloud).
Elle est principalement utilisé dans la reconnaissance vocale ou d’image et dans les applications textuelles, comme Google Translate par exemple.
Elle a pour avantage d’être très utilisée ce qui fait qu’il y a beaucoup de documentation avec une grosse communauté de développeur.
Point faible, elle est lente car il y a beaucoup de fonctionnalitées implémentées qui ne seront pas utilisé par tout le monde mais forcément importés.


`Page d'accueil TensorFlow <https://www.tensorflow.org>`_

Pytorch
************

**Description**

Bibliothèque très complète. Elle est complexe mais permet une grande flexibilité et une personnalisation approfondie une fois les compétences acquises.
Elle a été développé par Facebook, elle est assez plébiscitée par les chercheurs du fait de son efficacité
et de sa rapidité pour mettre en place des modèles d’apprentissages. Elle a pour avantage d’avoir des pièces modulaires prêtes à l’emplois,
un processus de modélisation simple et son mode de définition se rapproche beaucoup de la programmation standard.
Mais par contre il n’y a pas d’interface permettant de visualiser le processus ce qui peut compliquer la tâche des programmeurs.

`Page d'accueil Pytorch <https://pytorch.org/>`_

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparaison de différentes bibliotèques
=======================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Dans cette partie nous comparerons seulement les quatres bibliothèques présentées
ci-dessus car ce sont les bibliothèques python les plus utilisées.
Il faut tout de même garder en tête que TensorFlow est basé sur Keras donc ceux
qui utilisent TensorFlow utilise aussi d’une certaine manière Keras.

La comparaison entre plusieurs bibliothèques peut se faire sous de nombreux aspects
tels que la popularité, la complexité d’utilisation, la rapidité d'exécution, etc.

L'article Deep Learning Framework Power Scores 2018 de Jeff Hale nous a permis d'avoir
une comparaison de l’utilisation, de l’intérêt et de la popularité des différentes bibliothèques python.


L'article de Jeff Hale
**********************

L'article `Deep Learning Framework Power Scores 2018 <https://towardsdatascience.com/deep-learning-framework-power-scores-2018-23607ddf297a>`_
de Jeff Hale nous a permis d'avoir une comparaison de l’utilisation,
de l’intérêt et de la popularité des différentes bibliothèques python.

Jeff Hale a regroupé tous ses résultats et en a fait un seul et
même graphique où il donne des scores à chaque bibliothèque.
Sur ce graphique il est possible de voir que TensorFlow est largement plus utilisé que les autres.
Cependant, il faut prendre en compte le fait que TensorFlow est en quelques sortes
une amélioration / surcouche de Keras et que Keras éxiste depuis plus longtemps que Pytorch et TensorFlow.

On peut par exemple proposé que les personnes utilisants Keras migre de plus en plus vers Tensorflow
sachant que certaines personnes (du fait de sa simplicité) commencer directement le Deep Learning avec Tensorflow.
PyTorch, d’un autre côté, est plus compliqué et est utilisé dans des cas un peu plus particulier
car permet plus de personnalisation. Enfin, Theano est classé dernier mais cela semble logique
du fait que c’est une des premières bibliothèques python permettant de faire du Deep Learning et qui est,
par conséquent, moins performante et dispose de moins de fonctionnalités. Theano est aussi plus
difficile à prendre en main et par conséquent est nettement moins utilisé.

.. image:: ../Site/pictures/Score_de_puissance.png

