import sys
import character 


def show_main_menu():
    print("Bienvenue dans le jeu !")
    print("1. Nouvelle partie")
    print("2. Charger une partie")
    print("3. Quitter")

def select_character():
    show_main_menu()
    while True:
        choice = input("Entrez votre choix : ")
        if choice == "1":
            name = input("Entrez le nom de votre personnage : ")
            character_class = input("Choisissez votre classe (Archer, Druid, Thief, Warrior, Mage) : ")
            if character_class.lower() == "archer":
                return character.Archer(name, 100, 10, 5, character.Dice_spawn())
            elif character_class.lower() == "druid":
                return character.Druid(name, 120, 8, 6, character.Dice_spawn(), 20, random.randint(1, 5))
            elif character_class.lower() == "thief":
                return character.Thief(name, 80, 12, 4, character.Dice_spawn())
            elif character_class.lower() == "warrior":
                return character.Warrior(name, 150, 6, 8, character.Dice_spawn())
            elif character_class.lower() == "mage":
                return character.Mage(name, 80, 15, 3, character.Dice_spawn())
            else:
                print("Classe invalide.")
                continue
        elif choice == "2":
            print("Chargement d'une partie...")
            # Ajouter la logique de chargement de la partie ici
        elif choice == "3":
            print("Au revoir !")
            sys.exit()
        else:
            print("Choix invalide. Veuillez réessayer.")