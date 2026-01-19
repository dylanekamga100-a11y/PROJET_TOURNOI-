import json
import os

def initialiser_donnees():
    # Définition des fichiers et de leur structure initiale
    fichiers = {
        "joueurs.json": [],
        "tournoi_en_cours.json": {},
        "historique_tournois.json": []
    }

    for nom_fichier, contenu in fichiers.items():
        # On ne crée le fichier que s'il n'existe pas encore
        if not os.path.exists(nom_fichier):
            with open(nom_fichier, 'w', encoding='utf-8') as f:
                json.dump(contenu, f, indent=4)
            print(f"✅ Fichier créé : {nom_fichier}")
        else:
            print(f"ℹ️ Le fichier {nom_fichier} existe déjà (non modifié).")

if __name__ == "__main__":
    initialiser_donnees() 