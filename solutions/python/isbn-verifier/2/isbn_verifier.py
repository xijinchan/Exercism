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
                valid = False
                continue

    if len(digits) != 10: valid = False 

    if valid == True:
        checksum = 0
        
        for index in range(1, len(digits) + 1):
            checksum = checksum + (digits[index - 1] * (len(digits) - (index - 1)))
    
        checksum = checksum % 11
    
        return bool(checksum == 0)
    else:
        return False
        


        

