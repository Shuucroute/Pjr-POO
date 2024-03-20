from objet import 
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

        #Bouclier
        wooden_shield = WoodenShield()
        bone_shield = BoneShield()
        iron_shield = IronShield()
        cooper_shield = CooperShield()

        #Epée
        wooden_sword = WoodenSword()
        iron_sword = IronSword()
        diamond_sword = DiamondSword()
        excalibur = Excalibur()

        #Armure
        leather_armor = LeatherArmor()
        iron_armor = IronArmor()
        chainmail = Chainmail()
        endium_armor = EndimuAmor()

        #Baton Magique
        fire_stick = FireStick()
        ice_stick = IceStick()
        wind_stick = WindStick()
        ultimate_stick = UltimateStick()

        #Dague
        wooden_dagger = WoodenDagger()
        silver_dagger = SilverDagger()
        coper_dagger = CoperDagger()
        gold_dagger = GoldDagger()

        #Arc
        classic_arc = ClassicArc()
        long_arc = LongArc()
        arbalète = Arbalète()
        triplearc = TripleArc()
        
        #Cape
        mana_cape = ManaCape()
        heal_cape = HealCape()
        defense_cape = DefenseCape()
        utlimate_cape = UltimateCape()




