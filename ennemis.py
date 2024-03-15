from character import Character
from dice import Dice 

class Zombie(Character):
    def init(self, name="Zombie", hp=20, attack_value=5, defense_value=5, dice=Dice("green", 6)):
        super().init(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print(f"🧟 Zombie t'attaque !")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 Zombie est faible !")
        return super().compute_raw_damages(damages, roll, attacker)

    @staticmethod
    def create_enemy(dice):
        return Zombie("Zombie", hp=20, attack_value=5, defense_value=5, dice=dice)
    
class Zombie2_0(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 Zombie robuste t'attaque ! (+2 dmg)")
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 Zobmie robuste a faim ! (-2 dmg)" )
        return super().compute_raw_damages(damages, roll, attacker) - 2
    
    @staticmethod
    def create_enemy(dice):
        return Zombie2_0("Zombie 2.0", hp=30, attack_value=7, defense_value=7, dice=dice)

class Zombie_guerrier(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 Zombie guerrier t'attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 Zombie guerrier a faim ! (-5 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 5
    
    @staticmethod
    def create_enemy(dice):
        return Zombie_guerrier("Zombie guerrier", hp=40, attack_value=10, defense_value=10, dice=dice)

class Skeletons(Character):
    def __init__(self, name="Squelettes", hp=20, attack_value=5, defense_value=3, dice=Dice("White", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print(f"💀 Squelette vous attaque ! (+3 dmg)")
        return super().compute_damages(roll, target) + 3
        
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 Squelette prends des dégâts")
        return super().compute_raw_damages(damages, roll, attacker)
    
    @staticmethod
    def create_enemy(dice):
        return Skeletons("Squelettes", hp=20, attack_value=5, defense_value=3, dice=dice)

class Reinforced_Skeleton(Skeletons):
    def compute_damages(self, roll, target):
        print(f"💀 Squelette renforcé vous attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 Squelette renforcé prends des dégâts ! (-3 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 3
    
    @staticmethod
    def create_enemy(dice):
        return Reinforced_Skeleton("Squelette renforcé", hp=30, attack_value=7, defense_value=7, dice=dice)

class armor_Skeletons(Skeletons):
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 Squelettes à armure prends des dégâts ! (-6 dmg)")
        return super().compute_raw_damages(damages, roll)


class Goblins(Character):
    def __init__ (self, name="gobelins", hp=20, attack_value=5, defense_value=5, dice=Dice("white_green", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

class big_goblins(Goblins):
    def compute_damages(self, roll, target):
        print(f"👹 Gros gobelin vous frappe ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"👹 Gros gobelin prends des dégâts ! (-4 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 4
        

class Trolls(Character):
    def __init__ (self, name="Trolls", hp=35, attack_value=15, defense_value=10, dice=Dice("black", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

class Olog_hai(Trolls):
    def compute_damages(self, roll, target):
        print("🧌 Olog_hai vous attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5


class Renegas(Character):
    pass


class Boss(Character):
    boss_killed_count = 0
    def __init__ (self, name="Boss", hp=50, attack_value=20, defense_value=20, dice=Dice("Red", 10)):
        return super().__init__(name, hp, attack_value, defense_value, dice)

class Cadaverus_Devorator(Boss): #Boss Zombie
    def compute_damages(self, roll, target):
        print("Le Cadaverus Devorator vous attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le Cadaverus Devorator prends des dégâts ! (-5 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 5

class Kondylos_o_Sarantapus(Boss): #boss squelette
    def compute_damages(self, roll, target):
        print("Le Kondylos_o_Sarantapus vous attaque ! (+6 dmg)")
        return super().compute_damages(roll, target) + 6
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le ondylos_o_Sarantapus prends des dégâts ! (-4 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 4
    
class Roi_Gobelin(Boss): #boss gobelin
    def compute_damages(self, roll, target):
        print("Le Roi Gobelin vous attaque ! (+7 dmg)")
        return super().compute_damages(roll, target) + 7
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le Roi Gobelin prends des dégâts ! (-7 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) -7 
    
class Garrok_le_Féroce(Boss): #troll boss
    def compute_damages(self, roll, target):
        print("Le Garrok le Féroce vous attaque ! (+10 dmg)")
        return super().compute_damages(roll, target) +10 
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le Garrok le Féroce prends des dégâts ! (-10 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) -10 

    @classmethod
    def increase_boss_killed_count(cls):
        cls.boss_killed_count += 1
        if cls.boss_killed_count % 5 == 0:
            return Balrog.summon_balrog()
        else:
            return None

class Balrog(Character):
    def __init__ (self, name="Balrog", hp=100, attack_value=50, defense_value=50, dice=Dice("Black_red", 15)):
        return super().__init__(name, hp, attack_value, defense_value, dice)
    
    @classmethod
    def summon_balrog(cls):
        print("Cinqs Boss sont morts ! Le Balrog apparait !")
        return cls()
    
class TESTE(Character):
    def __init__(self, name="TESTE", hp=10000, attack_value=10000, defense_value=10000, dice=Dice("blue", 20)) -> None:
        super().__init__(name, hp, attack_value, defense_value, dice)


ENNEMIES = [Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton, armor_Skeletons, Goblins]

#char1 = TESTE()
#char2 = Roi_Gobelin()
#char3 = Garrok_le_Féroce()
#char4 = Kondylos_o_Sarantapus()
#char5 = Cadaverus_Devorator()
#char6 = Roi_Gobelin()

#while char1.is_alive() and char2.is_alive() and char3.is_alive() and char4.is_alive() and char5.is_alive() and char6.is_alive():
 #   char1.attack(char2)
  #  char1.attack(char3)
  #  char1.attack(char4)
  #  char1.attack(char5)
  #  char1.attack(char6)



#okokok