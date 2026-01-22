def steps(number):
    result = number
    steps = 0

    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    while result != 1:
        if result % 2 == 0: result = result / 2
        else: result = result * 3 + 1
        steps += 1
        if steps > 1000000:
            break

    return steps