import random
import math

def dice():
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    d = random.randint(1,6)

    values = [a,b,c,d]
    values.sort()
    return sum(values[1:])

class Character:

    def __init__(self):
        self.strength = dice()
        self.dexterity = dice()
        self.constitution = dice()
        self.intelligence = dice()
        self.wisdom = dice()
        self.charisma = dice()
        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        abilities = [self.strength, self.dexterity, self.constitution, self.intelligence, self.wisdom, self.charisma]
        return abilities[random.randint(0,5)]

def modifier(score):
    result = math.floor((score - 10) / 2)
    return result
