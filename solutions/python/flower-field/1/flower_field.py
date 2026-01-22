def annotate(garden):
    if garden == []: return []
    
    row_length = len(garden)
    col_length = len(garden[0])
    garden_padded = []
    pad_row = "-" * (col_length + 2)
    
    garden_padded.append(pad_row)
    
    for row in range(row_length):
        if len(garden[row]) != col_length: raise ValueError("The board is invalid with current input.")
        padded_row = "-" + garden[row] + "-"
        garden_padded.append(padded_row)
    
    garden_padded.append(pad_row)
    

    count_table = []
    
    for row in range(1, row_length + 1):
        row_string = ""
        for col in range(1, col_length + 1):
            if garden_padded[row][col] == '*':
                row_string += '*'
            elif garden_padded[row][col] == ' ':
                count = 0
                count += 1 if garden_padded[row-1][col-1] == '*' else 0
                count += 1 if garden_padded[row-1][col] == '*' else 0
                count += 1 if garden_padded[row-1][col+1] == '*' else 0
                count += 1 if garden_padded[row][col+1] == '*' else 0
                count += 1 if garden_padded[row+1][col+1] == '*' else 0
                count += 1 if garden_padded[row+1][col] == '*' else 0
                count += 1 if garden_padded[row+1][col-1] == '*' else 0
                count += 1 if garden_padded[row][col-1] == '*' else 0
                if count == 0:
                    row_string += " "
                else:
                    row_string += str(count)
            else:
                raise ValueError("The board is invalid with current input.")

        
        count_table.append(row_string)
    
    return count_table