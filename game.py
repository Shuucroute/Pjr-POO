from character import Character, Warrior, Mage, Thief, Archer, Druid
from ennemis import Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton, armor_Skeletons, Goblins, big_goblins, Trolls, Olog_hai
from dice import Dice
import menu
import random
from boss import Cadaverus_Devorator, Kondylos_o_Sarantapus, Roi_Gobelin, Garrok_le_Féroce, Balrog, kill_boss, Boss
import random


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
        print("\nChoisir une action:")
        print("1. Attaque")
        print("2. Utilise un item")
        print("3. S'enfuir")
        choice = input("Entrez le numéro de l'action (1/2/3/4): ")

        if choice == "1":
            print("\nChoisissez un ennemi à attaquer:")
            for i, enemy in enumerate(enemies, 1):
                print(f"{i}. {enemy.name}")
            enemy_choice = int(input("Entrez le numéro de l'ennemi: "))
            if 1 <= enemy_choice <= len(enemies):
                enemy = enemies[enemy_choice - 1]
                player.attack(enemy)
                if not enemy.is_alive():
                    print(f"{enemy.name} a été vaincu !")
                    player.gain_exp(enemy.exp_reward)
                    player.get_coins(enemy.coins_reward)
                    if isinstance(enemy, Boss):
                        Boss.increase_boss_killed_count()
                    enemies.pop(enemy_choice - 1)
                else:
                    print(f"{enemy.name} contre-attaque!")
                    
                    # Attaque automatique de l'allié
                    if ally:
                        ally_attack_enemy = random.choice(enemies)
                        ally.attack(ally_attack_enemy)
                        if not ally_attack_enemy.is_alive():
                            print(f"{ally.name} a vaincu {ally_attack_enemy.name}!")
                            ally.gain_exp(ally_attack_enemy.exp_reward)
                            enemies.remove(ally_attack_enemy)
                        else:
                            print(f"{ally.name} attaque {ally_attack_enemy.name}!")
                    else:
                        print("Tu n'as pas d'allié.")
                    
                    player.defense(enemy.attack_value, enemy)
                    if not player.is_alive():
                        print(f"{player.name} a été vaincu!")
                        break
                    else:
                        print(f"{player.name} a résisté à l'attaque de {enemy.name}!")
            else:
                print("Numéro d'ennemi invalide.")
        elif choice == "2":
            print("Aucun article n'est disponible pour le moment.")
        elif choice == "3":
            print("Tu fuis la bataille!")
            break
        else:
            print("Action invalide.")

        # Vérifier si les ennemis sont toujours en vie
        if not enemies:
            print("Vous avez vaincu tous les ennemis!")
            break

        # Le Druid lance un sort sur le joueur pour le soigner
        if isinstance(ally, Druid) and ally.mana >= ally.get_mana_max():
            ally.cast_spell(player)

        # Afficher la barre de mana du Druid
        if isinstance(ally, Druid):
            ally.show_manabar()

            # Vérifier si 5 boss ont été tués et ajouter le Balrog au jeu
        if Boss.boss_killed_count >= 5:
            print("Cinqs Boss sont morts ! Le Balrog apparait !")
            enemies.append(Balrog.create_mega_boss())

        # Vérifier si les ennemis sont toujours en vie
        if not enemies:
            print("Vous avez vaincu tous les ennemis!")
            break

    # Vérifier si un boss a été tué et mettre à jour le compteur de boss tués
    for enemy in enemies[:]:  # utiliser enemies[:] pour créer une copie de la liste et éviter la modification de la liste pendant l'itération
        if isinstance(enemy, Boss) and not enemy.is_alive():
            new_enemy = Boss.increase_boss_killed_count()
            if new_enemy:  # Si new_enemy n'est pas None, c'est un Balrog
                enemies.append(new_enemy)
                break  # arrêter la boucle une fois qu'un Balrog a été ajouté
            
class Dungeon:
    def __init__(self, name):
        self.name = name
        self.floors = []

    def add_floor(self, enemies):
        self.floors.append(enemies)


