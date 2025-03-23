from rich.console import Console
from rich.progress import Progress, BarColumn, TextColumn
from rich.table import Table
from rich.panel import Panel
from character import Character, Warrior, Mage, Thief, Archer, Druid
from ennemis import Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton, armor_Skeletons, Goblins, big_goblins, Trolls, Olog_hai
from dice import Dice
import menu
import random
from boss import Cadaverus_Devorator, Kondylos_o_Sarantapus, Roi_Gobelin, Garrok_le_Féroce, Balrog, kill_boss, Boss

console = Console()

def show_health_bar(character):
    console.print(f"[bold green]{character.name}[/bold green]")
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
    ) as progress:
        task = progress.add_task("Vie", total=character.hp_max, completed=character.hp)
        progress.update(task, completed=character.hp)

def show_mana_bar(character):
    if hasattr(character, "mana_max"):
        console.print(f"[bold blue]{character.name}[/bold blue]")
        with Progress(
            TextColumn("[progress.description]{task.description}"),
            BarColumn(bar_width=None),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        ) as progress:
            task = progress.add_task("Mana", total=character.mana_max, completed=character.mana)
            progress.update(task, completed=character.mana)

def show_combat_menu():
    console.print("\n[bold cyan]Choisir une action:[/bold cyan]")
    table = Table(show_header=False, show_lines=True)
    table.add_column("Action", style="bold green")
    table.add_column("Description", style="bold yellow")
    table.add_row("1", "Attaquer")
    table.add_row("2", "Utiliser un objet")
    table.add_row("3", "Fuir")
    console.print(table)

def show_enemies(enemies):
    console.print("\n[bold red]Ennemis disponibles:[/bold red]")
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Numéro", style="dim", width=12)
    table.add_column("Nom", style="bold red")
    table.add_column("Vie", style="bold green")
    for i, enemy in enumerate(enemies, 1):
        table.add_row(str(i), enemy.name, f"{enemy.hp}/{enemy.hp_max}")
    console.print(table)

def combat(player, ally, enemies):
    while enemies:
        # Afficher les barres de vie et de mana
        console.print("\n[bold cyan]État des combattants:[/bold cyan]")
        show_health_bar(player)
        if ally:  # Vérifier si un allié est présent
            show_health_bar(ally)
        if isinstance(ally, Druid):
            show_mana_bar(ally)

        # Afficher le menu des actions
        show_combat_menu()
        choice = input("Entrez le numéro de l'action (1/2/3): ")

        if choice == "1":
            # Afficher les ennemis disponibles
            show_enemies(enemies)
            while True:
                try:
                    enemy_choice = input("Entrez le numéro de l'ennemi: ")
                    enemy_choice = int(enemy_choice)  # Convertir en entier
                    if 1 <= enemy_choice <= len(enemies):
                        break  # Sortir de la boucle si l'entrée est valide
                    else:
                        console.print("Numéro d'ennemi invalide. Veuillez entrer un numéro valide.", style="bold red")
                except ValueError:
                    console.print("Entrée invalide. Veuillez entrer un nombre.", style="bold red")

            enemy = enemies[enemy_choice - 1]
            console.print(f"\n[bold red]{player.name} attaque {enemy.name} ![/bold red]")
            player.attack(enemy)
            if not enemy.is_alive():
                console.print(f"[bold red]{enemy.name} a été vaincu ![/bold red]")
                player.gain_exp(enemy.exp_reward)
                player.get_coins(enemy.coins_reward)
                if isinstance(enemy, Zombie):
                    player.zombies_killed += 1
                elif isinstance(enemy, Goblins):
                    player.goblins_killed += 1
                if isinstance(enemy, Boss):
                    Boss.increase_boss_killed_count()
                enemies.pop(enemy_choice - 1)
            else:
                console.print(f"[bold red]{enemy.name} contre-attaque ![/bold red]")
                enemy.attack(player)
                if not player.is_alive():
                    console.print(f"[bold red]{player.name} a été vaincu ![/bold red]")
                    return False  # Retourne False si le joueur est mort
                else:
                    console.print(f"[bold green]{player.name} a résisté à l'attaque de {enemy.name} ![/bold green]")
        elif choice == "2":
            console.print("Aucun article n'est disponible pour le moment.", style="bold yellow")
        elif choice == "3":
            console.print("Tu fuis la bataille !", style="bold red")
            break
        else:
            console.print("Action invalide.", style="bold red")

        # Vérifier si les ennemis sont toujours en vie
        if not enemies:
            console.print("[bold green]Vous avez vaincu tous les ennemis ![/bold green]")
            check_quests(player)  # Vérifier les quêtes après le combat
            break

    return True  # Retourne True si le joueur a survécu

