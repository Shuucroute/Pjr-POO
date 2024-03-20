import menu
import game

# Créer une instance de dé
# dice = Dice(color="black", faces=6) # Cette ligne n'est pas nécessaire car vous n'utilisez pas Dice dans le main

# Afficher le menu principal et choisir un personnage
player, ally = menu.select_character()

# Si aucun personnage n'est sélectionné, afficher un message et quitter
if player is None:
    print("Aucun personnage n'a été sélectionné.")
    exit()

    

game.start_game()