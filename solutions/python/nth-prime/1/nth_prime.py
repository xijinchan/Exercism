def prime(number):
    if number == 0: raise ValueError('there is no zeroth prime')
        
    primes_found = 0
    primes = []
    is_prime = True
    candidate = 2

    while primes_found != number:
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
            primes_found += 1
            primes.append(candidate)
        if primes_found == number: return candidate

        if candidate >= 3:
            candidate += 2
        else:
            candidate += 1                