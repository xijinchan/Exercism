def encode(message, rails):
    which_rail = ([k for k in range(rails)] + [k for k in range(rails-2,0,-1)])
    output = [[] for i in range(rails)]
    
    for i, letter in enumerate(message):
        output[which_rail[i % len(which_rail)]].append(letter)

    return ''.join([''.join(k) for k in output])


def decode(encoded_message, rails):
    which_rail = ([k for k in range(rails)] + [k for k in range(rails-2,0,-1)])
    indices = [[] for i in range(rails)]

    counter = 0
    for k in range(len(encoded_message)):
        if any([k % (2 * rails - 2) == 0, k % ((2 * rails - 2) / 2) == 0]): # if rail row
            indices[which_rail[k % len(which_rail)]].append(counter)
            counter += 1
        elif k % (rails * 2 - 2) < rails - 1: # if going down
            indices[which_rail[k % len(which_rail)]].append(counter)
            counter += 1
        elif k % (rails * 2 - 2) > rails - 1: # if going up
            indices[which_rail[k % len(which_rail)]].append(counter)
            counter += 1

    indices = [j for i in indices for j in i]
    
    message = ''.join([encoded_message[indices.index(k)] for k in range(len(encoded_message))])
    return message
