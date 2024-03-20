import menu
import game

# Afficher le menu principal et choisir un personnage
player, ally = menu.select_character()

# Si aucun personnage n'est sélectionné, afficher un message et quitter
if player is None:
    print("Aucun personnage n'a été sélectionné.")
    exit()

# Lancer le jeu avec le personnage et l'allié sélectionnés
game.start_game(player,ally)
