def encode(numbers):
    # convert to binary
    binary = [bin(k) for k in numbers]
    binary = [str(k)[2:][::-1] for k in binary] # remove binary prefix

    # prefix all segments with 1, except last segment
    split = [['0'+('0'*(8-len(k[i:i+7])-1))+k[i:i+7][::-1] if i == 0 else '1'+('0'*(8-len(k[i:i+7])-1))+k[i:i+7][::-1]  for i in range(0,len(k),7)] for k in binary]
    
    for k in split:
        k.reverse()

    unpacked = [item for sublist in split for item in sublist]
    
    # convert to decimal
    output = [int(k, 2) for k in unpacked]

    return output
    
def decode(bytes_):
    if bytes_[-1] > 127: raise ValueError('incomplete sequence')
    binary = [str(bin(k))[2:] for k in bytes_] # remove binary prefix
    binary = [k if len(k) == 8 else ('0'*(8-len(k)))+k for k in binary] # add padded 0s

    # identify 0 prefix numbers
    zeros = [i for i, k in enumerate(binary) if k[0] == '0']

    # remove 0,1 prefixes
    output = [[k[1:] for k in binary[:zeros[0]+1]]]
    for i, k in enumerate(zeros[1:]):
        group = [k[1:] for k in binary[zeros[i]+1:zeros[i+1]+1]]
        output.append(group)
    output = [''.join(k) for k in output]
    
    # convert to decimal
    if len(zeros) == 0:
        output = [int(k, 2) for k in output]
    else:
        output = [int(k, 2) for k in output]

    return output
    