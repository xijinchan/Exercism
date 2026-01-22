def equilateral(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    return bool(a == b == c and a > 0)

def isosceles(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    inequality = bool(a + b < c or a + c < b or b + c < a)

    return bool((a == b or a == c or b == c) and inequality == False)
    
def scalene(sides):
    a = sides[0]
    b = sides[1]
    c = sides[2]

    inequality = bool(a + b < c or a + c < b or b + c < a)

    return bool((a != b and a != c and b!= c) and inequality == False)