import sys
import character
import random 
import dice

def show_main_menu():
    print("Bienvenue dans le jeu !")
    print("/" * 30)
    print("|", "1. Nouvelle partie".ljust(25), "|")
    print("|", "2. Charger une partie".ljust(25), "|")
    print("|", "3. Quitter".ljust(25), "|")
    print("/" * 30)

def select_character():
    show_main_menu()
    while True:
        choice = input("Entrez votre choix : ")
        if choice == "1":
            name = input("Entrez le nom de votre personnage : ")
            character_class = input("Choisissez votre classe (Archer, Druid, Thief, Warrior, Mage) : ").lower()
            if character_class == "archer":
                return character.Archer(name, 100, 10, 5, character.Dice_spawn())
            elif character_class == "druid":
                return character.Druid(name, 120, 8, 6, character.Dice_spawn(), 20, random.randint(1, 5))
            elif character_class == "thief":
                return character.Thief(name, 80, 12, 4, character.Dice_spawn())
            elif character_class == "warrior":
                return character.Warrior(name, 150, 6, 8, character.Dice_spawn())
            elif character_class == "mage":
                return character.Mage(name, 80, 15, 3, character.Dice_spawn())
            else:
                print("Classe invalide.")
        elif choice == "2":
            print("Chargement d'une partie...")
            # Ajouter la logique de chargement de la partie ici
        elif choice == "3":
            print("Au revoir !")
            sys.exit()
        else:
            print("Choix invalide.")
