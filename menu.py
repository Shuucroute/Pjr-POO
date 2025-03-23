import sys
import json
import os
import character
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from dice import Dice
from shop import *

console = Console()

def show_welcome_screen():
    title_art = """
    ██╗     ███████╗ ██████╗ ███████╗███╗   ██╗██████╗ ███████╗ █████╗ 
    ██║     ██╔════╝██╔════╝ ██╔════╝████╗  ██║██╔══██╗██╔════╝██╔══██╗
    ██║     █████╗  ██║  ███╗█████╗  ██╔██╗ ██║██║  ██║█████╗  ███████║
    ██║     ██╔══╝  ██║   ██║██╔══╝  ██║╚██╗██║██║  ██║██╔══╝  ██╔══██║
    ███████╗███████╗╚██████╔╝███████╗██║ ╚████║██████╔╝███████╗██║  ██║
    ╚══════╝╚══════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝
    """
    
    welcome_message = Text("Bienvenue dans le monde des héros et des monstres !", style="bold blue")
    
    console.print(Panel.fit(title_art, style="bold red"))
    console.print(Panel.fit(welcome_message, style="bold green"))
    input("Appuyez sur Entrée pour commencer...")

def save_game(player, ally):
    save_data = {
        "player": {
            "name": player.name,
            "hp": player.hp,
            "hp_max": player.hp_max,
            "attack_value": player.attack_value,
            "defense_value": player.defense_value,
            "exp": player.exp,
            "level": player.level,
            "coins": player.coins,
            "inventory": [item.name for item in player.inventory],
        },
        "ally": {
            "name": ally.name if ally else None,
            "hp": ally.hp if ally else None,
            "hp_max": ally.hp_max if ally else None,
            "attack_value": ally.attack_value if ally else None,
            "defense_value": ally.defense_value if ally else None,
            "exp": ally.exp if ally else None,
            "level": ally.level if ally else None,
            "coins": ally.coins if ally else None,
        },
    }
    with open("save_game.json", "w") as save_file:
        json.dump(save_data, save_file)
    console.print("Partie sauvegardée avec succès !", style="bold green")

def load_game():
    if not os.path.exists("save_game.json"):
        console.print("Aucune sauvegarde trouvée.", style="bold red")
        return None, None

    with open("save_game.json", "r") as save_file:
        save_data = json.load(save_file)

    player_data = save_data["player"]
    player = character.Character(
        player_data["name"],
        player_data["hp_max"],
        player_data["attack_value"],
        player_data["defense_value"],
        Dice(6),
        exp_reward=1,
        coins_reward=1,
    )
    player.hp = player_data["hp"]
    player.exp = player_data["exp"]
    player.level = player_data["level"]
    player.coins = player_data["coins"]
    player.inventory = [item for item in player_data["inventory"]]

    ally_data = save_data["ally"]
    ally = None
    if ally_data["name"]:
        ally = character.Character(
            ally_data["name"],
            ally_data["hp_max"],
            ally_data["attack_value"],
            ally_data["defense_value"],
            Dice(6),
            exp_reward=1,
            coins_reward=1,
        )
        ally.hp = ally_data["hp"]
        ally.exp = ally_data["exp"]
        ally.level = ally_data["level"]
        ally.coins = ally_data["coins"]

    console.print("Partie chargée avec succès !", style="bold green")
    return player, ally

def show_main_menu():
    console.print(Panel.fit("Bienvenue dans Légendes d'Etheria !", style="bold blue"))
    console.print("1. Nouvelle partie", style="bold green")
    console.print("2. Charger une partie", style="bold yellow")
    console.print("3. Quitter", style="bold red")

def select_character():
    show_main_menu()
    while True:
        choice = input("Entrez votre choix : ")
        if choice == "1":
            name = input("Entrez le nom de votre personnage : ")
            character_class = choose_character_class()
            recruit_ally = input("Voulez-vous recruter un allié? (oui/non) : ").lower()
            if recruit_ally in ["o", "oui"]:
                ally = choose_ally(character_class)
            else:
                ally = None
                console.print("Vous avez choisi de ne pas recruter d'allié.", style="bold yellow")
            player = create_main_character(name, character_class)
            console.print("Personnage principal créé avec succès !", style="bold green")
            break
        elif choice == "2":
            player, ally = load_game()
            if player is None:
                continue
            break
        elif choice == "3":
            console.print("Au revoir !", style="bold red")
            sys.exit()
        else:
            console.print("Choix invalide. Veuillez entrer une option valide (1, 2 ou 3).", style="bold red")
    return player, ally

