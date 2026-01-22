def factors(value):
    divisor = 2
    prime_factors = []
    endloop = False

    class PrimeFactors():

        def __init__(self, value, divisor, prime_factors, endloop):
            self.current_value = value
            self.current_divisor = divisor
            self.prime_factors = prime_factors
            self.endloop = endloop
        
        def __iter__(self):
            return self
            
        def __next__(self):
            while self.endloop == False and self.current_value % self.current_divisor == 0:
                self.current_value = self.current_value / self.current_divisor
                if self.current_value == 1 or self.current_value < 1: self.endloop = True
                prime_factors.append(self.current_divisor)
            self.current_divisor += 1
            if self.current_value <= 1: self.endloop = True
            return self.current_value

    myclass = PrimeFactors(value, divisor, prime_factors, endloop)
    myiter = iter(myclass)

    while myiter.endloop == False:
        next(myiter)

    return prime_factors