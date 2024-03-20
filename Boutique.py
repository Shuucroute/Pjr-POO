from objet import *

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

if __name__ == "__main__":
        
        # Création de joueurs
        James = Player("James", 100)
        Lisa = Player("Lisa", 150)

        
        # Création des objets (Bouclier - Epée - Armure - Baton Magique - Dague - Arc - Cape)
        objects = [
            WoodenShield(), BoneShield(), IronShield(), CooperShield(),
            WoodenSword(), IronSword(), DiamondSword(), Excalibur(),
            LeatherArmor(), IronArmor(), Chainmail(), EndiumArmor(),
            FireStick(), IceStick(), WindStick(), UltimateStick(),
            WoodenDagger(), SilverDagger(), CoperDagger(), GoldDagger(),
            ClassicArc(), LongArc(), Arbalète(), TripleArc(),
            ManaCape(), HealCape(), DefenseCape(), UltimateCape()
        ]

        #Achat des objets
        for item in objects:
             James.buy_item(item)
             Lisa.buy_item(item)
        




