def transpose(lines):
    lines_split = lines.split('\n')
    longest_element = max(lines_split, key=len)
    longest_element_index = lines_split.index(longest_element)

    lines_split_padded = [k + (len(longest_element) - len(k)) * ' ' for k in lines_split]
    lines_transposed = [''.join([k[i] for k in lines_split_padded]) for i in range(len(longest_element))]

    # Delete trailing padding
    character_stop = longest_element_index
    for element in range(len(lines_transposed)-1,-1,-1):
        for character in range(len(lines_transposed[0])-1,character_stop,-1):
            if lines_transposed[element][character] == ' ':
                lines_transposed[element] = lines_transposed[element][:character]
            else:
                character_stop = character
                break
    
    return '\n'.join(lines_transposed).rstrip()