class Quest:
    def __init__(self, name, description, objective, reward):
        self.name = name
        self.description = description
        self.objective = objective  # Exemple : "Tuer 5 zombies"
        self.reward = reward  # Exemple : {"exp": 100, "coins": 50}
        self.completed = False

    def check_completion(self, player):
        if not self.completed:
            if self.objective == "Tuer 5 zombies" and player.zombies_killed >= 5:
                self.completed = True
                player.gain_exp(self.reward["exp"])
                player.get_coins(self.reward["coins"])
                console.print(f"Quête '{self.name}' terminée !", style="bold green")

def check_quests(player):
    """
    Vérifie si le joueur a accompli des quêtes.
    """
    for quest in quests:
        quest.check_completion(player)

# Exemple de quête
quests = [
    Quest(
        name="La Menace Zombie",
        description="Tuez 5 zombies pour protéger le village.",
        objective="Tuer 5 zombies",
        reward={"exp": 100, "coins": 50},
    ),
    Quest(
        name="Le Trésor des Gobelins",
        description="Tuez 3 gobelins pour récupérer leur trésor.",
        objective="Tuer 3 gobelins",
        reward={"exp": 150, "coins": 75},
    ),
]

class Dungeon:
    def __init__(self, name):
        self.name = name
        self.floors = []

    def add_floor(self, enemies):
        self.floors.append(enemies)

