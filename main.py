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

# Créer une instance de la classe Game
game_instance = game.Game()

# Lancer le premier donjon avec le personnage sélectionné
game_instance.start_dungeon(player, ally)
