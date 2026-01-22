def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    def find_factors(number):
        factors = []

        if number > 0 and isinstance(number, int) == True:
            for current_number in range(1, number):
                if number % current_number == 0:
                    factors.append(current_number)

            return factors
        else:
            raise ValueError("Classification is only possible for positive integers.")

    factors = find_factors(number)

    if sum(factors) == number:
        return "perfect"
    if sum(factors) > number:
        return "abundant"
    if sum(factors) < number:
        return "deficient"
    