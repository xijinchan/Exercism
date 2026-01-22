def largest(min_factor, max_factor):
    """Given a range of numbers, find the largest palindromes which
       are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
             Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor: raise ValueError("min must be <= max")
        
    output = None
    product = None
    factors = []
    found = False

    # find factors that result in palindrome, search from highest number combinations
    for digit in range(max_factor, min_factor-1, -1):
        for digit_two in range(max_factor, digit-1, -1):
            if str(digit * digit_two) == str(digit * digit_two)[::-1]:
                product = digit * digit_two
                factors.append([digit, digit_two])
                found = True
                break
        if found == True: break

    max_no = max_factor * max_factor
    found = False

    # check for other palindromes greater than first-found palindrome
    if product != None:
        if len(str(product)) % 2 == 0:
            left_half = int(len(str(product)) / 2)
            for k in range(int(str(max_no)[:left_half])+1, int(str(product)[:left_half]), -1):
                palindrome_candidate = int(str(k) + str(k)[::-1])
                for factor_candidate in range(max_factor, min_factor-1, -1):
                    factor_candidate_two = palindrome_candidate / factor_candidate
                    if all([factor_candidate_two.is_integer() == True, min_factor-1 < int(factor_candidate_two) < max_factor+1, [factor_candidate, int(factor_candidate_two)] not in factors, [int(factor_candidate_two), factor_candidate] not in factors]):
                            product = palindrome_candidate
                            factors = [[factor_candidate, factor_candidate_two]]
                            found = True
                            break
                    if found == True: break
    
        # find any other factors
        for factor_candidate in range(min_factor, max_factor+1):
            factor_candidate_two = product / factor_candidate
            if all([factor_candidate_two.is_integer() == True, min_factor-1 < int(factor_candidate_two) < max_factor+1, [factor_candidate, int(factor_candidate_two)] not in factors, [int(factor_candidate_two), factor_candidate] not in factors]):
                        factors.append([factor_candidate, int(factor_candidate_two)])

    output = (product, factors)
    return output


def smallest(min_factor, max_factor):
    """Given a range of numbers, find the smallest palindromes which
    are products of two numbers within that range.

    :param min_factor: int with a default value of 0
    :param max_factor: int
    :return: tuple of (palindrome, iterable).
    Iterable should contain both factors of the palindrome in an arbitrary order.
    """
    if min_factor > max_factor: raise ValueError("min must be <= max")

    output = None
    product = None
    factors = []
    found = False

    # find factors that result in palindrome, search from lowest number combinations
    for digit in range(min_factor,max_factor):
        for digit_two in range(digit,max_factor):
            if str(digit * digit_two) == str(digit * digit_two)[::-1]:
                product = digit * digit_two
                factors.append([digit, digit_two])
                found = True
                break
        if found == True: break

    print(output)

    min_no = min_factor * min_factor
    found = False

    # check for other palindromes smaller than first-found palindrome
    if product != None:
        if len(str(product)) % 2 == 0:
            left_half = int(len(str(product)) / 2)
            for k in range(int(str(min_no)[:left_half])+1, int(str(product)[:left_half])):
                palindrome_candidate = int(str(k) + str(k)[::-1])
                for factor_candidate in range(min_factor, max_factor+1):
                    factor_candidate_two = palindrome_candidate / factor_candidate
                    if all([factor_candidate_two.is_integer() == True, min_factor-1 < int(factor_candidate_two) < max_factor+1, [factor_candidate, int(factor_candidate_two)] not in factors, [int(factor_candidate_two), factor_candidate] not in factors]):
                        product = palindrome_candidate
                        factors = [[factor_candidate, factor_candidate_two]]
                        found = True
                        break
                    if found == True: break

        # find any other factors
        for factor_candidate in range(min_factor, max_factor+1):
            factor_candidate_two = product / factor_candidate
            if all([factor_candidate_two.is_integer() == True, min_factor-1 < int(factor_candidate_two) < max_factor+1, [factor_candidate, int(factor_candidate_two)] not in factors, [int(factor_candidate_two), factor_candidate] not in factors]):
                factors.append([factor_candidate, int(factor_candidate_two)])

    output = (product, factors)
    return output
