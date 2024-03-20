from dice import Dice
import random
from rich import print

class Character:
    def __init__(self, name, hp_max, attack_value, defense_value, dice, exp_reward) -> None:
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.attack_value = attack_value
        self.defense_value = defense_value
        self.dice = dice
        self.exp = 0  # Points d'expérience
        self.level = 1  # Niveau
        self.exp_reward = exp_reward

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} a gagné {amount} points d'expérience.")
        self.check_level_up()  # Vérifie si le personnage monte de niveau

    def check_level_up(self):
        exp_threshold = 50 * self.level  # Seuil d'expérience pour passer au niveau suivant
        if self.exp >= exp_threshold:
            self.level += 1
            print(f"{self.name} a atteint le niveau {self.level} !")
            self.exp -= exp_threshold  # Retire l'excès d'EXP pour le prochain niveau

            # Exemple : Augmente les statistiques lors du passage de niveau
            self.hp_max += 10
            self.hp = self.hp_max
            self.attack_value += 2
            self.defense_value += 1
            self.update_exp_reward()  # Met à jour la récompense en expérience pour le prochain niveau

    def update_exp_reward(self):
        self.exp_reward += 1  # Exemple de mise à jour de la récompense en expérience pour le prochain niveau

    def show_expbar(self):
        filled_exp = min(self.exp, 50 * self.level)
        empty_exp = 50 * self.level - filled_exp
        print(f"[{'🟢' * filled_exp}{'⚫' * empty_exp}] {self.exp}/{50 * self.level} EXP")


    def __str__(self) -> str:
        return f"""I'm {self.name}. Those are my caracs :
    - {self.hp}/{self.hp_max} hp
    - att: {self.attack_value}
    - def: {self.defense_value}"""

    def is_alive(self):
        return self.hp > 0

    def decrease_hp(self, amount):
        self.hp = self.hp - amount
        if self.hp < 0:
            self.hp = 0
        self.show_healthbar()

    def increase_hp(self, amount):
        self.hp += amount

    def show_healthbar(self):
        print(
            f"[{'♥' * self.hp}{'♡' * (self.hp_max - self.hp)}] {self.hp}/{self.hp_max}hp"
        )

    def compute_damages(self, roll, target):
        return self.attack_value + roll

    def attack(self, target):
        if self.is_alive():
            roll = self.dice.roll()
            damages = self.compute_damages(roll, target)
            print(
                f"{self.name} [red]attack[/red] with {damages} (att: {self.attack_value} + roll: {roll})"
            )
            target.defense(damages, self)

    def compute_raw_damages(self, damages, roll, attacker):
        return max(0, damages - self.defense_value - roll)

    def defense(self, damages, attacker):
        roll = self.dice.roll()
        raw_damages = self.compute_raw_damages(damages, roll, attacker)
        print(
            f"{self.name} [blue]defend[/blue] againt {damages} and took {raw_damages} damages ({damages} - def: {self.defense_value} - roll: {roll})"
        )
        self.decrease_hp(raw_damages)



class Warrior(Character):
    def compute_damages(self, roll, target):
        print("🪓 Axe in your face ! (+3 dmg)")
        return super().compute_damages(roll, target) + 3


class Mage(Character):
    def compute_raw_damages(self, damages, roll, attacker):
        print(f"🔮 Magic armor ! (-3 dmg)")
        return super().compute_raw_damages(damages, roll, attacker) - 3
    
    def show_manabar(self):
        print(
            f"[{'🔵' * self.mana}{'⚪' * (self.mana_max - self.mana)}] {self.mana}/{self.mana_max}mana") 


class Thief(Character):
    def compute_damages(self, roll, target):
        print(f"🔪 Sneacky attack ! (+{target.defense_value} dmg)")
        return super().compute_damages(roll, target) + target.defense_value
    
class Archer(Character):
    def compute_damages(self, roll, target):
        print("🏹 Arrow hit you ! (+5dmg)")
        return super().compute_damages(roll,target) +5


class Druid(Character):
    def __init__(self, name, hp_max, attack_value, defense_value, mana_max, dice, exp_reward, healing_value):
        super().__init__(name, hp_max, attack_value, defense_value, dice, exp_reward)
        self.mana_max = mana_max
        self.mana = mana_max  # Mettre à jour la valeur initiale de self.mana pour qu'elle soit égale à mana_max
        self.healing_value = healing_value
        self.allies = []

    def get_mana_max(self) -> int:
        return self.mana_max

    def heal_ally(self, target : Character):
        if target in self.allies and self.mana >= self.mana_cost():
            heal_amount = min(self.healing_value, target.hp_max - target.hp)
            target.increase_hp(heal_amount)
            print(f"{self.name} [green]soigne[/green] {target.name} de {self.healing_value} pv (mana: {self.mana}/{self.mana_max})")
            target.show_healthbar()
        else:
            print(f"{self.name} n'a pas assez de mana pour lancer un sort.")

    def show_manabar(self):
        print(
            f"[{'🔵' * self.mana}{'⚪' * (self.mana_max - self.mana)}] {self.mana}/{self.mana_max}mana")

    def mana_cost(self):
        return random.randint(1,5)
    
    def cast_spell(self, target):
        self.show_manabar()
        mana_cost = self.mana_cost()  # Déterminer un coût de mana aléatoire entre 1 et self.mana_max
        if target in self.allies and self.mana >= mana_cost:
            self.mana -= mana_cost
            self.heal_ally(target)
            print(f"{self.name} [green]lance un sort[/green] sur {target.name} (mana: {self.mana}/{self.mana_max})")
        elif target not in self.allies:
            print("Cet allié n'est pas dans la liste des alliés.")
        else:
            print(f"{self.name} n'a pas assez de mana pour lancer un sort.")
        self.show_manabar()



