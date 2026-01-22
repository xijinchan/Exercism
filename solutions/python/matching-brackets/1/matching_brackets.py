def is_paired(input_string):
    brackets = ['[',']','{','}','(',')']
    bracket_pairs = {
        "[": "]",
        "{": "}",
        "(": ")"
    }

    input_string_brackets = [k for k in input_string if k in brackets]
    
    if input_string == '': return True
    if len(input_string_brackets) % 2 != 0: return False

    for i in range(len(input_string_brackets)):
        for k in range(len(input_string_brackets) - 1):
            try:
                if bracket_pairs[input_string_brackets[k]] == input_string_brackets[k+1]:
                    input_string_brackets = input_string_brackets[:k] + input_string_brackets[(k+2):]
            except:
                continue
    
    if input_string_brackets == []:
        return True
    else:
        return False