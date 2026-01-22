def combinations(target, size, exclude):    
    candidates = [k+1 for k in range(size)]
    found = []

    def incrementer(target, list):
        if sum(list) == target and len([k for k in list if k in exclude]) == 0:
            found.append([k for k in list])
        if sum(list) >= len(list) * 9: return [list]
            
        # look for left-most digit != 9
        for k in range(-1, -len(list)-1, -1):
            if list[k] !=9:
                list[k] += 1
                if list[k] in exclude: list[k] += 1 # skip if incremented digit is in exclusions
                for l in range(k+1, 0): # reset all digits on right to +1 whatever is to their left
                    list[l] = list[l-1] + 1
                break
        return incrementer(target, list)

    incrementer(target, candidates)
    return found