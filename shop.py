from objet import *
from objet import WoodenShield, BoneShield, IronShield, CooperShield
from objet import WoodenSword, IronSword, DiamondSword, Excalibur
from objet import LeatherArmor, IronArmor, Chainmail, EndiumArmor
from objet import FireStick, IceStick, WindStick, UltimateStick
from objet import WoodenDagger, SilverDagger, CoperDagger, GoldDagger
from objet import ClassicArc, LongArc, Arbalète, TripleArc
from objet import ManaCape, HealCape, DefenseCape, UltimateCape

def select_shield():
    shields = [WoodenShield(), BoneShield(), IronShield(), CooperShield()]
    print("Voici les boucliers disponibles :")
    for i, shield in enumerate(shields, start=1):
        print(f"{i}. {shield.name} - Prix : {shield.price} coins")

def select_sword():
    swords = [WoodenSword(), IronSword(), DiamondSword(), Excalibur()]
    print("Voici les épées disponibles :")
    for i, sword in enumerate(swords, start=1):
        print(f"{i}. {sword.name} - Prix : {sword.price} coins")

def select_armor():
    armors = [LeatherArmor(), IronArmor(), Chainmail(), EndiumArmor()]
    print("Voici les armures disponibles :")
    for i, armor in enumerate(armors, start=1):
        print(f"{i}. {armor.name} - Prix : {armor.price} coins")

def select_stick():
    sticks = [FireStick(), IceStick(), WindStick(), UltimateStick()]
    print("Voici les bâtons magiques disponibles :")
    for i, stick in enumerate(sticks, start=1):
        print(f"{i}. {stick.name} - Prix : {stick.price} coins")

def select_dagger():
    daggers = [WoodenDagger(), SilverDagger(), CoperDagger(), GoldDagger()]
    print("Voici les dagues disponibles :")
    for i, dagger in enumerate(daggers, start=1):
        print(f"{i}. {dagger.name} - Prix : {dagger.price} coins")

def select_arc():
    arcs = [ClassicArc(), LongArc(), Arbalète(), TripleArc()]
    print("Voici les arcs disponibles :")
    for i, arc in enumerate(arcs, start=1):
        print(f"{i}. {arc.name} - Prix : {arc.price} coins")

def select_cape():
    capes = [ManaCape(), HealCape(), DefenseCape(), UltimateCape()]
    print("Voici les capes disponibles :")
    for i, cape in enumerate(capes, start=1):
        print(f"{i}. {cape.name} - Prix : {cape.price} coins")

class Shop:
    def __init__(self):
        self.items =  [
            WoodenShield(), BoneShield(), IronShield(), CooperShield(),
            WoodenSword(), IronSword(), DiamondSword(), Excalibur(),
            LeatherArmor(), IronArmor(), Chainmail(), EndiumArmor(),
            FireStick(), IceStick(), WindStick(), UltimateStick(),
            WoodenDagger(), SilverDagger(), CoperDagger(), GoldDagger(),
            ClassicArc(), LongArc(), Arbalète(), TripleArc(),
            ManaCape(), HealCape(), DefenseCape(), UltimateCape()
        ]

    def display_shop(self, player):
        print("Bienvenue dans le magasin !")
        self.select_category(player)

    def select_category(self, player):
        print("\nChoisissez une catégorie :")
        print("1. Boucliers")
        print("2. Epées")
        print("3. Armures")
        print("4. Bâtons magiques")
        print("5. Dagues")
        print("6. Arcs")
        print("7. Capes")
        category_choice = int(input("Entrez le numéro de la catégorie : "))
        if category_choice == 1:
            select_shield()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice)
        elif category_choice == 2:
            select_sword()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice + 4)
        elif category_choice == 3:
            select_armor()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice + 8)
        elif category_choice == 4:
            select_stick()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice + 12)
        elif category_choice == 5:
            select_dagger()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice + 16)
        elif category_choice == 6:
            select_arc()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice + 20)
        elif category_choice == 7:
            select_cape()
            item_choice = int(input("Entrez le numéro de l'article que vous voulez acheter : "))
            self.buy_item(player, item_choice + 24)
        else:
            print("Catégorie invalide.")

    def buy_item(self, player, item_choice):
        item = self.items[item_choice]
        if player.coins >= item.price:
            player.coins -= item.price
            print(f"Vous avez acheté {item.name} pour {item.price} coins. ")
        else:
            print("Vous n'avez pas assez de coins pour acheter cet objet.")
