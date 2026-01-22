def roman(number):
    letters = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M'}
    romanised = ''

    for digit_index, digit in enumerate(str(number)):
        reverse_digit_index = abs(digit_index - (len(str(number)) - 1))

        try:
            romanised = letters[number]
        except:
            if int(digit) < 4:
                romanised += int(digit) * letters[int(str(1) + (reverse_digit_index * '0'))]
            elif int(digit) == 4:
                romanised += letters[int(str(1) + (reverse_digit_index * '0'))] + letters[int(str(5) + (reverse_digit_index * '0'))]
            elif int(digit) == 5:
                romanised += letters[int(str(5) + (reverse_digit_index * '0'))]
            elif int(digit) < 9:
                romanised += letters[int(str(5) + (reverse_digit_index * '0'))] + (int(digit) - 5) * letters[int(str(1) + (reverse_digit_index * '0'))]
            elif int(digit) == 9:
                romanised += letters[int(str(1) + (reverse_digit_index * '0'))] + letters[int(str(1) + ((reverse_digit_index + 1) * '0'))]
            
    return romanised