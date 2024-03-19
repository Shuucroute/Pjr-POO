from dice import Dice
import random

class Character:
    def __init__(self, name, hp_max, attack_value, defense_value, dice) -> None:
        self.name = name
        self.hp_max = hp_max
        self.hp = hp_max
        self.attack_value = attack_value
        self.defense_value = defense_value
        self.dice = dice

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
    def __init__(self, name, hp_max, attack_value, defense_value, dice, mana_max, healing_value):
        super().__init__(name, hp_max, attack_value, defense_value, dice)
        self.mana_max = mana_max
        self.mana = 20
        self.healing_value = healing_value
        self.allies = []

    def heal_ally(self, target):
        if target in self.allies and self.mana >= self.healing_value:
            heal_amount = min(self.healing_value, target.hp_max - target.hp)
            target.increase_hp(heal_amount)
            print(f"{self.name} [green]soigne[/green] {target.name} de {self.healing_value} pv (mana: {self.mana}/{self.mana_max})")
            target.show_healthbar()
        else:
            print(f"{self.name} n'a pas assez de mana pour lancer un sort.")

    def show_manabar(self):
        print(
            f"[{'🔵' * self.mana}{'⚪' * (self.mana_max - self.mana)}] {self.mana}/{self.mana_max}mana")        

    def cast_spell(self, target):
        self.show_manabar()
        mana_cost = random.randint(1, 5)  # Déterminer un coût de mana aléatoire entre 1 et 5
        if target in self.allies and self.mana >= mana_cost:
            self.mana -= mana_cost
            self.heal_ally(target)
            print(f"{self.name} [green]lance un sort[/green] sur {target.name} (mana: {self.mana}/{self.mana_max})")
        elif target in self.allies:
            print(f"{self.name} n'a pas assez de mana pour lancer un sort.")
        else:
            print("Cet allié n'est pas dans la liste des alliés.")
        self.show_manabar()