from dice import Dice
from rich import print


# SOLID
# S
# D


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
        self.mana = mana_max
        self.healing_value = healing_value

    def has_enough_mana(self, mana_cost):
        return self.mana >= mana_cost

    def heal(self, target):
        if self.is_alive():
            if isinstance(self.healing_value, int) and self.has_enough_mana(5):
                roll = self.dice.roll()
                healing = self.healing_value + roll
                self.mana -= 5
                print(f"{self.name} [green]heals[green] {target.name} with {healing} pv")
                target.increase_hp(healing)
            else:
                print(f"{self.name} doesn't have enough mana to cast a spell.")
        else:
            print(f"{self.name} is not alive.")