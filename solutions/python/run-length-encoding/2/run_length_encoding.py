def decode(string):
    previous_index = 0
    counts = []
    characters = []
    
    for character in range(len(string)):
        if string[character].isalpha() is True or string[character] == ' ':
            if any([string[character - 1].isalpha(), string[character - 1] == ' ']):
                count = 1
            else:
                count = int(string[previous_index:character])
            previous_index = character + 1
            counts.append(count)
            characters.append(string[character])

    string_decoded = [a * b for a, b in zip(counts, characters)]
    string_decoded = ''.join(string_decoded)  
    return string_decoded

def encode(string):
    if string == '': return ''

    previous_index = 0
    string_encoded = ''

    for character in range(len(string)):
        try:
            if string[character + 1] != string[character]:
                count = str(len(string[previous_index:character + 1]))
                if count == '1': count = ''
                string_encoded = string_encoded + count + string[character]
                previous_index = character + 1
        except:
            if character == len(string) - 1:
                count = str(len(string[previous_index:character]) + 1)
                if count == '1' or count == '0': count = ''
                string_encoded = string_encoded + count + string[character]

    return string_encoded
             