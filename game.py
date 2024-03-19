from character import Character, Warrior, Mage, Thief, Archer, Druid
from ennemis import Zombie, Skeletons, Goblins, Trolls
from dice import Dice

class Joueur(Character):
    def __init__(self, nom, vie, force, defense, dice, exp_reward) -> None:
        super().__init__(nom, vie, force, defense, dice, exp_reward)

class Allie(Character):
    pass

class Donjon:
    def __init__(self, nom, ennemis):
        self.nom = nom
        self.ennemis = ennemis

def combat(joueur, allie, ennemis):
    while ennemis:
        print("\nChoisissez une action :")
        print("1. Attaquer")
        print("2. Utiliser un objet")
        print("3. Fuir")
        choix = input("Entrez le numéro de l'action (1/2/3) : ")

        if choix == "1":
            ennemi = ennemis[0]
            joueur.attack(ennemi)
            if not ennemi.is_alive():
                print(f"{ennemi.name} a été vaincu !")
                ennemis.pop(0)
            else:
                print(f"{ennemi.name} contre-attaque !")
                allie.attack(joueur)
                if not joueur.is_alive():
                    print(f"{joueur.name} a été vaincu !")
                    break
                else:
                    print(f"{joueur.name} a résisté à l'attaque de {ennemi.name} !")
        elif choix == "2":
            print("Aucun objet n'est disponible pour l'instant.")
        elif choix == "3":
            print("Vous fuyez le combat !")
            break
        else:
            print("Action invalide.")

def start_game():
    print("Bienvenue dans le jeu !")
    joueur = Joueur("Cloud", 100, 15, 10, Dice("black", 6))
    allie = Allie("Barret", 120, 12, 8, Dice("black", 6))
    donjons = [
        Donjon("Donjon 1", [
            Zombie("Zombie", 40, 8, 2, Dice("green", 6)),
            Zombie("Zombie", 40, 8, 2, Dice("green", 6)),
            Zombie("Zombie", 40, 8, 2, Dice("green", 6)),
            Zombie("Zombie", 40, 8, 2, Dice("green", 6))
        ]),
        Donjon("Donjon 2", [
            Skeletons("Squelette", 50, 10, 4, Dice("white", 6)),
            Skeletons("Squelette", 50, 10, 4, Dice("white", 6)),
            Skeletons("Squelette", 50, 10, 4, Dice("white", 6)),
            Skeletons("Squelette", 50, 10, 4, Dice("white", 6))
        ]),
        Donjon("Donjon 3", [
            Goblins("Gobelin", 50, 10, 5, Dice("white_green", 6)),
            Goblins("Gobelin", 50, 10, 5, Dice("white_green", 6)),
            Goblins("Gobelin", 50, 10, 5, Dice("white_green", 6)),
            Goblins("Gobelin", 50, 10, 5, Dice("white_green", 6))
        ]),
        Donjon("Donjon 4", [
            Trolls("Troll", 90, 20, 8, Dice("black", 6)),
            Trolls("Troll", 90, 20, 8, Dice("black", 6)),
            Trolls("Troll", 90, 20, 8, Dice("black", 6)),
            Trolls("Troll", 90, 20, 8, Dice("black", 6))
        ])
    ]

    for donjon in donjons:
        print(f"Vous entrez dans le {donjon.nom} !")
        combat(joueur, allie, donjon.ennemis)
        if not joueur.is_alive():
            print("Vous avez été vaincu ! Fin du jeu.")
            break
        elif not allie.is_alive():
            print("Votre allié a été vaincu ! Fin du jeu.")
            break
        else:
            print(f"Vous avez vaincu le {donjon.nom} ! Passage au donjon suivant...")
            # Ajoutez ici la logique pour passer au donjon suivant
            input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    start_game()
