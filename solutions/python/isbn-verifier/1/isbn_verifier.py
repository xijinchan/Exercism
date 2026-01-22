def is_valid(isbn):
    digits = []
    valid = True

    for character in isbn:
        try:
            digits.append(int(character))
        except ValueError:
            if character == "X" and character == isbn[-1]:
                digits.append(10)
            elif character == "-":
                continue
            else:
                # digits.append(0)
                valid = False
                continue

    if len(digits) != 10: valid = False 
    
    # checksum = (digits[0] * 10 + digits[1] * 9 + digits[2] * 8 + digits[3] * 7 + digits[4] * 6 + digits[5] * 5 + digits[6] * 4 + digits[7] * 3 + digits[8] * 2 + digits[9] * 1) % 11

    if valid == True:
        checksum = 0
        
        for index in range(1, len(digits) + 1):
            print(index)
            checksum = checksum + (digits[index - 1] * (len(digits) - (index - 1)))
    
        checksum = checksum % 11
    
        return bool(checksum == 0)
    else:
        return False
        


        

