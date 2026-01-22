class House:
    def __init__(self, color='', resident='',  animal='', drink='',smokes=''):
        self.color = color
        self.resident = Resident(resident)
        self.animal = animal
        self.drink = drink
        self.smokes = smokes

class Resident:
    def __init__(self, name,animal='', drink='', smokes=''):
        self.name = name
        self.animal = animal
        self.drink = drink
        self.smokes = smokes

def solve():
    # in order of instructions
    houses = []
    Englishman = Resident('Englishman')
    red = House('red')
    red.resident = Englishman
    Spaniard = Resident('Spaniard', 'dog')
    green = House('green', drink='coffee')
    Ukrainian = Resident('Ukrainian', drink='tea')
    ivory = House('ivory')
    houses += [ivory, green]
    old_gold_smoker = Resident('old_gold_smoker', animal='snails', smokes='old gold')
    yellow = House('yellow', smokes='kools')
    # instruction 9 'middle house drinks milk' after all houses created
    Norwegian = Resident('Norwegian')
    houses.insert(0, House('Norwegian_house'))
    houses[0].resident = Norwegian
    chesterfields_smoker = Resident('chesterfields_smoker', smokes='Chesterfields') # step 11 'fox' oart wait till last
    lucky_strike_smoker = Resident('lucky_strike_smoker', drink='orange juice')
    Japanese = Resident('Japanese', smokes='Parliaments')
    blue = House('blue')
    houses.insert(1, blue)

    # Deductions
    # Norwegian house must be remaining yellow, as Norwegian is next to blue
    houses[0].color = 'yellow'
    # yellow house has Kool smokes
    houses[0].smokes='kool'
    # horse is next to Kool smokes house
    blue.animal = 'horse'
    # red must be either house index 2 or 4, 4 ends in dead end with Old Gold smoke with snail instruction 7
    houses.insert(2, red)
    # middle house drinks milk (i nstruction 9)
    houses[2].drink = 'milk'

    # Ukrainian with tea either 1 or 3
    blue.resident = Ukrainian
    # lucky strike smoker remaining 1 or 3
    ivory.resident = lucky_strike_smoker
    # Japanese has to be green
    green.resident = Japanese
    # lucky_strike smoker has to be Spaniard
    lucky_strike_smoker.name, lucky_strike_smoker.animal, lucky_strike_smoker.smokes = 'Spaniard', 'dog', 'lucky strike'
    # old gold smoker with snail is Englishman, as only remaining without smokes and animal
    Englishman.smokes, Englishman.animal = 'Old Gold', 'snail'
    # Chesterfield smoker must be Ukrainian, fox owner must be Norwegian
    Ukrainian.smokes = 'Chesterfield'
    Norwegian.animal = 'fox'
    
    return houses

    
def drinks_water():
    houses = solve()
    
    for h in houses:
        if h.drink == '' and h.resident.drink == '':
            person = h.resident.name

    return person

def owns_zebra():
    houses = solve()

    for h in houses:
        if h.animal == '' and h.resident.animal == '':
            person = h.resident.name

    return person
