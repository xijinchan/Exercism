'''returns if word is isogram (phrase without repeating letter)'''
def is_isogram(string):
    letters = []
    isogram = True
    
    for character in string:
        if character.lower() not in letters:
            if character.isalpha() is True:
                letters.append(character.lower())
        else:
            isogram = False

    if string == "": isogram = True

    return isogram
