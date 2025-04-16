## Projet d'Analyse des Performances Scolaires à NYC 👨🏻‍🎓
#### Description
Ce projet analyse les performances des écoles de New York City (NYC) aux tests SAT de mathématiques, lecture et écriture. L'analyse se concentre sur l'identification des meilleures écoles en mathématiques, les établissements les plus performants globalement, et explore les différences entre les arrondissements (boroughs) de NYC.

<img width="474" alt="Capture d’écran 2025-04-16 à 20 25 13" src="https://github.com/user-attachments/assets/aca78b71-c16a-4c9d-87a6-5ea2dbb40ec1" />


#### Données
L'analyse utilise le fichier schools.csv qui contient des informations sur les écoles de NYC, incluant:

- Noms des écoles (school_name)
- Arrondissement (borough)
- Scores moyens aux tests SAT:

- Mathématiques (average_math)
  - Lecture (average_reading)
  - Écriture (average_writing)


#### Analyses Réalisées
##### 1. Meilleures Écoles en Mathématiques

- Filtrage des écoles ayant un score moyen en mathématiques supérieur à 640
- Classement par ordre décroissant des scores

<img width="703" alt="Capture d’écran 2025-04-16 à 20 30 07" src="https://github.com/user-attachments/assets/cb3725cd-c6c3-4203-a04f-0ec42bd47c88" />


##### 2. Top 10 des Écoles Globalement

- Calcul du score SAT total (mathématiques + lecture + écriture) pour chaque école
- Identification et classement des 10 écoles les plus performantes

  <img width="575" alt="Capture d’écran 2025-04-16 à 20 23 39" src="https://github.com/user-attachments/assets/5f640544-0a0f-46ad-abbb-0ed0c5cb489a" />


##### 3. Analyse par Arrondissement (Borough)

- Calcul et comparaison de l'écart-type des scores SAT totaux par arrondissement
- Identification de l'arrondissement avec la plus grande variabilité (Manhattan)
- Analyse détaillée de Manhattan:
  - Nombre d'écoles
  - Score SAT total moyen
  - Écart-type des scores SAT totaux

<img width="829" alt="Capture d’écran 2025-04-16 à 20 23 48" src="https://github.com/user-attachments/assets/c16444b3-37d3-4646-81c7-9b05665c4ed0" />


#### Résultats Clés

- Liste des écoles les plus performantes en mathématiques (scores > 640)
- Top 10 des écoles basé sur les scores SAT combinés
- Manhattan présente la plus grande variabilité dans les performances scolaires
- Statistiques détaillées sur les 127 écoles de Manhattan:
  - Score SAT total moyen: 1340.13
  - Écart-type: 230.29



#### Technologies Utilisées

- Python
- Pandas (manipulation et analyse des données)
- Techniques d'agrégation et de regroupement
- Calculs statistiques (moyenne, écart-type)

#### Comment Utiliser ce Projet

1. Clonez ce dépôt
2. Assurez-vous que la bibliothèque Pandas est installée
3. Exécutez le script principal pour reproduire l'analyse

#### Perspectives et Applications
Cette analyse peut être utile pour:
  - Les parents cherchant les meilleures écoles pour leurs enfants
  - Les responsables éducatifs analysant les performances par quartier
  - Les chercheurs étudiant les inégalités éducatives à NYC

#### Auteur 🙆🏻‍♀️
Nana CHEN - [Mail](cxxnana@gmail.com) - [LinkedIn](https://www.linkedin.com/in/cxxhime/)

#### Remarques
Ce projet a été réalisé dans le cadre d'un exercice DataCamp visant à démontrer les compétences en analyse de données avec Python et Pandas.
