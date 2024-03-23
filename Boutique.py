from objet import * 
from shop import *


class Player:
    def __init__(self, name, coins):
        self.name = name
        self.coins = coins

    def buy_item(self, item, price):
        if self.coins >= price:
            self.coins -=price
            print(f"{self.name} a acheté {item.name} pour {price} coins.")
        else:
            print(f"{self.name} n'a pas assez de coins pour acheter {item.name}.")


    def display_shop():
        print("Bienvenue dans le magasin ! Voici nos articles :")
        print("1. Boucliers :")
        print(" 1.1 - Bouclier en bois : 10 coins")
        print(" 1.2 - Bouclier en os : 20 coins")
        print(" 1.3 - Bouclier en fer : 30 coins")
        print(" 1.4 - Bouclier en cuivre : 40 coins")

        print("2. Epées :")
        print(" 2.1  - Epéé en bois : 10 coins")
        print(" 2.2  - Epée en fer : 20 coins")
        print(" 2.3 - Epée en diamant : 30 coins")
        print(" 2.4 - Excalibur : 40 coins ")

        print("3. Armure :")
        print(" 3.1  - Armure en cuir : 10 coins")
        print(" 3.2  - Armure en fer : 20 coins")
        print(" 3.3 - Cote de maille : 30 coins")
        print(" 3.4 - Armure Endium : 40 coins")

        print("4. Baton magique :")
        print(" 4.1  - Baton de feu : 10 coins")
        print(" 4.2  - Baton de glace : 20 coins")
        print(" 4.3  - Baton de vent : 30 coins")
        print(" 4.4  - Baton ultime : 40 coins")

        print("5. Dague :")
        print(" 5.1  - Dage en bois : 10 coins")
        print(" 5.2  - Dague en argent : 20 coins")
        print(" 5.3 - Dague en cuivre : 30 coins")
        print(" 5.4  - Dague en or : 40 coins")

        print("6. Arc :")
        print(" 6.1  - Arc classique : 10 coins")
        print(" 6.2  - Arc long : 20 coins")
        print(" 6.3  - Arbalète: 30 coins")
        print(" 6.4  - Arc triple: 40 coins")

        print("7. Cape :")      
        print(" 7.1  - Cape de Mana : 10 coins")
        print(" 7.2  - Cape de heal : 20 coins")
        print(" 7.3  - Cape de défense: 30 coins")
        print(" 7.4  - Cap Ultime: 40 coins")


    def select_item_to_buy():
        while True:
            choice = input("Entrez le numéro de l'article que vous souhaitez acheter :")
            if choice == "1":
                print(" Vous avez choisi la catégorie 'Boucliers' .")
                select_shield()
            elif choice == "2":
                print(" Vous avez choisi la catégorie 'Epées' .")
                select_sword()
            elif choice =="3":
                print("Vous avez choisi la catégorie 'Armures' .")
                select_armor()
            elif choice == "4":
                print(" Vous avez choisi la catégorie 'Batons magiques' .")
                select_stick()
            elif choice == "5":
                print(" Vous avez choisi la catégorie 'Dague' .")
                select_dagger()
            elif choice == "6":
                print(" Vous avez choisi la catégorie 'Arc' .")
                select_arc()
            elif choice == "7":
                print("Vous avez choisi la catégorie 'Capes' .")
                select_cape()

        




