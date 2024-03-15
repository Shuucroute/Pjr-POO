from character import Character
from dice import Dice



class Boss(Character):
    boss_killed_count = 0
    def __init__ (self, name="Boss", hp=50, attack_value=20, defense_value=20, dice=Dice("Red", 10)):
        return super().__init__(name, hp, attack_value, defense_value, dice)
    
    @classmethod
    def increase_boss_killed_count(cls):
        cls.boss_killed_count += 1
        if cls.boss_killed_count % 5 == 0:
            return Balrog.summon_balrog()
        else:
            return None

class Cadaverus_Devorator(Boss): #Boss Zombie
    def compute_damages(self, roll, target):
        print("Cadaverus Devorator vous attaque ! (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Cadaverus Devorator prends des dégâts ! (-5 dmg)")
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 5
        return max(0, raw_damages)
    
    @classmethod
    def create_boss(cls, dice):
        return cls(name="Cadaverus Devorator",dice=dice)

class Kondylos_o_Sarantapus(Boss): #boss squelette
    def compute_damages(self, roll, target):
        print("Le Kondylos o Sarantapus vous attaque ! (+6 dmg)")
        return super().compute_damages(roll, target) + 6
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le ondylos o Sarantapus prends des dégâts ! (-4 dmg)")
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 4
        return max(0, raw_damages)
    
    @classmethod
    def create_boss(cls, dice):
        return cls(name="Kondylos o Sarantapus",dice=dice)
    
class Roi_Gobelin(Boss): #boss gobelin
    def compute_damages(self, roll, target):
        print("Le Roi Gobelin vous attaque ! (+7 dmg)")
        return super().compute_damages(roll, target) + 7
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le Roi Gobelin prends des dégâts ! (-7 dmg)")
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 7
        return max(0, raw_damages)
    
    @classmethod
    def create_boss(cls, dice):
        return cls(name="Roi Gobelin",dice=dice)
    
class Garrok_le_Féroce(Boss): #troll boss
    def compute_damages(self, roll, target):
        print("Le Garrok le Féroce vous attaque ! (+10 dmg)")
        return super().compute_damages(roll, target) +10 
    
    def compute_raw_damages(self, damages, roll, attacker):
        print("Le Garrok le Féroce prends des dégâts ! (-10 dmg)")
        raw_damages = super().compute_raw_damages(damages, roll, attacker) -10 
        return max(0, raw_damages)
    
    @classmethod
    def create_boss(cls, dice):
        return cls(name="Garrok le Féroce",dice=dice)

class Balrog(Character):
    def __init__ (self, name="Balrog", hp=100, attack_value=50, defense_value=50, dice=Dice("Black_red", 15)):
        return super().__init__(name, hp, attack_value, defense_value, dice)
    
    @classmethod
    def summon_balrog(cls):
        print("Cinqs Boss sont morts ! Le Balrog apparait !")
        return cls()
    
    @classmethod
    def create_mega_boss(cls, dice):
        return cls(dice=dice)