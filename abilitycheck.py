from classes import *
import random

roll = random.randint(1,20)


def ability_check():
    if Player.Charisma >= 12 and Player.Charisma < 14:
        return roll + 1

    if Player.Charisma >= 14 and Player.Charisma < 16:
        return roll + 2

    if Player.Charisma >= 16 and Player.Charisma < 18:
        return roll + 3

    if Player.Charisma >= 18 and Player.Charisma < 20:
        return roll + 4
    else:
        return roll





