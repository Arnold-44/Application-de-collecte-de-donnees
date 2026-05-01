# StatEdu - Plateforme de Collecte et d'Analyse 

## 📋 Présentation du Projet
**StatEdu** est une application web développée dans le cadre de l'EC2 du cours **INF 232 (Analyse de données)** à l'UY1. L'objectif est de collecter des données précises sur les habitudes de vie et les performances académiques des étudiants pour alimenter nos futurs modèles de régression et de classification.

## 🚀 Fonctionnalités
*   **Collecte Intelligente :** Formulaire optimisé pour recueillir des variables clés (heures d'étude, réseaux sociaux, stress, moyenne).
*   **Analyse Descriptive en Temps Réel :** Visualisation immédiate des tendances via des graphiques interactifs (Scatter charts, Bar charts).
*   **Calcul de Corrélation :** Analyse automatique du lien entre l'usage des réseaux sociaux et la réussite académique.

## 🛠️ Stack Technique
*   **Langage :** Python 3.x
*   **Interface & Dashboard :** [Streamlit](https://streamlit.io/)
*   **Traitement de données :** Pandas & NumPy
*   **Base de données :** SQLite (pour la persistance et la fiabilité des données)
*   **Déploiement :** Streamlit Cloud

## ⚖️ Critères de Notation Respectés

### 1. Idée (Créativité & Imagination)
L'application ne se contente pas de stocker des noms, elle se concentre sur l'impact des **réseaux sociaux** et du **stress** sur la performance académique, un sujet crucial pour l'ingénieur en formation.

### 2. Robustesse
*   Validation des entrées : Utilisation de bornes numériques (ex: impossible d'entrer plus de 24h d'étude/jour).
*   Gestion de base de données : Utilisation de SQLite pour éviter la perte de données en cas de redémarrage du serveur.

### 3. Efficacité
*   Expérience utilisateur (UX) : Formulaire remplissable en moins de 30 secondes.
*   Dashboard "tout-en-un" : Les résultats de l'analyse descriptive sont affichés sur la même page que la collecte.

### 4. Fiabilité
*   Calculs statistiques basés sur la bibliothèque **Pandas**, garantissant une précision mathématique totale pour les moyennes et les corrélations.

## 📂 Structure du Projet
```text
.
├── app.py              # Code principal de l'application (Streamlit)
├── requirements.txt    # Liste des dépendances (pandas, streamlit...)
├── enquetes_enspd.db   # Base de données SQLite (générée au lancement)
└── README.md           # Documentation du projet
