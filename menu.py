from character import Warrior, Mage, Thief, Archer
from dice import Dice

dice = Dice()

def display_menu():
    print("Choisis un personnage :")
    print("1. Warrior")
    print("2. Mage")
    print("3. Thief")
    print("4. Archer")

def get_choice():
    while True:
        try:
            choice = int(input("Entre ton choix : "))
            if 1 <= choice <= 4:
                return choice
            else:
                print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")
        except ValueError:
            print("Choix invalide. Veuillez entrer un nombre entre 1 et 4.")

def create_character(choice):
    if choice == 1:
        return Warrior("Warrior", 100, 10, 5, dice)
    elif choice == 2:
        return Mage("Mage", 80, 15, 3, dice)
    elif choice == 3:
        return Thief("Thief", 90, 12, 4, dice)
    elif choice == 4:
        return Archer("Archer", 70, 13, 2, dice)

def main():
    display_menu()
    choice = get_choice()
    player = create_character(choice)
    print(f"Tu as choisi {player.name}.")
    print(player)

if __name__ == "__main__":
    main()