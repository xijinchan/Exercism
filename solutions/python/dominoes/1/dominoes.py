import itertools

def can_chain(dominoes):

    if dominoes == []:
        return []

    candidate_set = []
    candidate_set_variations = []

    # variations with reversed dominoes
    for m in range(len(dominoes)):
        for n in range(0,int(len(dominoes)/2)+1):
            candidate_set_variations.append([k[::-1] if m <= i <= m+n else k for i,k in enumerate(dominoes)])
        
    def solve(dominoes_set):
        solution = ([dominoes_set[k] for k in candidate_set_]
            for candidate_set_ in itertools.permutations(range(len(dominoes_set)))
            if dominoes_set[candidate_set_[0]][0] == dominoes_set[candidate_set_[-1]][1]
            if all([True if dominoes_set[k][1] == dominoes_set[candidate_set_[i+1]][0] else False for i, k in enumerate(candidate_set_[:-1])])
            )
        try:
            return next(solution)
        except StopIteration:
            return None

    candidate_set = solve(dominoes)
    if candidate_set:
        return candidate_set
        
    if candidate_set_variations == []:
        return None

    for variation in candidate_set_variations:
        candidate_set = solve(variation)
        if candidate_set:
            return candidate_set
                
    return None