import random
class Player:

    chosenclass = "bard"
    hp = 16 + random.randint(1, 6)
    Strength = 10
    Dexterity = 14
    Constitution = 13
    Intelligence = 12
    Wisdom = 10
    Charisma = 16



class Weapon:
    type = "Rapier"
    damage = 4 + random.randint(1, 4)
