from character import Character
from dice import Dice 
from rich.text import Text
from rich import print


class Zombie(Character):
    def __init__(self, name="Zombie", hp=20, attack_value=15, defense_value=5, dice=Dice(6), exp_reward=50, coins_reward=5):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[green1]{self.name}[/green1]")
        print(self.exp_reward)
    
    def compute_damages(self, roll, target):
        print(f"🧟 {self.name} [bold]Vous attaque ![/bold]")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧟 {self.name} [bold]prend des dégâts ![/bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    def defeat(self, player : Character, num_zombie_vaincus):
        player.gain_exp(self.exp_reward * num_zombie_vaincus)  # Récompense le joueur avec l'expérience appropriée
    
    @classmethod
    def create_enemy(cls):
        return cls(dice=Dice(6))   
    
class Zombie2_0(Zombie):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 2
        return max(0, raw_damages)  # Assure que les dégâts ne peuvent pas être négatifs
    
    def defeat(self, player : Character, num_zombie2_0_vaincus):
        player.gain_exp(self.exp_reward * num_zombie2_0_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls(name="Zombie Robuste" ,dice=Dice(6), exp_reward=60, coins_reward=7)

class Zombie_guerrier(Zombie):
    def compute_damages(self, roll, target):
        print(f"🧟 {self.name} [bold]Vous attaque ![/bold] (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 5
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_zombiesGuerrier_vaincus):
        player.gain_exp(self.exp_reward * num_zombiesGuerrier_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls(name="Zombie Guerrier" ,dice=Dice(6), exp_reward=100, coins_reward= 10)

class Skeletons(Character):
    def __init__(self, name="Squelettes", hp=20, attack_value=5, defense_value=3, dice=Dice(6), exp_reward=65, coins_reward=5):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[dim]{self.name}[/dim]")

    def compute_damages(self, roll, target):
        print(f"💀 {self.name} [bold]Vous attaque ![/bold] (+3 dmg)")
        return super().compute_damages(roll, target) + 3
        
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"💀 {self.name} [bold]prend des dégâts ![bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    def defeat(self, player : Character, num_skeletons_vaincus):
        player.gain_exp(self.exp_reward * num_skeletons_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls(dice=Dice(6))

class Reinforced_Skeleton(Skeletons):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):

        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 3
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_Reinforced_Skeletons_vaincus):
        player.gain_exp(self.exp_reward * num_Reinforced_Skeletons_vaincus) 
    
    @classmethod
    def create_enemy(cls):
        return cls(name="Squelette renforcé",dice=Dice(6), exp_reward=70, coins_reward=7)

class armor_Skeletons(Skeletons):
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 6
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_Armor_Skeletons_vaincus):
        player.gain_exp(self.exp_reward * num_Armor_Skeletons_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls(name="squelette à armure",dice=Dice(6), exp_reward=75, coins_reward=10)

class Goblins(Character):
    def __init__ (self, name="gobelins", hp=20, attack_value=5, defense_value=5, dice=Dice(6), exp_reward=90, coins_reward=7):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[green]{self.name}[/green]")

    def compute_damages(self, roll, target):
        print(f"👹 {self.name} [bold]Vous attaque ![/bold]")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"👹 {self.name} [bold]prend des dégâts ![/bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    def defeat(self, player : Character, num_Goblins_vaincus):
        player.gain_exp(self.exp_reward * num_Goblins_vaincus)

    @classmethod
    def create_enemy(cls):
        return cls(dice=Dice(6))

class big_goblins(Goblins):
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 4
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_big_gobelins_vaincus):
        player.gain_exp(self.exp_reward * num_big_gobelins_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls(name="Gros gobelin",dice=Dice(6), exp_reward=95, coins_reward=12)
        

class Trolls(Character):
    def __init__ (self, name="Trolls", hp=35, attack_value=15, defense_value=10, dice=Dice(6), exp_reward= 105, coins_reward=15):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[dark green]{self.name}[/dark green]")

    def compute_damages(self, roll, target):
        print(f"🧌 {self.name} [bold]Vous attaque ![/bold]")
        return super().compute_damages(roll, target)

    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🧌 {self.name} [bold]prend des dégâts ![/bold]")
        return super().compute_raw_damages(damages, roll, attacker)
    
    def defeat(self, player : Character, num_Trolls_vaincus):
        player.gain_exp(self.exp_reward * num_Trolls_vaincus)

    @classmethod
    def create_enemy(cls):
        return cls(dice=Dice(6))

class Olog_hai(Trolls):
    def compute_damages(self, roll, target):
        print("🧌 {self.name} [bold]Vous attaque ![/bold] (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def defeat(self, player : Character, num_Olog_hai_vaincus):
        player.gain_exp(self.exp_reward * num_Olog_hai_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls(name="Olog hai",dice=Dice(6), exp_reward=110, coins_reward=20)

ENNEMIES = [Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton, armor_Skeletons, Goblins, big_goblins, Trolls, Olog_hai]