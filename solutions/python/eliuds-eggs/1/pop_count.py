def egg_count(display_value):

    if display_value == 0:
        return 0

    remainder = None
    quotient = display_value
    binary_string = ''

    while quotient >= 1:
        remainder = int(quotient % 2)
        quotient = quotient / 2
        binary_string = str(remainder) + binary_string

    count = len([k for k in binary_string if k == '1'])        

    return count