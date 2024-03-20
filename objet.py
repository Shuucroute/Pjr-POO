from character import Character


 # Ajout de l'objet Bouclier 
        
     
class Shield(Character):
    def __init__(self, name, defense_bonus) -> None:
        self.name = name
        self.defense_bonus = defense_bonus
    
class WoodenShield(Shield):
    def __init__(self):
        self.price = 10
        super().__init__("Bouclier en bois", +1)

class BoneShield(Shield):
    def __init__(self):
        self.price = 20
        super().__init__("Bouclier en os", +2)

class IronShield(Shield):
    def __init__(self):
        self.price = 30
        super().__init__("Bouclier en fer", +3)

class CooperShield(Shield):
    def __init__(self):
        self.price = 40
        super().__init__("Bouclier en cuivre", +4)

    # Ajout de l'objet Epée 

class Sword(Character):
    def __init__(self, name, defense_bonus) -> None:
        self.name = name
        self.defense_bonus = defense_bonus

class WoodenSword(Sword):
     def __init__(self):
        self.price = 10
        super().__init__("Epée en bois", +1)

class IronSword(Sword):
    def __init__(self):
        self.price = 20
        super().__init__("Epée en fer", +2)

class DiamondSword(Sword):
    def __init__(self):
        self.price = 30
        super().__init__("Epée en diament", +3)

class Excalibur(Sword):
    def __init__(self):
        self.price = 40
        super().__init__("Excalibur", +4)
        


    # Ajout de l'objet Armure
        
        
class Armor(Character):
    def __init__(self, name, defense_bonus) ->None:
        self.name = name
        self.defense_bonus = defense_bonus

class LeatherArmor(Armor):
    def __init__(self):
        self.price = 10
        super().__init__("Armure en cuir", +1)

class IronArmor(Armor):
    def __init__(self):
        self.price = 20
        super().__init__("Armure en fer", +2)

class Chainmail(Armor):
    def __init__(self):
        self.price = 30
        super().__init__("Cotte de maille", +3)

class EndiumArmor(Armor):
    def __init__(self):
        self.price = 40
        super().__init__("Armure Endium", +4)

    
    # Ajout de l'objet Baton magique 
        
        
class Stick(Character):
    def __init__(self, name, defense_bonus) ->None:
        self.name = name
        self.defense_bonus = defense_bonus

class FireStick(Stick):
    def __init__(self):
        self.price = 10
        super().__init__("Baton de feu", +1)

class IceStick(Stick):
    def __init__(self):
        self.price = 20
        super().__init__("Baton de glace", +2)

class WindStick(Stick):
    def __init__(self):
        self.price = 30
        super().__init__("Baton de vent", +3)

class UltimateStick(Stick):
    def __init__(self):
        self.price = 40
        super().__init__("Baton ultime", +4)

    # Ajout de l'objet Dague
        
        
class Dagger(Character):
 def __init__(self, name, attack_bonus) -> None:
        self.name = name
        self.attakc_bonus = attack_bonus

class WoodenDagger(Dagger):
    def __init__(self):
        self.price = 10
        super().__init__("Dague en bois", +1)

class SilverDagger(Dagger):
    def __init__(self):
        self.price = 20
        super().__init__("Dague en argent", +2)

class CoperDagger(Dagger):
    def __init__(self):
        self.price = 30
        super().__init__("Dague en cuivre", +3)

class GoldDagger(Dagger):
    def __init__(self):
        self.price = 40
        super().__init__("Dague en or", +4)

        # Ajout de l'objet Arc 


class Arc(Character):
 def __init__(self, name, attack_bonus) -> None:
        self.name = name
        self.attakc_bonus = attack_bonus

class ClassicArc(Arc):
     def __init__(self):
        self.price = 10
        super().__init__("Arc classique", +1)

class LongArc(Arc):
     def __init__(self):
        self.price = 20
        super().__init__("Arc long", +2)

class Arbalète(Arc):
     def __init__(self):
        self.price = 30
        super().__init__("Arbalète", +3)

class TripleArc(Arc):
    def __init__(self):
        self.price = 40
        super().__init__("Arc triple", +4)

        # Ajout de l'objet Cape
        

class Cape(Character):
    def __init__(self, name):
        self.name = name

        def apply_effects(self, character):
            pass

class ManaCape(Cape):
    def __init__(self):
        self.price = 10
        super().__init__("Cape de Mana", +10) #ManaBonus

class HealCape(Cape):
    def __init__(self):
        self.price = 20        
        super().__init__("Cape de heal", +15) #HealBonus

class DefenseCape(Cape):
    def __init__(self):
        self.price = 30
        super().__init__("Cape de défense", +5) #DefenseBonus

class UltimateCape(Cape):
    def __init__(self):
        self.price = 40
        super().__init__("Cape Ultime", +10, +15, +5) 

