def sum_of_multiples(limit, multiples):
    factors = []
    factor = 0
    
    for number in range(0,limit):
        for multiple in multiples:
            if multiple == 0:
                factors.append(factor)
            elif number % multiple == 0:
                factor = number
                factors.append(factor)

    factors_dict = set(factors)
    return sum(factors_dict)
 