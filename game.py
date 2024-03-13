from dice import Dice
from character import Character

char1 = Character("James", 20, 8, 3, Dice("red", 6))
char2 = Character("Lisa", 20, 8, 3, Dice("blue", 6))

while char1.is_alive() and char2.is_alive():
    char1.attack(char2)
    char2.attack(char1)