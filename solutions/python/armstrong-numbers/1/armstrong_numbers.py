def is_armstrong_number(number):
    total = 0
    
    for digit in str(number):
        no_of_digits = len(str(number))
        total += int(digit) ** no_of_digits

    return bool(total == number)