def choose_character_class():
    console.print("Choisissez votre classe :", style="bold blue")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Numéro", style="dim", width=12)
    table.add_column("Classe", style="bold green")
    table.add_row("1", "Archer")
    table.add_row("2", "Thief")
    table.add_row("3", "Warrior")
    table.add_row("4", "Mage")
    console.print(table)

    while True:
        choice = input("Entrez le numéro correspondant à votre classe : ")
        if choice == "1":
            return "archer"
        elif choice == "2":
            return "thief"
        elif choice == "3":
            return "warrior"
        elif choice == "4":
            return "mage"
        else:
            console.print("Classe invalide.", style="bold red")

def create_main_character(name, character_class):
    if character_class == "archer":
        return character.Archer(name, 30, 10, 5, Dice(6), exp_reward=1, coins_reward=1)
    elif character_class == "thief":
        return character.Thief(name, 32, 10, 4, Dice(6), exp_reward=1, coins_reward=1)
    elif character_class == "warrior":
        return character.Warrior(name, 35, 12, 8, Dice(6), exp_reward=1, coins_reward=1)
    elif character_class == "mage":
        return character.Mage(name, 30, 12, 3, Dice(6), exp_reward=1, coins_reward=1)

def choose_ally(character_class):
    console.print("Choisissez un allié avec des caractéristiques similaires à votre classe principale :", style="bold blue")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Numéro", style="dim", width=12)
    table.add_column("Classe", style="bold green")
    table.add_row("1", "Archer")
    table.add_row("2", "Druid")
    table.add_row("3", "Thief")
    table.add_row("4", "Warrior")
    table.add_row("5", "Mage")
    table.add_row("0", "Ne pas recruter d'allié")
    console.print(table)

    while True:
        choice = input("Entrez le numéro correspondant à la classe de votre allié : ")
        if choice == "0":
            console.print("Vous avez choisi de ne pas recruter d'allié.", style="bold yellow")
            return None
        elif choice == "1":
            console.print("Vous avez choisi d'avoir un allié Archer.", style="bold green")
            return character.Archer("Ally", 100, 10, 5, Dice(6), exp_reward=1, coins_reward=1)
        elif choice == "2":
            console.print("Vous avez choisi d'avoir un allié Druid.", style="bold green")
            return character.Druid("Ally", 120, 0, 6, 20, Dice(6), 1, 5, coins_reward=1)
        elif choice == "3":
            console.print("Vous avez choisi d'avoir un allié Thief.", style="bold green")
            return character.Thief("Ally", 80, 12, 4, Dice(6), exp_reward=1, coins_reward=1)
        elif choice == "4":
            console.print("Vous avez choisi d'avoir un allié Warrior.", style="bold green")
            return character.Warrior("Ally", 150, 6, 8, Dice(6), exp_reward=1, coins_reward=1)
        elif choice == "5":
            console.print("Vous avez choisi d'avoir un allié Mage.", style="bold green")
            return character.Mage("Ally", 80, 15, 3, Dice(6), exp_reward=1, coins_reward=1)
        else:
            console.print("Choix invalide.", style="bold red")

def show_game_menu():
    console.print(Panel.fit("Menu secondaire :", style="bold blue"))
    console.print("1. Accès au donjon", style="bold green")
    console.print("2. Shop", style="bold yellow")
    console.print("3. Sauvegarder", style="bold cyan")
    console.print("4. Quitter", style="bold red")

def select_option(player, ally):
    show_game_menu()
    while True:
        choice = input("Entrez votre choix : ")
        if choice == "1":
            console.print("Vous avez choisi d'accéder au donjon.", style="bold green")
            break
        elif choice == "2":
            console.print("Vous avez choisi d'aller au magasin.", style="bold yellow")
            shop = Shop()
            shop.display_shop(player)
            buy_choice = input("Entrez le numéro de l'article que vous souhaitez acheter : ")
            try:
                buy_choice = int(buy_choice) - 1
                item = shop.items[buy_choice]
                if player.coins >= item.price:
                    player.coins -= item.price
                    player.inventory.append(item)
                    console.print(f"Vous avez acheté {item.name} pour {item.price} pièces d'or.", style="bold green")
                else:
                    console.print("Vous n'avez pas assez d'argent pour acheter cet article.", style="bold red")
            except (ValueError, IndexError):
                console.print("Choix invalide.", style="bold red")
            break
        elif choice == "3":
            save_game(player, ally)
        elif choice == "4":
            console.print("Au revoir !", style="bold red")
            sys.exit()
        else:
            console.print("Choix invalide. Veuillez entrer une option valide (1, 2, 3 ou 4).", style="bold red")

def show_death_menu():
    console.print(Panel.fit("Vous êtes mort ! Que souhaitez-vous faire ?", style="bold red"))
    console.print("1. Recommencer", style="bold green")
    console.print("2. Quitter", style="bold red")
    while True:
        choice = input("Entrez votre choix : ")
        if choice == "1":
            return "restart"
        elif choice == "2":
            console.print("Fermeture du jeu...", style="bold red")
            sys.exit()  # Fermer le jeu
        else:
            console.print("Choix invalide. Veuillez entrer 1 ou 2.", style="bold red")