.. title:: Bibliotèques python

Présentation de différentes bibliotèques
========================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Avans-propos
************

Avant de vous présenter les principales bibliothèques python permettant de faire du Deep-Learning,
il faut savoir qu’une bibliothèque scientifique appelé NumPy est utilisée
dans toutes les bibliothèques qui vont suivre. NumPy permet certes,
d’avoir un affichage graphique, mais son attrait principal réside dans la création
et la manipulation de matrice à n dimension (noté numpy.array).

`Page d'accueil NumPy <http://www.numpy.org/>`_

Keras
*********

**Description**

Sûrement la bibliothèque python la plus aimé car elle est simple d’utilisation.
C’est une très bonne base et c’est pour cette raison que d’autres bibliothèques
tels que TensorFlow ou Theano sont basées sur Keras. Le problème est que sa simplicité
rends plus difficile les modifications particulières et c’est une des raisons qui pousse
les programmeurs à utiliser des surcouches (TensorFlow et Theano).

`Page d'accueil Keras <https://keras.io/>`_

Theano
***********

**Description**

Une bibliothèque basée sur Keras qui ajoute quelques fonctionnalités.
Elle a été créé il y a longtemps et c’est pour cette raisons que de moins en moins de personnes l’utilisent.
En effet, du fait de sa "vieillesse" son utilisation est moins trivial et moins de
fonctionnalités sont implémentés par rapport à TensorFlow. Theano est vouée à disparaître puisque
étant de moins en moins utilisé, presque plus personne ne le met à jour ce qui a
pour conséquence de ne pas attirer de nouvelles personnes.

`Page d'accueil Theano <http://deeplearning.net/software/theano/index.html>`_

TensorFlow
**********

**Description**

Bibliothèque la plus utilisée, elle se sert de Keras et en améliore les possibilitées de
personnalisations et en simplifie le débogage. C’est en somme une surcouche de Keras qui a le mérite
d’être simplifiée. TensorFlow est une bibliothèque open source développée par une équipe de Google (Google Brain Team).
Elle n'est pas seulement utilisée par Google mais par beaucoup d'autres grandes entreprises (Twitter, Coca-Cola, Airbus...).
Cette bibliothèque peut être utilisée pour plusieurs plateformes (ordinateurs, telephones, internet et cloud) et
est principalement utilisé dans la reconnaissance vocale ou d’image et dans les applications textuelles
comme Google Translate par exemple.
Elle a pour avantage d’être beaucoup utilisée ce qui lui permet de jouir d'une grande documentation
ainsi qu'une grande communauté de développeurs. En revanche, son point faible
est qu'elle est plus lente que les autres.

`Page d'accueil TensorFlow <https://www.tensorflow.org>`_

Pytorch
************

**Description**

Bibliothèque très complète. Elle est complexe mais permet une grande flexibilité et
une personnalisation approfondie une fois les compétences acquises.
Elle a été développée par Facebook, c’est la version Python de Torch,
elle est assez plébiscitée par les chercheurs du fait de son efficacité et
de sa rapidité pour mettre en place des modèles d’apprentissages.
Elle a pour avantage d'avoir un processus de modélisation simple et son mode de définition se rapproche beaucoup
de la programmation standard.

`Page d'accueil Pytorch <https://pytorch.org/>`_

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Comparaison de différentes bibliotèques
=======================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. toctree::
   :maxdepth: 2

Dans cette partie nous comparerons seulement les quatres bibliothèques présentées
ci-dessus car ce sont les bibliothèques Python les plus utilisées.
Il faut tout de même garder en tête que TensorFlow est basé sur Keras donc ceux
qui utilisent TensorFlow utilise aussi d’une certaine manière Keras.

La comparaison entre plusieurs bibliothèques peut se faire sous de nombreux aspects
tels que la popularité, la complexité d’utilisation, la rapidité d'exécution, etc.

Performance
***********

