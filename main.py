import menu
import game
import character
from rich.console import Console

console = Console()

def main():
    menu.show_welcome_screen()

    player, ally = menu.select_character()

    if player is None:
        console.print("Aucun personnage n'a été sélectionné.", style="bold red")
        exit()

    if isinstance(ally, character.Druid):
        ally.allies.append(player)

    while True:
        menu.select_option(player, ally)
        game.start_game(player, ally)

if __name__ == "__main__":
    main()