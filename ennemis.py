from character import Character
from dice import Dice 


class Zombie(Character):
    def __init__(self, name="Zombie", hp=20, attack_value=5, defense_value=5, dice=Dice("green", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print(f"🧟 Zombie t'attaque !")
        return super().compute_damages(roll, target)
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 Zombie est faible !")
        return super().compute_raw_damages(damages, roll, attacker)

class Zombie2_0(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 Zombie robuste t'attaque ! (+2 dmg)")
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 Zobmie robuste a faim ! (-2 dmg)" )
        return super().compute_raw_damages(damages, roll, attacker) - 2
    
class Zombie_guerrier(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 Zombie guerrier t'attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 Zombie guerrier a faim ! (-5 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 5


class Skeletons(Character):
    def __init__(self, name="Squelettes", hp=20, attack_value=5, defense_value=3, dice=Dice("White", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print(f"💀 Squelette vous attaque ! (+3 dmg)")
        return super().compute_damages(roll, target) + 3
        
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 Squelette prends des dégâts")
        return super().compute_raw_damages(damages, roll, attacker)

class Reinforced_Skeleton(Skeletons):
    def compute_damages(self, roll, target):
        print(f"💀 Squelette renforcé vous attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 Squelette renforcé prends des dégâts ! (-3 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 3

class armor_Skeletons(Skeletons):
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 Squelettes à armure prends des dégâts ! (-6 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 6


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
    def __init__ (self, name="Trolls", hp=35, attack_value=15, defense_value=13, dice=Dice("black", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

class Troll_trucs(Trolls):
    print("🧌")


class Renegas(Character):
    pass

class Boss(Character):
    pass


class Balrog(Character):
    pass