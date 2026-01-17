import json
import os

FICHIER_SAUVEGARDE = "sauvegarde.json"


def sauvegarder_tournoi(etat):
    """
    Sauvegarde l'état du tournoi dans un fichier JSON.
    etat : dictionnaire contenant les informations du tournoi
    """
    with open(FICHIER_SAUVEGARDE, "w", encoding="utf-8") as f:
        json.dump(etat, f, indent=4, ensure_ascii=False)


def charger_tournoi():
    """
    Charge l'état du tournoi depuis le fichier JSON.
    Retourne un dictionnaire ou None s'il n'y a pas de sauvegarde.
    """
    if os.path.exists(FICHIER_SAUVEGARDE):
        with open(FICHIER_SAUVEGARDE, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def supprimer_sauvegarde():
    """
    Supprime la sauvegarde (utile quand le tournoi est terminé).
    """
    if os.path.exists(FICHIER_SAUVEGARDE):
        os.remove(FICHIER_SAUVEGARDE)