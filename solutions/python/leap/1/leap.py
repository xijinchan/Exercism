'''returns whether year is Gregorian calendar leap year or not'''

def leap_year(year):
    if year % 4 == 0:
        if year % 100 != 0:
            output = True
        elif year % 400 == 0:
            output = True
        else:
            output = False
    else:
        output = False

    return output
