import math

def score(x, y):
    distance = math.sqrt((x ** 2) + (y ** 2))
    print(distance)

    if distance > 10: return 0
    if 5 < distance <= 10: return 1
    if 1 < distance <= 5: return 5
    if distance <= 1: return 10
