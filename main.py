import menu
import game
import character


# Afficher le menu principal et choisir un personnage
player, ally = menu.select_character()

# Si aucun personnage n'est sélectionné, afficher un message et quitter
if player is None:
    print("Aucun personnage n'a été sélectionné.")
    exit()

# Ajouter le personnage principal à la liste d'alliés si l'allié est un druide
if isinstance(ally, character.Druid):
    ally.allies.append(player)

# Lancer le jeu avec le personnage et l'allié sélectionnés
menu.select_option(player)
game.start_game(player, ally)