La performance est un point important en ce qui concerne les bibliothèque de Deep Learning.
En effet, plus elles sont performantes plus elles sont versatiles.
Cette performance peut être décomposée en différent paramètres : la vitesse d’exécution,
la facilité de prise en main, les différentes plateformes d'exécutions.
Dans le graphique ci-dessous on peut voir cette comparaison. Ce graphique
représente les différents points forts des bibliothèques donc pour ce qui est des valeurs,
le 3 représente un bon score, un 2 représente un score moyen et un 1 représente un score faible.

.. image:: ../Site/pictures/comparaison_performance.png
    :align: center

Source : Ranking Popular Deep Learning Libraries for Data Science Posted by Michael Li

On remarque que TensorFlow et PyTorch se valent. Ils sont tous deux très bon pour la modélisation CCN
mais TensorFlow est meilleur en ce qui concerne la prise en main tandis que PyTorch quant à lui est
meilleur en vitesse. Ils restent tous les deux moyens dans les autres domaines. Pour Theano,
il a de moins bon score et est moyen pour ce qui est de la modélisation CCN ainsi que la prise en main.


Popularité
**********

La contribution est elle aussi crucial car c’est un facteur déterminant lorsque l’on choisit
la bibliothèque que l’on souhaite utiliser. En effet il est plus rassurant de commencer un projet
en utilisant une bibliothèque pour laquelle il y a beaucoup de ressources sur internet que ce soit
des livres, des tutoriels ou tout simplement un nombre conséquent d’utilisateurs.
L'article `Deep Learning Framework Power Scores 2018 <https://towardsdatascience.com/deep-learning-framework-power-scores-2018-23607ddf297a>`_
de Jeff Hale nous a permis d'avoir une
comparaison de l’utilisation, de l’intérêt et de la popularité des différentes bibliothèques Python.

Le graphique ci-dessous nous montre les pourcentages de contenu que l’on peut trouver sous différentes formes
comme la recherche d’emplois, l’utilisation les activitées GitHub et le volume de recherche sur Google.

.. image:: ../Site/pictures/popularite_internet.png
    :align: center

Source : Towards Data Science

Le graphique suivant quand à lui reflète le contenu plus littéraire comme le nombre d’articles
ArXiv (site d'hébergement d'articles majoritairements universitaires sur le Machine Learning),
le nombre de livre et le nombre d’articles publiés sur `Medium <https://medium.com/topic/data-science>`_.


.. image:: ../Site/pictures/contribution_litteraire.png
    :align: center

Source : Towards Data Science

Jeff Hale a regroupé tous ses résultats et en a fait un seul et même graphique, que l’on peut retrouver ci-dessous,
où il donne des scores à chaque bibliothèque. Sur ce graphique il est possible de voir que TensorFlow est largement
plus utilisé que les autres. Cependant, il faut prendre en compte le fait que TensorFlow est en quelques sortes
une amélioration / surcouche de Keras et que Keras éxiste depuis plus longtemps que Pytorch et TensorFlow.
On peut par exemple proposer que les personnes utilisant Keras migrent de plus en plus vers Tensorflow
sachant que certaines personnes (du fait de sa simplicité) commencent directement le Deep Learning avec Tensorflow.
PyTorch, d’un autre côté, est plus compliqué et est utilisé dans des cas un peu plus particuliers
car permet plus de personnalisation. Enfin, Theano est classé dernier mais cela semble logique
du fait que c’est une des premières bibliothèques python permettant de faire du Deep Learning et qui est,
par conséquent, moins performante et dispose de moins de fonctionnalités. Theano est aussi plus difficile
à prendre en main et par conséquent, nettement moins utilisé.

.. image:: ../Site/pictures/Score_de_puissance.png
    :align: center

Source: `Deep Learning Framework Power Scores 2018 <https://towardsdatascience.com/deep-learning-framework-power-scores-2018-23607ddf297a>`_

