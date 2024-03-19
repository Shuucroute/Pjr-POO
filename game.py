import character
import ennemis
from dice import Dice

class Donjon:
    def __init__(self, nom, ennemis):
        self.nom = nom
        self.ennemis = ennemis

def combat(joueur, allie, ennemis):
    print("Début du combat !")
    while True:
        # Gestion du tour du joueur
        print("Tour du joueur :")
        choix = input("Que voulez-vous faire ? (1. Attaquer, 2. Utiliser un objet, 3. Utiliser une compétence spéciale) : ")
        if choix == "1":
            ennemi_cible = choisir_ennemi(ennemis)
            joueur.attack(ennemi_cible)
        elif choix == "2":
            utiliser_objet(joueur)
        elif choix == "3":
            joueur.utiliser_competence_speciale(ennemi_cible)  # Appel de la compétence spéciale du joueur
        else:
            print("Choix invalide. Réessayez.")

        # Gestion des tours des ennemis
        print("Tour des ennemis :")
        for ennemi in ennemis:
            ennemi.attack(joueur)

        # Vérification de la fin du combat
        if joueur.is_defeated():
            print("Vous avez été vaincu !")
            break
        elif allie.is_defeated():
            print("Votre allié a été vaincu !")
            break
        elif all_enemies_defeated(ennemis):
            print("Vous avez vaincu tous les ennemis !")
            break

def choisir_ennemi(ennemis):
    print("Choisissez un ennemi à attaquer :")
    for i, ennemi in enumerate(ennemis):
        print(f"{i+1}. {ennemi}")
    while True:
        choix = input("Entrez le numéro correspondant à l'ennemi : ")
        if choix.isdigit() and 1 <= int(choix) <= len(ennemis):
            return ennemis[int(choix)-1]
        else:
            print("Choix invalide. Réessayez.")

def utiliser_objet(joueur):
    # Implémentez ici la logique pour utiliser un objet pendant le combat
    pass

class Joueur(character.Character):
    def __init__(self, nom, pv, attaque, defense):
        super().__init__(nom, pv, attaque, defense)

    def utiliser_competence_speciale(self, cible):
        print(f"{self.nom} utilise sa compétence spéciale !")
        # Implémentez ici la logique de la compétence spéciale
        # Par exemple, une compétence qui inflige des dégâts supplémentaires
        cible.subir_degats(20)

class Allie(character.Character):
    def __init__(self, nom, pv, attaque, defense):
        super().__init__(nom, pv, attaque, defense)

    def utiliser_competence_speciale(self, cible):
        print(f"{self.nom} utilise sa compétence spéciale !")
        # Implémentez ici la logique de la compétence spéciale pour l'allié
        # Par exemple, une compétence qui soigne le joueur
        cible.guerir(15)

def all_enemies_defeated(ennemis):
    return all(ennemi.is_defeated() for ennemi in ennemis)

def start_game():
    print("Bienvenue dans le jeu !")
    joueur = Joueur("Cloud", 100, 15, 10)
    allie = Allie("Barret", 120, 12, 8)
    donjons = [
        Donjon("Donjon 1", [
            ennemis.Zombie("Zombie", 40, 8, 2),
            ennemis.Zombie("Zombie", 40, 8, 2),
            ennemis.Zombie("Zombie", 40, 8, 2),
            ennemis.Zombie("Zombie", 40, 8, 2)
        ]),
        Donjon("Donjon 2", [
            ennemis.Squelette("Squelette", 50, 10, 4),
            ennemis.Squelette("Squelette", 50, 10, 4),
            ennemis.Squelette("Squelette", 50, 10, 4),
            ennemis.Squelette("Squelette", 50, 10, 4)
        ]),
        Donjon("Donjon 3", [
            ennemis.Gobelin("Gobelin", 50, 10, 5),
            ennemis.Gobelin("Gobelin", 50, 10, 5),
            ennemis.Gobelin("Gobelin", 50, 10, 5),
            ennemis.Gobelin("Gobelin", 50, 10, 5)
        ]),
        Donjon("Donjon 4", [
            ennemis.Troll("Troll", 90, 20, 8),
            ennemis.Troll("Troll", 90, 20, 8),
            ennemis.Troll("Troll", 90, 20, 8),
            ennemis.Troll("Troll", 90, 20, 8)
        ])
    ]

    for donjon in donjons:
        print(f"Vous entrez dans le {donjon.nom} !")
        combat(joueur, allie, donjon.ennemis)
        if joueur.is_defeated():
            print("Vous avez été vaincu ! Fin du jeu.")
            break
        elif allie.is_defeated():
            print("Votre allié a été vaincu ! Fin du jeu.")
            break
        else:
            print(f"Vous avez vaincu le {donjon.nom} ! Passage au donjon suivant...")
            # Ajoutez ici la logique pour passer au donjon suivant
            input("Appuyez sur Entrée pour continuer...")

if __name__ == "__main__":
    start_game()
