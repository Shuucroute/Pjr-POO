from character import Character
from ennemis import Zombie
from dice import Dice

# Création d'une instance de joueur
player = Character("Nom du personnage", 100, 30, 5, dice=Dice("Blue", 6), exp_reward=1)

# Création d'une liste d'ennemis
zombies = [Zombie() for _ in range(2)]  # Crée 5 zombies

# Combat contre les zombies
for zombie in zombies:
    while player.is_alive() and zombie.is_alive():
        player.attack(zombie)
        if zombie.is_alive():
            zombie.attack(player)

        # Vérifie si le joueur est vivant après chaque attaque
        if not player.is_alive():
            print("Le joueur est mort!")
            break
        # Vérifie si le zombie est mort après chaque attaque
        elif not zombie.is_alive():
            print("Le zombie est mort!")
            zombie.defeat(player, len(zombies))  # Passe l'instance du joueur comme argument
            break


# Affiche les statistiques du joueur après les combats
print(player)