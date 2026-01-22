import itertools

def solve(puzzle):
    letters_dict = dict.fromkeys({k for k in puzzle if k.isalpha() == True})
    letters = [k for k in letters_dict]
    letters.sort()

    letter_to_number = {letter: str(index) for index, letter in enumerate(letters)}
    puzzle_parsed = ''.join([letter_to_number[k] if k.isalpha() is True else k for k in puzzle])

    # find crude max total if left hand side of equation digits were all 9
    left_right_puzzle_parsed = [k for k in puzzle_parsed.split(' == ')]
    right_max_crude = eval(''.join([str(9) if k.isdigit() is True else k for k in left_right_puzzle_parsed[0]]))
    left_max_len = max([len(k) for k in left_right_puzzle_parsed[0].split(' ')])


    def evaluate_str(letters, puzzle_parsed, right_max_crude):
        try:
            expression = ''.join([str(letters[int(k)]) if k.isdigit() is True else k for k in puzzle_parsed])

            if left_max_len < len(str(right_max_crude)):
                # stop evaluation if right side greater than crude max total
                if int(expression.split(' == ')[1]) > right_max_crude: return False
            
            # stop if leading 0s
            if [k for k in expression.split(' ') if k[0] == '0' and len(k) > 1]:
                return False
            
            return eval(expression)
        except:
            return False
        

    solution = ([*letters]
        for [*letters] in itertools.permutations(range(10), len(letters))
        if evaluate_str(letters, puzzle_parsed, right_max_crude)
        )
    
    try:
        output = next(solution)
    except:
        return None

    letters_dict.update(zip(letters, output))

    return letters_dict