def start_game(player, ally):
    console.print("Bienvenue dans le jeu !", style="bold blue")
    while True:  # Boucle principale pour redémarrer le jeu si le joueur choisit de recommencer
        dungeon1 = Dungeon("Donjon Zombie")
        dungeon2 = Dungeon("Donjon Squelettes")
        dungeon3 = Dungeon("Donjon Gobelins")
        dungeon4 = Dungeon("Donjon Trolls")
        
        # Ajout des étages avec les ennemis correspondants
        dungeon1.add_floor([Zombie.create_enemy() for _ in range(3)])  # Etage 1 avec des Zombies
        dungeon1.add_floor([Zombie2_0.create_enemy() for _ in range(3)])  # Etage 2 avec des Zombie2_0
        dungeon1.add_floor([Zombie_guerrier.create_enemy() for _ in range(3)])  # Etage 3 avec des Zombie_guerrier
        if random.random() < 0.4:
            dungeon1.add_floor([Cadaverus_Devorator.create_boss()])  # Etage 4 avec un boss

        for floor_num, enemies in enumerate(dungeon1.floors, start=1):
            console.print(f"Tu rentres dans le {dungeon1.name}, étage {floor_num}!", style="bold cyan")
            if not combat(player, ally, enemies):  # Si le joueur meurt, afficher le menu de mort
                choice = menu.show_death_menu()
                if choice == "restart":
                    player.reset_stats()  # Réinitialiser les stats du joueur
                    if ally:
                        ally.reset_stats()  # Réinitialiser les stats de l'allié
                    break  # Recommencer le jeu
                elif choice == "quit":
                    return  # Quitter le jeu
            # Réinitialisation de la vie et de la mana entre les étages
            player.reset_stats()
            if ally:  # Vérifier si un allié est présent avant de réinitialiser ses stats
                ally.reset_stats()
            if floor_num < len(dungeon1.floors):
                console.print("Passons à l'étage suivant...", style="bold cyan")
                input("Appuyez sur Entrée pour continuer...")
        else:
            console.print("Félicitations ! Vous avez vaincu tous les étages du donjon Zombie.", style="bold green")
            break  # Sortir de la boucle si le joueur a terminé le donjon
        
        dungeon2.add_floor([Skeletons.create_enemy() for _ in range(3)])
        dungeon2.add_floor([Reinforced_Skeleton.create_enemy() for _ in range(3)])
        dungeon2.add_floor([armor_Skeletons.create_enemy() for _ in range(3)])
        if random.random() < 0.4:
            dungeon2.add_floor([Kondylos_o_Sarantapus.create_boss()])
        for floor_num, enemies in enumerate(dungeon2.floors, start=1):
            console.print(f"Tu rentres dans le {dungeon2.name}, étage {floor_num}!", style="bold cyan")
            if not combat(player, ally, enemies):  # Si le joueur meurt, afficher le menu de mort
                choice = menu.show_death_menu()
                if choice == "restart":
                    player.reset_stats()  # Réinitialiser les stats du joueur
                    if ally:
                        ally.reset_stats()  # Réinitialiser les stats de l'allié
                    break  # Recommencer le jeu
                elif choice == "quit":
                    return  # Quitter le jeu
            # Réinitialisation de la vie et de la mana entre les étages
            player.reset_stats()
            if ally:  # Vérifier si un allié est présent avant de réinitialiser ses stats
                ally.reset_stats()
            if floor_num < len(dungeon2.floors):
                console.print("Passons à l'étage suivant...", style="bold cyan")
                input("Appuyez sur Entrée pour continuer...")
        else:
            console.print("Félicitations ! Vous avez vaincu tous les étages du donjon squelettes.", style="bold green")
            break  # Sortir de la boucle si le joueur a terminé le donjon
        
        dungeon3.add_floor([Goblins.create_enemy() for _ in range(3)])
        dungeon3.add_floor([big_goblins.create_enemy() for _ in range(3)])
        if random.random() < 0.4:
            dungeon3.add_floor([Roi_Gobelin.create_boss()])
        for floor_num, enemies in enumerate(dungeon3.floors, start=1):
            console.print(f"Tu rentres dans le {dungeon3.name}, étage {floor_num}!", style="bold cyan")
            if not combat(player, ally, enemies):  # Si le joueur meurt, afficher le menu de mort
                choice = menu.show_death_menu()
                if choice == "restart":
                    player.reset_stats()  # Réinitialiser les stats du joueur
                    if ally:
                        ally.reset_stats()  # Réinitialiser les stats de l'allié
                    break  # Recommencer le jeu
                elif choice == "quit":
                    return  # Quitter le jeu
            # Réinitialisation de la vie et de la mana entre les étages
            player.reset_stats()
            if ally:  # Vérifier si un allié est présent avant de réinitialiser ses stats
                ally.reset_stats()
            if floor_num < len(dungeon3.floors):
                console.print("Passons à l'étage suivant...", style="bold cyan")
                input("Appuyez sur Entrée pour continuer...")
        else:
            console.print("Félicitations ! Vous avez vaincu tous les étages du donjon Gobelins.", style="bold green")
            break  # Sortir de la boucle si le joueur a terminé le donjon
        
        dungeon4.add_floor([Trolls.create_enemy() for _ in range(3)])
        dungeon4.add_floor([Olog_hai.create_enemy() for _ in range(3)])
        if random.random() < 0.4:
            dungeon4.add_floor([Garrok_le_Féroce.create_boss()])
        for floor_num, enemies in enumerate(dungeon4.floors, start=1):
            console.print(f"Tu rentres dans le {dungeon4.name}, étage {floor_num}!", style="bold cyan")
            if not combat(player, ally, enemies):  # Si le joueur meurt, afficher le menu de mort
                choice = menu.show_death_menu()
                if choice == "restart":
                    player.reset_stats()  # Réinitialiser les stats du joueur
                    if ally:
                        ally.reset_stats()  # Réinitialiser les stats de l'allié
                    break  # Recommencer le jeu
                elif choice == "quit":
                    return  # Quitter le jeu
            # Réinitialisation de la vie et de la mana entre les étages
            player.reset_stats()
            if ally:  # Vérifier si un allié est présent avant de réinitialiser ses stats
                ally.reset_stats()
            if floor_num < len(dungeon4.floors):
                console.print("Passons à l'étage suivant...", style="bold cyan")
                input("Appuyez sur Entrée pour continuer...")
        else:
            console.print("Félicitations ! Vous avez vaincu tous les étages du donjon Trolls.", style="bold green")
            break  # Sortir de la boucle si le joueur a terminé le donjon