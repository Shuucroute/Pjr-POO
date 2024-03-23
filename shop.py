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


    def display_shop(self):
        print("Bienvenue dans le magasin ! Voici les articles disponibles :")
        print("1. Boucliers :")
        for item in self.items[:4]:  # Afficher les boucliers
            print(f" {item.name} - Prix : {item.price} coins")
        print("\n2. Epées :")
        for item in self.items[4:8]:  # Afficher les épées
            print(f" {item.name} - Prix : {item.price} coins")
        print("\n3. Armures :")
        for item in self.items[8:12]:  # Afficher les armures
            print(f" {item.name} - Prix : {item.price} coins")
        print("\n4. Bâtons magiques :")
        for item in self.items[12:16]:  # Afficher les bâtons magiques
            print(f" {item.name} - Prix : {item.price} coins")
        print("\n5. Dagues :")
        for item in self.items[16:20]:  # Afficher les dagues
            print(f" {item.name} - Prix : {item.price} coins")
        print("\n6. Arcs :")
        for item in self.items[20:24]:  # Afficher les arcs
            print(f" {item.name} - Prix : {item.price} coins")
        print("\n7. Capes :")
        for item in self.items[24:]:  # Afficher les capes
            print(f" {item.name} - Prix : {item.price} coins")

    
    def buy_item(self, player, choice):
        item = self.items[choice]
        if player.coins >= item.price:
            player.coins <= item.price
            print(f"Vous avez acheté {item.name} pour {item.price} coins. ")

        
        else:
            print("Vous n'avez pas assez de coins pour acheter cet objet.")
     





        