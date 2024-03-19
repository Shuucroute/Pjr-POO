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
        print("3. Flee")
        choice = input("Enter the action number (1/2/3): ")

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
            print("You flee the battle!")
            break
        else:
            print("Invalid action.")



def start_game():
    print("Welcome to the game!")
    player, ally = menu.select_character()
    dungeons = [
        Dungeon("Dungeon 1", [
            Zombie(),
            Zombie(),
            Zombie(),
            # ...
        ]),
        # ...
    ]

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
