def primes(limit):
    primes = []
    not_prime = []
    
    for number in range(2,limit+1):
        if number not in not_prime:
            primes.append(number)
            not_prime += [k for k in range(number * 2, limit+1, number) if k not in not_prime]

    return primes
