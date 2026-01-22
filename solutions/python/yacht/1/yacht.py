# Score categories.
# Change the values as you see fit.
YACHT = 'YACHT'
ONES = 'ONES'
TWOS = 'TWOS'
THREES = 'THREES'
FOURS = 'FOURS'
FIVES = 'FIVES'
SIXES = 'SIXES'
FULL_HOUSE = 'FULL_HOUSE'
FOUR_OF_A_KIND = 'FOUR_OF_A_KIND'
LITTLE_STRAIGHT = 'LITTLE_STRAIGHT'
BIG_STRAIGHT = 'BIG_STRAIGHT'
CHOICE = 'CHOICE'


def score(dice, category):
    dice.sort()

    if category == 'YACHT' and sum(dice) == dice[0] * 5:
        return 50
    if category == 'BIG_STRAIGHT' and dice == [2,3,4,5,6]:
        return 30
    if category == 'LITTLE_STRAIGHT' and dice == [1,2,3,4,5]:
        return 30

    counts = dict((i, dice.count(i)) for i in dice)
    threes_sum = None
    twos_sum = None
    fours_sum = None

    for pips in counts:
        match counts.get(pips):
            case 4:
                fours_sum = pips * 4
            case 3:
                threes_sum = pips * 3
            case 2:
                twos_sum = pips * 2
 
    if category == 'FULL_HOUSE' and threes_sum != None and twos_sum != None:
            return threes_sum + twos_sum
    if category == 'FOUR_OF_A_KIND' and fours_sum != None:
            return fours_sum
    if category == 'FOUR_OF_A_KIND' and sum(dice) == dice[0] * 5:
            return dice[0] * 4
    if category == 'SIXES': return 6 * dice.count(6)
    if category == 'FIVES': return 5 * dice.count(5)
    if category == 'FOURS': return 4 * dice.count(4)
    if category == 'THREES': return 3 * dice.count(3)
    if category == 'TWOS': return 2 * dice.count(2)
    if category == 'ONES': return 1 * dice.count(1)
    if category == 'CHOICE': return sum(dice)

    return 0