def prime(number):
    if number == 0: raise ValueError('there is no zeroth prime')
        
    primes = []
    is_prime = True
    candidate = 2

    while len(primes) != number:
        is_prime = True

        if candidate <= 3:
            for each_number in range(2, candidate):

                if candidate % each_number == 0:
                    is_prime = False
                    break
                else:
                    continue
        else:
            for each_prime in primes:
                if candidate % each_prime == 0:
                    is_prime = False
                    break
                else:
                    continue

        if is_prime == True:
            primes.append(candidate)
        if len(primes) == number: return candidate

        if candidate >= 3:
            candidate += 2
        else:
            candidate += 1                