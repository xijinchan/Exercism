'''Determine if sentence is pangram (includes all letters of alphabet)'''

def is_pangram(sentence):
    letters = []

    for character in sentence:
        if character.lower() not in letters and character.isalpha() is True:
            letters.append(character)

    return bool(len(letters) == 26)
        
