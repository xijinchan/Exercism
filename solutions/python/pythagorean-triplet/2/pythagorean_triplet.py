import math

def triplets_with_sum(number):
    triplet_summands = []

    triplet_summands = [[int(math.sqrt((c-b)*(c+b))), b, c] for c in range(int(number / 3), int(number / 2)) for b in range(int(number / 4), c) if all([math.sqrt((c-b)*(c+b)) < b, math.sqrt((c-b)*(c+b)) + b + c == number])]

    return triplet_summands