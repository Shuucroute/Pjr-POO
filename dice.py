import random


class Dice:
    def __init__(self, color, faces):
        self.color = color
        self.faces = faces
        self.material = "wood"

    def __str__(self):
        return f"I'm a {self.faces} faces dice !"

    def __eq__(self, another_dice: object) -> bool:
        if self.faces == another_dice.faces:
            return True
        else:
            return False

    def roll(self):
        return random.randint(1, self.faces)


class RiggedDice(Dice):
    def roll(self):
        return self.faces


# a_dice = Dice("blue", 6)
# print(a_dice.roll())

# a_second_dice = Dice("blue", 6)
# print(a_second_dice.roll())

# print(a_dice)
# print(a_dice == a_second_dice)
