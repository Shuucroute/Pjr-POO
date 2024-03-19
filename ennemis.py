from character import Character
from dice import Dice 
from rich.text import Text
from rich import print



class Zombie(Character):
    def __init__(self, name="Zombie", hp=20, attack_value=5, defense_value=5, dice=Dice("green", 6), exp_reward=55):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward)
        self.name = Text(f"[bold green]{self.name}[/bold green]")

    def compute_damages(self, roll, target):
        print(f"🧟 {self.name} [bold]Vous attaque ![/bold]")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 {self.name} [bold]prend des dégâts ![/bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    def defeat(self, player, num_zombie_vaincus):
        super().defeat()  # Appel de la méthode de la classe parente pour gérer la défaite du Zombie
        player.gain_exp(self.exp_reward * num_zombie_vaincus)  # Récompense le joueur avec l'expérience appropriée
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(dice=dice)   
    
class Zombie2_0(Zombie):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 2
        return max(0, raw_damages)  # Assure que les dégâts ne peuvent pas être négatifs
    
    def defeat(self, player, num_zombie_vaincus):
        super().defeat(player, num_zombie_vaincus)  
        player.gain_exp((self.exp_reward + 10) * num_zombie_vaincus)
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(name="Zombie Robuste" ,dice=dice)

class Zombie_guerrier(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 {self.name} [bold]Vous attaque ![/bold] (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 5
        return max(0, raw_damages)
    
    def drop_exp(self):
        return 50
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(name="Zombie Guerrier" ,dice=dice)

class Skeletons(Character):
    def __init__(self, name="Squelettes", hp=20, attack_value=5, defense_value=3, dice=Dice("White", 6), exp_reward=60):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward)
        self.name = Text(f"[dim]{self.name}[/dim]")

    def compute_damages(self, roll, target):
        print(f"💀 {self.name} [bold]Vous attaque ![/bold] (+3 dmg)")
        return super().compute_damages(roll, target) + 3
        
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 {self.name} [bold]prend des dégâts ![bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(dice=dice)

class Reinforced_Skeleton(Skeletons):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):

        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 3
        return max(0, raw_damages)
    
    def drop_exp(self):
        return 35
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(name="Squelette renforcé",dice=dice)

class armor_Skeletons(Skeletons):
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 6
        return max(0, raw_damages)
    
    def drop_exp(self):
        return 45
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(name="squelette à armure",dice=dice)

class Goblins(Character):
    def __init__ (self, name="gobelins", hp=20, attack_value=5, defense_value=5, dice=Dice("white_green", 6), exp_reward=90):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward)
        self.name = Text(f"[green]{self.name}[/green]")

    def compute_damages(self, roll, target):
        print(f"👹 {self.name} [bold]Vous attaque ![/bold]")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"👹 {self.name} [bold]prend des dégâts ![/bold]")
        return super().compute_raw_damages(damages, roll, attacker)

    @classmethod
    def create_enemy(cls, dice):
        return cls(dice=dice)

class big_goblins(Goblins):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 4
        return max(0, raw_damages)
    
    def drop_exp(self):
        return 35
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(name="Gros gobelin",dice=dice)
        

class Trolls(Character):
    def __init__ (self, name="Trolls", hp=35, attack_value=15, defense_value=10, dice=Dice("black", 6)):
        super().__init__(name, hp, attack_value, defense_value, dice)
        self.name = Text(f"[dark green]{self.name}[/dark green]")

    def compute_damages(self, roll, target):
        print(f"🧌 {self.name} [bold]Vous attaque ![/bold]")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧌 {self.name} [bold]prend des dégâts ![/bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    def drop_exp(self):
        return 45


    @classmethod
    def create_enemy(cls, dice):
        return cls(dice=dice)

class Olog_hai(Trolls):
    def compute_damages(self, roll, target):
        print("🧌 {self.name} [bold]Vous attaque ![/bold] (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def drop_exp(self):
        return 50
    
    @classmethod
    def create_enemy(cls, dice):
        return cls(name="Olog hai",dice=dice)

ENNEMIES = [Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton, armor_Skeletons, Goblins, big_goblins, Trolls, Olog_hai]