def annotate(minefield):
    if minefield == [] or minefield == ['']: return minefield
    if len(minefield[0]) * len(minefield) != len(''.join(minefield)) or len(''.join([''.join([m for m in k if m not in ' *']) for k in minefield])) > 0: raise ValueError("The board is invalid with current input.")
    
    minefield_padded = [*[' ' * (len(minefield[0])+2)],*[' ' + str(k) + ' ' for k in minefield],*[' ' * (len(minefield[0])+2)]]

    counts = [''.join([str([minefield_padded[i][j + 1] == '*', # count top
                            minefield_padded[i + 2][j + 1] == '*', # bottom
                            minefield_padded[i + 1][j] == '*', # left
                            minefield_padded[i + 1][j + 2] == '*', # right
                            minefield_padded[i][j] == '*', # top left
                            minefield_padded[i][j + 2] == '*', # top right
                            minefield_padded[i + 2][j] == '*', # bottom left
                            minefield_padded[i + 2][j + 2] == '*', # bottom right
                           ].count(True)) if m != '*' else '*' for j, m in enumerate(k[1:-1])]) for i, k in enumerate(minefield_padded[1:-1])]

    counts = [k.replace('0',' ') for k in counts]
    return counts
