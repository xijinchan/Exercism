def abbreviate(words):

    output = words[0]
    
    for character in range(1, len(words)):
        if words[character] == " " or words[character] == "-" or words[character] == "_":
            if words[character + 1].isalpha() == True:
                output = output + words[character + 1].upper()

    return output