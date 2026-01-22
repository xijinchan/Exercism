alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def encode(plain_text):
    output = ''
    counter = 0

    for letter in plain_text:
        if letter.isalpha() == False:
            if letter.isnumeric() is True:
                if counter == 5:
                    output = output + ' ' + letter
                    counter = 1
                else:
                    output = output + letter
                    counter += 1
            continue 
        letter_index = [alphabet.index(k) for k in alphabet if k == letter.lower()][0]
        letter_index_reversed = 25 - letter_index
        
        if counter == 5:
            output = output + ' ' + alphabet[letter_index_reversed]
            counter = 1
        else:
            output = output + alphabet[letter_index_reversed]
            counter += 1

    return output


def decode(ciphered_text):
    output = ''
    
    for letter_ciphered in ciphered_text:
        if letter_ciphered.isalpha() == False:
            if letter_ciphered.isnumeric() is True: output += letter_ciphered
            continue
        letter_ciphered_index = [alphabet.index(k) for k in alphabet if k == letter_ciphered.lower()][0]
        letter_index = 25 - letter_ciphered_index
        output = output + alphabet[letter_index]

    return output
