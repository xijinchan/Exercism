def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        index = 0
        distance = 0
        for letter in strand_a:
            if letter != strand_b[index]: distance += 1
            index +=1

    return distance