from character import Character
from dice import Dice 
from rich.text import Text
from rich import print

class Zombie(Character):
    def __init__(self, name="Zombie", hp=20, attack_value=15, defense_value=5, dice=Dice(6), exp_reward=5, coins_reward=5):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[green1]{self.name}[/green1]")
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
        """
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
    def __init__(self):
        super().__init__(name="Zombie Robuste", hp=30, attack_value=18, defense_value=8, dice=Dice(6), exp_reward=10, coins_reward=7)
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         /   \\
        """
    
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 2
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 2
        return max(0, raw_damages)  # Assure que les dégâts ne peuvent pas être négatifs
    
    def defeat(self, player : Character, num_zombie2_0_vaincus):
        player.gain_exp(self.exp_reward * num_zombie2_0_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls()

class Zombie_guerrier(Zombie):
    def __init__(self):
        super().__init__(name="Zombie Guerrier", hp=40, attack_value=20, defense_value=10, dice=Dice(6), exp_reward=15, coins_reward=10)
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         / | \\
        """
    
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
        return cls()

class Skeletons(Character):
    def __init__(self, name="Squelettes", hp=20, attack_value=5, defense_value=3, dice=Dice(6), exp_reward=6, coins_reward=5):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[dim]{self.name}[/dim]")
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         /   \\
        """

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
    def __init__(self):
        super().__init__(name="Squelette renforcé", hp=30, attack_value=10, defense_value=6, dice=Dice(6), exp_reward=12, coins_reward=7)
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         / | \\
        """
    
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 3
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_Reinforced_Skeletons_vaincus):
        player.gain_exp(self.exp_reward * num_Reinforced_Skeletons_vaincus) 
    
    @classmethod
    def create_enemy(cls):
        return cls()

class armor_Skeletons(Skeletons):
    def __init__(self):
        super().__init__(name="Squelette à armure", hp=40, attack_value=12, defense_value=10, dice=Dice(6), exp_reward=15, coins_reward=10)
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         / | \\
         [---]
        """
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 6
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_Armor_Skeletons_vaincus):
        player.gain_exp(self.exp_reward * num_Armor_Skeletons_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls()

class Goblins(Character):
    def __init__ (self, name="gobelins", hp=20, attack_value=5, defense_value=5, dice=Dice(6), exp_reward=7, coins_reward=7):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[green]{self.name}[/green]")
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         /   \\
        """

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
    def __init__(self):
        super().__init__(name="Gros gobelin", hp=40, attack_value=10, defense_value=8, dice=Dice(6), exp_reward=18, coins_reward=12)
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         / | \\
        """
    
    def compute_damages(self, roll, target):
        return super().compute_damages(roll, target) + 5
    
    def compute_raw_damages(self, damages, roll, attacker):
        raw_damages = super().compute_raw_damages(damages, roll, attacker) - 4
        return max(0, raw_damages)
    
    def defeat(self, player : Character, num_big_gobelins_vaincus):
        player.gain_exp(self.exp_reward * num_big_gobelins_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls()

class Trolls(Character):
    def __init__ (self, name="Trolls", hp=35, attack_value=15, defense_value=10, dice=Dice(6), exp_reward= 25, coins_reward=15):
        super().__init__(name, hp, attack_value, defense_value, dice, exp_reward, coins_reward)
        self.name = Text(f"[dark green]{self.name}[/dark green]")
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         / | \\
        """

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
    def __init__(self):
        super().__init__(name="Olog hai", hp=50, attack_value=20, defense_value=15, dice=Dice(6), exp_reward=30, coins_reward=20)
        self.ascii_art = """
          .-.
         (o o)
         | O |
          \_/
         / | \\
         [---]
        """
    
    def compute_damages(self, roll, target):
        print("🧌 {self.name} [bold]Vous attaque ![/bold] (+5 dmg)")
        return super().compute_damages(roll, target) + 5
    
    def defeat(self, player : Character, num_Olog_hai_vaincus):
        player.gain_exp(self.exp_reward * num_Olog_hai_vaincus)
    
    @classmethod
    def create_enemy(cls):
        return cls()

ENNEMIES = [Zombie, Zombie2_0, Zombie_guerrier, Skeletons, Reinforced_Skeleton, armor_Skeletons, Goblins, big_goblins, Trolls, Olog_hai]