def start_game(player, ally):
    print("Bienvenue dans le jeu !")
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
        print(f"Tu rentres dans le {dungeon1.name}, étage {floor_num}!")
        combat(player, ally, enemies)
        # Réinitialisation de la vie et de la mana entre les étages
        if not player or not player.is_alive():
            print("Vous avez été vaincu ! Jeu terminé.")
            break
        elif not ally or not ally.is_alive():
            print("Ton allié a été vaincu ! Jeu terminé.")
            break
        else:
            print(f"Vous avez vaincu l'étage {floor_num} du {dungeon1.name}!")
            if floor_num < len(dungeon1.floors):
                print("Passons à l'étage suivant...")
                input("Appuyez sur Entrée pour continuer...")
    else:
        print("Félicitations ! Vous avez vaincu tous les étages du donjon Zombie.")
        
    
    dungeon2.add_floor([Skeletons.create_enemy() for _ in range(3)])
    dungeon2.add_floor([Reinforced_Skeleton.create_enemy() for _ in range(3)])
    dungeon2.add_floor([armor_Skeletons.create_enemy() for _ in range(3)])
    if random.random() < 0.4:
        dungeon2.add_floor([Kondylos_o_Sarantapus.create_boss()])
    for floor_num, enemies in enumerate(dungeon2.floors, start=1):
        print(f"Tu rentres dans le {dungeon2.name}, étage {floor_num}!")
        combat(player, ally, enemies)
        player.reset_stats()
        ally.reset_stats()
        if not player or not player.is_alive():
            print("Vous avez été vaincu ! Jeu terminé.")
            break
        elif not ally or not ally.is_alive():
            print("Ton allié a été vaincu ! Jeu terminé.")
            break
        else:
            print(f"Vous avez vaincu l'étage {floor_num} du {dungeon2.name}!")
            if floor_num < len(dungeon2.floors):
                print("Passons à l'étage suivant...")
                input("Appuyez sur Entrée pour continuer...")
    else:
        print("Félicitations ! Vous avez vaincu tous les étages du donjon squelettes.")
   
    

    dungeon3.add_floor([Goblins.create_enemy() for _ in range(3)]) 
    dungeon3.add_floor([big_goblins.create_enemy() for _ in range(3)])
    if random.random() < 0.4:
        dungeon3.add_floor([Roi_Gobelin.create_boss()])  

    for floor_num, enemies in enumerate(dungeon3.floors, start=1):
        print(f"Tu rentres dans le {dungeon3.name}, étage {floor_num}!")
        combat(player, ally, enemies)
        player.reset_stats()
        ally.reset_stats()
        if not player or not player.is_alive():
            print("Vous avez été vaincu ! Jeu terminé.")
            break
        elif not ally or not ally.is_alive():
            print("Ton allié a été vaincu ! Jeu terminé.")
            break
        else:
            print(f"Vous avez vaincu l'étage {floor_num} du {dungeon3.name}!")
            if floor_num < len(dungeon3.floors):
                print("Passons à l'étage suivant...")
                input("Appuyez sur Entrée pour continuer...")
    else:
        print("Félicitations ! Vous avez vaincu tous les étages du donjon Gobelins.")


    dungeon4.add_floor([Trolls.create_enemy() for _ in range(3)])
    dungeon4.add_floor([Olog_hai.create_enemy() for _ in range(3)])
    if random.random() < 0.4:
        dungeon4.add_floor([Garrok_le_Féroce.create_boss()])

    for floor_num, enemies in enumerate(dungeon4.floors, start=1):
        print(f"Tu rentres dans le {dungeon4.name}, étage {floor_num}!")
        combat(player, ally, enemies)
        player.reset_stats()
        ally.reset_stats()
        if not player or not player.is_alive():
            print("Vous avez été vaincu ! Jeu terminé.")
            break
        elif not ally or not ally.is_alive():
            print("Ton allié a été vaincu ! Jeu terminé.")
            break
        else:
            print(f"Vous avez vaincu l'étage {floor_num} du {dungeon4.name}!")
            if floor_num < len(dungeon4.floors):
                print("Passons à l'étage suivant...")
                input("Appuyez sur Entrée pour continuer...")
    else:
        print("Félicitations ! Vous avez vaincu tous les étages du donjon Trolls.")
