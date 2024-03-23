from character import Character, Warrior, Mage, Thief, Archer, Druid
from ennemis import Zombie,Zombie2_0,Zombie_guerrier, Skeletons,Reinforced_Skeleton,armor_Skeletons ,Goblins,big_goblins ,Trolls, Olog_hai
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
                    if isinstance(enemy, Boss):
                        Boss.increase_boss_killed_count()
                    enemies.pop(enemy_choice - 1)
                else:
                    print(f"{enemy.name} contre-attaque!")
                    if ally:
                        print("\nChoisissez un ennemi que votre allié devra attaquer:")
                        for i, enemy in enumerate(enemies, 1):
                            print(f"{i}. {enemy.name}")
                        ally_enemy_choice = int(input("Entrez le numéro de l'ennemi: "))
                        if 1 <= ally_enemy_choice <= len(enemies):
                            ally_enemy = enemies[ally_enemy_choice - 1]
                            ally.attack(ally_enemy)
                            if not ally_enemy.is_alive():
                                print(f"{ally_enemy.name} a été vaincu !")
                                ally.gain_exp(ally_enemy.exp_reward)
                                enemies.pop(ally_enemy_choice - 1)
                            else:
                                print(f"{ally_enemy.name} contre-attaque!")
                                player.defense(ally_enemy.attack_value, ally_enemy)
                                if not player.is_alive():
                                    print(f"{player.name} a été vaincu!")
                                    break
                                else:
                                    print(f"{player.name} a résisté à l'attaque de {ally_enemy.name}!")
                        else:
                            print("Numéro d'ennemi invalide.")
                    else:
                        print("Tu n'as pas d'allié.")
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
    def __init__(self, name, enemies):
        self.name = name
        self.enemies = enemies

def start_game(player, ally):
    print("Bienvenue dans le jeu !")
    dungeons = []

    dungeons.append(
        Dungeon("Donjon 1", [
            Zombie.create_enemy() for _ in range(3)
            # ...
        ]))
    dungeons.append(
        Dungeon("Etage 2", [
            Zombie2_0.create_enemy() for _ in range(3)
            #...
        ]))
    dungeons.append(
        Dungeon("Etage 3", [
            Zombie_guerrier.create_enemy() for _ in range(3)
            # ...
        ]))
    if random.random() < 0.4 :
        dungeons.append(
            Dungeon("Etage 4", [
                Cadaverus_Devorator.create_boss()
                # ...
            ]))
    dungeons.append(
        Dungeon("Donjon 2", [
            Skeletons.create_enemy()
            # ...
        ]))
    dungeons.append(
        Dungeon("Etage 2", [
            Reinforced_Skeleton.create_enemy() for _ in range(3)
            # ...
        ]))
    dungeons.append(
        Dungeon("Etage 3", [
            armor_Skeletons.create_enemy() for _ in range(3)
            # ...
        ]))
    if random.random() < 0.4 :
        dungeons.append(
            Dungeon("Etage 4", [
                Kondylos_o_Sarantapus.create_boss()
                # ...
            ]))
    dungeons.append(
        Dungeon("Donjon 3", [
            Goblins.create_enemy(),
            # ...
        ]))
    dungeons.append(
        Dungeon("Etage 2", [
            big_goblins.create_enemy() for _ in range(3)
            # ...
        ]))
    if random.random() < 0.4 :
        dungeons.append(
            Dungeon("Etage 3", [
                Roi_Gobelin.create_boss()
                # ...
            ]))
    dungeons.append(
        Dungeon("Donjon 4", [
            Trolls.create_enemy() for _ in range(3)
            # ...
        ]))
    dungeons.append(
        Dungeon("Etage 2", [
            Olog_hai.create_enemy() for _ in range(3)
            # ...
        ]))
    if random.random() < 0.4 :
        dungeons.append(
            Dungeon("Etage 4", [
                Garrok_le_Féroce.create_boss()
                # ...
            ]))
    # Ajouter le donjon Balrog après avoir tué 5 boss
    if Boss.boss_killed_count >= 5:
        dungeons.append(
            Dungeon("Une autre dimension", [
                Balrog.create_mega_boss()
                # ...
            ]))
    for dungeon in dungeons:
        print(f"Tu rentres dans le {dungeon.name}!")
        combat(player, ally, dungeon.enemies)
        if not player.is_alive():
            print("Vous avez été vaincu ! Jeu terminé.")
            break
        elif not ally.is_alive():
            print("Ton allié a été vaincu ! Jeu terminé.")
            break
        else:
            print(f"Vous avez vaincu le {dungeon.name}! Passons au donjon suivant...")
            # Add logic here to move on to the next dungeon
            for enemy in dungeon.enemies:
                if isinstance(enemy, Boss) and not enemy.is_alive():
                    kill_boss()
            input("Appuyez sur Entrée pour continuer...")