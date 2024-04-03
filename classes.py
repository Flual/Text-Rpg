import random
class Player:

    chosenclass = "bard"
    hp = 16 + random.randint(1, 6)
    Charisma = random.randint(12, 18)
    # Charisma = 10


class Weapon:
    type = "Rapier"
    damage = 4 + random.randint(1, 4)
