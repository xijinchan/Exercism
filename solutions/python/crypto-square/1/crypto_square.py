import math
import string

def cipher_text(plain_text):
    if plain_text == '': return ''
        
    normalised = plain_text.translate(str.maketrans('','',string.punctuation)).lower()
    normalised = normalised.replace(' ','')
    no_of_rows = int(math.sqrt(len(normalised)))
    
    if len(normalised) / no_of_rows == no_of_rows:
        no_of_columns = no_of_rows
    elif no_of_rows * (no_of_rows + 1) >= len(normalised):
        no_of_columns = no_of_rows + 1
    else:
        no_of_columns = no_of_rows + 1
        no_of_rows = no_of_columns

    normalised = normalised + (' ' * (no_of_rows * no_of_columns - len(normalised)))
    transposed = ' '.join([''.join([normalised[k] for k in range(i,len(normalised),no_of_columns)]) for i in range(0,no_of_columns)])

    return(transposed)