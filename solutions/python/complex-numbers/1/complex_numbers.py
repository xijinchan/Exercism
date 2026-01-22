import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __eq__(self, other):
        return bool(self.real == other.real and self.imaginary == other.imaginary)

    def __add__(self, other):
        if not isinstance(other, ComplexNumber): other = ComplexNumber(other, 0)
        
        sum_real = self.real + other.real
        sum_imaginary = self.imaginary + other.imaginary

        return ComplexNumber(sum_real, sum_imaginary)

    def __radd__(self, other):
        if type(other) in (int, float):
            return self + other
    
    def __mul__(self, other):
        if not isinstance(other, ComplexNumber): other = ComplexNumber(other, 0)
        
        a, c = self.real, other.real
        b, d = self.imaginary, other.imaginary
            
        return ComplexNumber(a * c - b * d, b * c + a * d)

    def __rmul__(self, other):
        if type(other) in (int, float):
            return self * other

    def __sub__(self, other):
        if not isinstance(other, ComplexNumber): other = ComplexNumber(other, 0)
        print('sub!')

        dif_real = self.real - other.real
        dif_imaginary = self.imaginary - other.imaginary

        print(dif_real)
        print(dif_imaginary)
            
        return ComplexNumber(dif_real, dif_imaginary)

    def __rsub__(self, other):
        print('rsub!')
        if type(other) in (int, float):
            return ComplexNumber(other, 0) - self

    def __truediv__(self, other):
        if not isinstance(other, ComplexNumber): other = ComplexNumber(other, 0)

        a, c = self.real, other.real
        b, d = self.imaginary, other.imaginary
        
        return ComplexNumber((a * c + b * d)/(c**2 + d**2),(b * c - a * d)/(c**2 + d**2))

    def __rtruediv__(self, other):
        if type(other) in (int, float):
            return ComplexNumber(other, 0) / self

    def __abs__(self):
        return math.sqrt(self.real ** 2 + self.imaginary ** 2)

    def conjugate(self):
        return ComplexNumber(self.real, -self.imaginary)

    def exp(self):
        a, b = self.real, self.imaginary
        e = math.e

        return ComplexNumber(e ** a, 0) * (ComplexNumber(math.cos(b), 0) + ComplexNumber(0, math.sin(b)))