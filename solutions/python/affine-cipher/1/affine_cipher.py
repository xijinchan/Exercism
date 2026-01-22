alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encode(plain_text, a, b):
    if modInverse(a, 26) == None: raise ValueError('a and m must be coprime.') 
    output = ''

    for character in plain_text:
        if not any([character.isnumeric() == True, character.isalpha() == True]): continue
        if character.isnumeric() is True:
            output += str(character)
            continue
        output += alphabet[(a * alphabet.index(character.lower()) + b) % 26]
        
    output_formatted = ' '.join([output[k:k+5] for k in range(0,len(output),5)])

    return output_formatted


def decode(ciphered_text, a, b):
    if modInverse(a, 26) == None: raise ValueError('a and m must be coprime.')
    output = ''
    
    for y in ciphered_text:
        if y == ' ': continue
        if y.isnumeric() is True:
            output += y
            continue
        output += alphabet[((modInverse(a, 26)) * (alphabet.index(y) - b)) % 26]

    return output
    
def gcdExtended(a, b):
    global x, y
 
    # Base Case
    if (a == 0):
        x = 0
        y = 1
        return b
 
    # To store results of recursive call
    gcd = gcdExtended(b % a, a)
    x1 = x
    y1 = y
 
    # Update x and y using results of recursive
    # call
    x = y1 - (b // a) * x1
    y = x1
 
    return gcd

def modInverse(A, M):
 
    g = gcdExtended(A, M)
    if (g != 1):
        return None
 
    else:
 
        # m is added to handle negative x
        res = (x % M + M) % M
        return res