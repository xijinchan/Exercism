def rotate(text, key):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

    output = ""
    
    for letter in text:
        if letter.isalpha() == False:
            output = output + letter
        else:
            index = (alphabet.index(letter.lower()) + (key % 26)) % 26

            if letter == letter.lower():
                output = output + alphabet[index]
            else:
                output = output + (str(alphabet[index])).upper()

    return output
    