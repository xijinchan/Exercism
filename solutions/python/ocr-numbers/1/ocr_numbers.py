def convert(input_grid):
    if len(input_grid) % 4 is not 0: raise ValueError("Number of input lines is not a multiple of four")
    if len(input_grid[0]) % 3 is not 0: raise ValueError("Number of input columns is not a multiple of three") 
        
    digits = [
        [' _ ', '| |', '|_|', '   '],
        ['   ', '  |', '  |', '   '],
        [' _ ', ' _|', '|_ ', '   '],
        [' _ ', ' _|', ' _|', '   '],
        ['   ', '|_|', '  |', '   '],
        [' _ ', '|_ ', ' _|', '   '],
        [' _ ', '|_ ', '|_|', '   '],
        [' _ ', '  |', '  |', '   '],
        [' _ ', '|_|', '|_|', '   '],
        [' _ ', '|_|', ' _|', '   ']
    ]
    
    input_grid_grouped = [[input_grid[p][k:k+3] for k in range(0,len(input_grid[p][:-2]),3)] for p in range(len(input_grid))]
    zipped = [list(k) for k in zip(*input_grid_grouped)]
    
    commas = False

    # for last test
    if len(zipped[0]) > 4:
        zipped = [zipped[j][k:k+4] for j in range(len(zipped)) for k in range(0,len(zipped[j]),4)]
        zipped = [list(k) for k in zip(*[zipped[k:k+3] for k in range(0,len(zipped),3)])]
        zipped = [item for sublist in zipped for item in sublist]
        commas = True

    output = ''.join([str(digits.index(k)) if k in digits else '?' for k in zipped])

    if commas == True:
        output = ','.join([output[k:k+3] for k in range(0,len(output),3)])

    return output