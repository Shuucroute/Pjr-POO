from character import Character, Warrior, Mage, Thief, Archer, Druid
from ennemis import Zombie, Skeletons, Goblins, Trolls
from dice import Dice
import menu

class Player(Character):
    def __init__(self, name, health, attack, defense, dice, exp_reward):
        super().__init__(name, health, attack, defense, dice, exp_reward)

class Ally(Character):
    def __init__(self, name, health, attack, defense, dice, exp_reward):
        super().__init__(name, health, attack, defense, dice, exp_reward)

class Dungeon:
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

def combat(player, ally, enemies):
    while enemies:
        print("\nChoose an action:")
        print("1. Attack")
        print("2. Use item")
        print("3. Ask ally to heal (Druid only)")
        print("4. Flee")
        choice = input("Enter the action number (1/2/3/4): ")

        if choice == "1":
            print("\nChoose an enemy to attack:")
            for i, enemy in enumerate(enemies, 1):
                print(f"{i}. {enemy.name}")
            enemy_choice = int(input("Enter the enemy number: "))
            if 1 <= enemy_choice <= len(enemies):
                enemy = enemies[enemy_choice - 1]
                player.attack(enemy)
                if not enemy.is_alive():
                    print(f"{enemy.name} has been defeated!")
                    player.gain_exp(enemy.exp_reward)
                    enemies.pop(enemy_choice - 1)
                else:
                    print(f"{enemy.name} counter-attacks!")
                    if ally:
                        print("\nChoose an enemy for your ally to attack:")
                        for i, enemy in enumerate(enemies, 1):
                            print(f"{i}. {enemy.name}")
                        ally_enemy_choice = int(input("Enter the enemy number: "))
                        if 1 <= ally_enemy_choice <= len(enemies):
                            ally_enemy = enemies[ally_enemy_choice - 1]
                            ally.attack(ally_enemy)
                            if not ally_enemy.is_alive():
                                print(f"{ally_enemy.name} has been defeated!")
                                ally.gain_exp(ally_enemy.exp_reward)
                                enemies.pop(ally_enemy_choice - 1)
                            else:
                                print(f"{ally_enemy.name} counter-attacks!")
                                player.defense(ally_enemy.attack_value, ally_enemy)
                                if not player.is_alive():
                                    print(f"{player.name} has been defeated!")
                                    break
                                else:
                                    print(f"{player.name} resisted {ally_enemy.name}'s attack!")
                        else:
                            print("Invalid enemy number.")
                    else:
                        print("You have no ally.")
            else:
                print("Invalid enemy number.")
        elif choice == "2":
            print("No items are available at the moment.")
        elif choice == "3":
            if isinstance(ally, Druid):
                if ally.mana >= 0:
                    ally.cast_spell(player)
                else:
                    print("Your ally doesn't have enough mana to heal you.")
            else:
                print("Your ally can't heal you.")
        elif choice == "4":
            print("You flee the battle!")
            break
        else:
            print("Invalid action.")

        # Vérifier si les ennemis sont toujours en vie
        if not enemies:
            print("You have defeated all enemies!")
            break

        # Le Druid lance un sort sur le joueur pour le soigner
        if isinstance(ally, Druid) and ally.mana >= ally.get_mana_max():
            ally.cast_spell(player)

        # Afficher la barre de mana du Druid
        if isinstance(ally, Druid):
            ally.show_manabar()

        # Vérifier si les ennemis sont toujours en vie
        if not enemies:
            print("You have defeated all enemies! ou")
            break

def start_game(player, ally):
    print("Bienvenue dans le jeu !")
    dungeons = []
    dungeons.append(
        Dungeon("Donjon 1", [
            Zombie(),
            Zombie(),
            Zombie(),
            # ...
        ]))
    dungeons.append(
        Dungeon("Donjon 2", [
            Zombie(),
            Zombie(),
            Zombie(),
            # ...
        ]))
    dungeons.append(
        Dungeon("Donjon 3", [
            Zombie(),
            Zombie(),
            Zombie(),
            # ...
        ]))
    dungeons.append(
        Dungeon("Donjon 4", [
            Zombie(),
            Zombie(),
            Zombie(),
            # ...
        ]))
    dungeons.append(
        Dungeon("Donjon 5", [
            Zombie(),
            Zombie(),
            Zombie(),
            # ...
        ]))

    for dungeon in dungeons:
        print(f"You enter the {dungeon.name}!")
        combat(player, ally, dungeon.enemies)
        if not player.is_alive():
            print("You have been defeated! Game over.")
            break
        elif not ally.is_alive():
            print("Your ally has been defeated! Game over.")
            break
        else:
            print(f"You have defeated the {dungeon.name}! Moving on to the next dungeon...")
            # Add logic here to move on to the next dungeon
            input("Press Enter to continue...")

if __name__ == "__main__":
    start_game()
