def rows(letter):
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    width = (letters.index(letter) + 1) * 2 - 1
    output = [' '*(int(width / 2 + 1)) for _ in range(int(width / 2 + 1))] # Blank spaces upper right quadrant

    for i in range(letters.index(letter)+1): # Fill upper right quadrant with letters
        output[i] = output[i][:i] + letters[i] + output[i][i+1:]

    for j in range(len(output)): # Mirror to left to form upper left quadrant
        output[j] = output[j][-1:0:-1] + output[j]

    output = output + output[-2::-1] # Mirror for bottom half
    return output
    