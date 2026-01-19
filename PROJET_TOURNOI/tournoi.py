from pierre_papier_ciseau import jouer_pierre_papier_ciseau
from morpion import jouer_morpion
from sauvegarde import charger_tournoi, sauvegarder_tournoi, supprimer_sauvegarde



def afficher_menu():
    print("\n🎮 MENU DU TOURNOI 🎮")
    print("1 - Pierre Papier Ciseaux")
    print("2 - Morpion")
    print("3 - Sauvegarder et quitter")
    print("0 - Quitter sans sauvegarder")


def lancer_tournoi():

    print("🎮 Bienvenue au tournoi 🎮")

    etat = charger_tournoi()

    if etat is None:
        etat = {}
        
    elif etat: 
        reprendre = input("Une sauvegarde existe. Reprendre ? (o/n) : ")
        if reprendre.lower() != "o":
            etat = {}

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            jouer_pierre_papier_ciseau()
            etat["dernier_jeu"] = "pfc"

        elif choix == "2":
            jouer_morpion()
            etat["dernier_jeu"] = "morpion"

        elif choix == "3":
            sauvegarder_tournoi(etat)
            print("Tournoi sauvegardé ✔")
            break

        elif choix == "0":
            supprimer_sauvegarde()
            print("Fin du tournoi 👋")
            break

        else:
            print("Choix invalide ❌")