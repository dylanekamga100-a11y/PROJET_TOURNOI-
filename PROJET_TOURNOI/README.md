 # 🏆 Système de Gestion de Tournois Multi-Jeux

C'est un projet réalisé dans le cadre d'un travail en groupe de 3 personnes permettant de jouer au morpion et au pierre-papier-ciseaux avec un système de classement Elo persistant.

## 🛠️ Fonctionnalités

- **Jeux** : Tic-Tac-Toe (grille ASCII) et PPC (variante 5 choix).

- **IA** : Niveaux Facile (aléatoire) et Difficile (stratégie).

- **Formats** : Élimination directe (Bracket) ou Round-Robin (Championnat).

- **Données** : Sauvegarde automatique et chargement via JSON.

- **Statistiques** : Historique détaillé, ratio W/L et évolution ELO.

## 📁 Structure du projet

`projet_tournoi/`
│
├──`main.py                    # Point d’entrée du programme`
├── `tournoi.py                 # Gestion du tournoi et du menu`
├── `sauvegarde.py              # Sauvegarde et chargement (JSON)`
├── `pierre_papier_ciseau.py    # Jeu Pierre Papier Ciseaux`
├── `morpion.py                 # Jeu du Morpion`
├── `.gitignore                 # Fichiers ignorés par Git`
└── `README.md                  # Présentation du projet`

## ▶️ Lancer le programme

Prérequis
	•	Python 3 installé

Exécution

Dans le dossier du projet, lancer la commande :
`python main.py`

## 💾 Sauvegarde du tournoi 

	•	Le tournoi peut être sauvegardé à tout moment
	•	Les données sont stockées dans un fichier sauvegarde.json
	•	À la relance du programme, l’utilisateur peut reprendre la partie 

Le fichier de sauvegarde est ignoré par Git grâce au .gitignore.



## 👥 Répartition du travail

	•	Membre 1 : Gestion du tournoi et sauvegarde
	•	Membre 2 : Jeu Pierre Papier Ciseaux
	•	Membre 3 : Jeu du Morpion



## 🛠️ Technologies utilisées

     •   Python 3
     •   JSON (pour la sauvegarde)
     •   Git / GitHub (travail collaboratif)

## 📅 Planning de Développement

- **Mercredi** : Conception, architecture et mise en place Git.

- **Jeudi**    : Développement des moteurs de jeu et du menu.

- **Lundi** : Gestion JSON, ELO et correction d'erreurs.

- **Mardi** : Finalisation, documentation et présentation.