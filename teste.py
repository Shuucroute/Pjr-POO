from character import Character
from ennemis import Zombie_guerrier
from dice import Dice

# Création d'une instance de joueur
player = Character("Nom du personnage", 100, 30, 5, dice=Dice(6), exp_reward=1)

# Création d'une liste d'ennemis
zombies = [Zombie_guerrier.create_enemy() for _ in range(1)] 

# Combat contre les zombies
for zombie in zombies:
    while player.is_alive() and zombie.is_alive():
        player.attack(zombie)
        if zombie.is_alive():
            zombie.attack(player)


        player.show_healthbar()
        player.show_expbar()


        if not player.is_alive():
            print("Le joueur est mort!")
            break

        elif not zombie.is_alive():
            print("Le zombie est mort!")
            zombie.defeat(player, len(zombies))  
            break


print (player)