from character import Character, Warrior, Mage, Thief, Archer, Druid
from ennemis import Zombie, Skeletons, Goblins, Trolls
from dice import Dice

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
            enemy = enemies[0]
            player.attack(enemy)
            if not enemy.is_alive():
                print(f"{enemy.name} has been defeated!")
                player.gain_exp(enemy.exp_reward)
                enemies.pop(0)
            else:
                print(f"{enemy.name} counter-attacks!")
                ally.attack(player)
                if not player.is_alive():
                    print(f"{player.name} has been defeated!")
                    break
                else:
                    print(f"{player.name} resisted {enemy.name}'s attack!")
        elif choice == "2":
            print("No items are available at the moment.")
        elif choice == "3":
            print("You flee the battle!")
            break
        else:
            print("Invalid action.")

def start_game():
    print("Welcome to the game!")
    player = Player("Cloud", 100, 15, 10, Dice(6), 10)
    ally = Ally("Barret", 120, 12, 8, Dice(6), 5)
    dungeons = [
        Dungeon("Dungeon 1", [
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
