from character import Character
from dice import Dice 


class Zombie(Character):
    def __init__(self, name="Zombie", hp=20, attack_value=5, defense_value=5, dice=Dice("green", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)

    def compute_damages(self, roll, target):
        print("🧟 Zombie t'attaque !")
        return super().compute_damages(roll, target)
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("🧟 Zombie est faible !")
        return super().compute_raw_damages(damages, roll, attacker)

class Zombie2_0(Zombie):
    def compute_damages(self, roll, target):
        print("🧟 Zombie robuste t'attaque ! (+2 dmg)")
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("🧟 Zobmie robuste a faim ! (-2 dmg)" )
        return super().compute_raw_damages(damages, roll, attacker) - 2
    
class Zombie_terminale(Zombie):
    def compute_damages(self, roll, target):
        print("🧟 Zombie finale t'attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("🧟 Zombie finale a faim ! (-5 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 5


class Skeletons(Character):
    def __init__():
        pass


class Gobelins(Character):
    pass


class Renegas(Character):
    pass


class Trolls(Character):
    pass


class Boss(Character):
    pass


class Balrog(Character):
    pass