def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    else:
        grains = 1 * (2 ** (number - 1))
        return grains

def total():
    total = 0

    for square_no in range(1,65):
        total = total + square(square_no)

    return total
