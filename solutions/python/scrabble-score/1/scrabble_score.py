def score(word):
    letter_scores = [
        [],
        ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'],
        ['D', 'G'],
        ['B', 'C', 'M', 'P'],
        ['F', 'H', 'V', 'W', 'Y'],
        ['K'],
        [],
        [],
        ['J', 'X'],
        [],
        ['Q', 'Z']
    ]

    score = 0
    
    for letter in word:
        for row in letter_scores:
            if letter.upper() in row:
                score += letter_scores.index(row)

    return score