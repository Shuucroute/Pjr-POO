import sys
import character
import random
from dice import Dice

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
        print("Vous avez choisi l'option:", choice)
        if choice == "1":
            name = input("Entrez le nom de votre personnage : ")
            character_class = choose_character_class()
            recruit_ally = input("Voulez-vous recruter un allié? (oui/non) : ").lower()
            if recruit_ally == "o":
                ally = choose_ally(character_class)
            else:
                ally = None
                print("Vous avez choisi de ne pas recruter d'allié.")
            player = create_main_character(name, character_class)
            print("Personnage principal créé avec succès !")
            break
        elif choice == "2":
            print("Chargement d'une partie...")
        elif choice == "3":
            print("Au revoir !")
            sys.exit()
        else:
            print("Choix invalide.")
    print("Fin de la sélection du personnage.")
    return player, ally

def choose_character_class():
    print("Choisissez votre classe :")
    print("1. Archer")
    print("2. Druid")
    print("3. Thief")
    print("4. Warrior")
    print("5. Mage")
    while True:
        choice = input("Entrez le numéro correspondant à votre classe : ")
        if choice == "1":
            return "archer"
        elif choice == "2":
            return "druid"
        elif choice == "3":
            return "thief"
        elif choice == "4":
            return "warrior"
        elif choice == "5":
            return "mage"
        else:
            print("Classe invalide.")

def create_main_character(name, character_class):
    if character_class == "archer":
        return character.Archer(name, 100, 10, 5,Dice(color="green",faces=6), exp_reward=1)
    elif character_class == "druid":
        return character.Druid(name, 120, 8, 6, 20, random.randint(1, 5), exp_reward=1)
    elif character_class == "thief":
        return character.Thief(name, 80, 12, 4,Dice(color="green",faces=6), exp_reward=1)
    elif character_class == "warrior":
        return character.Warrior(name, 150, 6, 8,Dice(color="green",faces=6), exp_reward=1)
    elif character_class == "mage":
        return character.Mage(name, 80, 15, 3,Dice(color="green",faces=6), exp_reward=1)

def choose_ally(character_class):
    print("Choisissez un allié avec des caractéristiques similaires à votre classe principale :")
    print("1. Archer")
    print("2. Druid")
    print("3. Thief")
    print("4. Warrior")
    print("5. Mage")
    print("0. Ne pas recruter d'allié")

    while True:
        choice = input("Entrez le numéro correspondant à la classe de votre allié : ")
        if choice == "0":
            print("Vous avez choisi de ne pas recruter d'allié.")
            return None
        elif choice == "1":
            print("Vous avez choisi d'avoir un allié Archer.")
            return character.Archer("Ally", 100, 10, 5)
        elif choice == "2":
            print("Vous avez choisi d'avoir un allié Druid.")
            # Ajoutez un argument supplémentaire 'healing_value'
            return character.Druid("Ally", 120, 8, 6, 20, random.randint(1, 5), random.randint(1, 5))
        elif choice == "3":
            print("Vous avez choisi d'avoir un allié Thief.")
            return character.Thief("Ally", 80, 12, 4)
        elif choice == "4":
            print("Vous avez choisi d'avoir un allié Warrior.")
            return character.Warrior("Ally", 150, 6, 8)
        elif choice == "5":
            print("Vous avez choisi d'avoir un allié Mage.")
            return character.Mage("Ally", 80, 15, 3)
        else:
            print("Choix invalide.")

if __name__ == "__main__":
    print("Début du script...")
    player, ally = select_character()
    print("Fin du script...")
