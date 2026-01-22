class Rational:
    def __init__(self, numer, denom):
        GCD = greatest_common_denom(numer, denom)
        if numer == 0:
            self.numer = 0
            self.denom = 1
        elif denom > -1:
            self.numer = numer / GCD
            self.denom = denom / GCD
        else:
            self.numer = -1 * numer / GCD
            self.denom = -1 * denom / GCD

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return f'{self.numer}/{self.denom}'

    def __add__(self, other):
        c = self.numer * other.denom + other.numer * self.denom
        d = self.denom * other.denom
        
        GCD = greatest_common_denom(c, d)
        return Rational(c / GCD, d / GCD)

    def __sub__(self, other):
        c = self.numer * other.denom - other.numer * self.denom
        d = self.denom * other.denom

        GCD = greatest_common_denom(c, d)
        return Rational(c / GCD, d / GCD)

    def __mul__(self, other):
        c = self.numer * other.numer
        d = self.denom * other.denom
        GCD = greatest_common_denom(c, d)
        
        return Rational(c / GCD, d / GCD)

    def __truediv__(self, other):
        c = self.numer * other.denom
        d = other.numer * self.denom
        GCD = greatest_common_denom(c, d)  
        
        return Rational(c / GCD, d / GCD)
        
    def __abs__(self):
        c = abs(self.numer)
        d = abs(self.denom)
        GCD = greatest_common_denom(c, d) 
        
        return Rational(c / GCD, d / GCD)

    def __pow__(self, power):
        c = self.numer ** abs(power)
        d = self.denom ** abs(power)
        GCD = greatest_common_denom(c, d)

        if power > 0:
            exp = Rational(c / GCD , d / GCD)
        else:
            exp = Rational(d / GCD , c / GCD)
        
        return exp

    def __rpow__(self, base):
        a = self.numer
        b = self.denom

        exp = (base ** a) ** (1 / b)

        return exp

def greatest_common_denom(a, b):
    if a == b: return a
    if a == 0 or b == 0: return 1

    if a > b:
        small = abs(b)
        result = abs(a - b)
    else:
        small = abs(a)
        result = abs(b - a)
    
    while result > small:
        result -= small
    
    if result - small == 0:
        return result
    
    if result - small < small:    
        result -= small
        return greatest_common_denom(small, result)

    return 1