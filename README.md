## Analyse des Interventions des Services d'Incendie et de Secours

**Description du Projet**

Ce projet vise à analyser les interventions réalisées par les services d'incendie et de secours en France en 2022. En utilisant des méthodes statistiques et des outils de data science, nous avons étudié les tendances, les facteurs influençant les interventions et les zones géographiques les plus concernées.

**Objectifs**

- Analyser les tendances des interventions en fonction du type d'urgence.

- Étudier les facteurs influençant ces interventions (zones géographiques, conditions climatiques, densité de population, etc.).

- Vérifier plusieurs hypothèses concernant la fréquence et la localisation des interventions.

- Créer des visualisations interactives pour mieux représenter les données.

**Données Utilisées**

- Source : data.gouv.fr

    - 99 lignes et 71 colonnes recensant les interventions.

**Variables clés :**

- Temporelles : année d’intervention.

- Géographiques : zone, région, département.

- Types d’intervention : incendies, accidents, secours à personnes, inondations, etc.

- Détails spécifiques : nombre total d’interventions.

**Structure du Projet**

- data
    - data2022.csv  : dataset sur lequel on travaille
- Projet.ipynb      : Notebook principal contenant notre analyse  
- README.md         : Documentation du projet


**Instructions d'Installation**

- Cloner le projet
```bash
git clone https://github.com/votre-utilisateur/projet-incendie.git
cd projet-incendie
```

Installer les dépendances
```bash
pip install -r requirements.txt
```

Lancer le Notebook Jupyter

jupyter notebook notebooks/Projet.ipynb

**Résultats Clés**

- Les secours à personne et secours à victime sont les interventions les plus fréquentes.

- Les zones les plus concernées sont l'Île-de-France, l'Auvergne-Rhône-Alpes et Provence-Alpes-Côte d'Azur.

**Hypothèses validées :**

- Plus d'incendies dans le Sud en raison du climat.

- Plus de pollution en Île-de-France comparée à la Franche-Comté.

**Hypothèses réfutées :**

- Pas de différences significatives entre les inondations en Hauts-de-France et en Bretagne.

- Les secours en montagne sont beaucoup plus nombreux en Auvergne-Rhône-Alpes qu'en Corse.

**Contributions**

Projet réalisé par Emma Stievenard et Clément Szewczyk dans le cadre du cours de Probabilités et Statistiques.
