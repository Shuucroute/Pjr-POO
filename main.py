import sys
import character
import random
from dice import Dice
import ennemis
import menu

# Créer une instance de dé
dice = Dice(color="black", faces=6)

# Appeler la fonction show_main_menu depuis le fichier menu.py pour afficher le menu principal du jeu
menu.show_main_menu()

# Afficher une invite pour entrer une réponse
choice = input("Entrez votre choix : ")

# Appeler la fonction select_character depuis le fichier menu.py et passer en argument la variable player
if choice == "1":
    player = menu.select_character()

    # Créer des instances de personnages
    if player is not None:
        enemy = random.choice(ennemis.ENNEMIES).create_enemy(dice)

        # Faire combattre le joueur et l'ennemi
        player.attack(enemy)

        # Afficher les caractéristiques des personnages
        print(player)
        print(enemy)
    else:
        print("Aucun personnage n'a été sélectionné.")
elif choice == "2":
    print("Chargement d'une partie...")
    # Ajouter la logique de chargement de la partie ici
elif choice == "3":
    print("Au revoir !")
    sys.exit()
else:
    print("Choix invalide")