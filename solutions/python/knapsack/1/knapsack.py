from itertools import combinations

def maximum_value(maximum_weight, items):
    if items == []: return 0
    if min([k['weight'] for k in items]) > maximum_weight: return 0

    highest_value = 0
    highest_value_combination = None
    
    for m in range(len(items),0,-1):
        candidates = [k for k in combinations(items, m)]
        
        for candidate in candidates:
            total_weight = sum([k['weight'] for k in candidate])
            if total_weight > maximum_weight: continue
            total_value = sum([k['value'] for k in candidate])
            if total_value > highest_value:
                highest_value = total_value
    
    return highest_value