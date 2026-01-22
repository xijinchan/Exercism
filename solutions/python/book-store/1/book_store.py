def total(basket):
    basket_sorted = [k for k in basket]
    basket_sorted.sort()
    print(basket_sorted)

    def grouping(max_n, basket_): # groupings upto length n
        sets_of_upto_n = [set()]
        for item in basket_:
            for current_set in sets_of_upto_n:
                if item not in current_set and len(current_set) < max_n:
                    current_set.add(item)
                    break
                if current_set == sets_of_upto_n[-1]:
                    new_set = {item}
                    sets_of_upto_n.append(new_set)
                    break

        return sets_of_upto_n

    def alt_grouping(max_n, basket_): # alternative grouping: single books distributed across groupings
        sets_of_upto_n = [{k} for k in basket_ if basket_.count(k) == 1]
        if sets_of_upto_n == []:
            sets_of_upto_n = [set()]
        
        for item in basket_:
            for current_set in sets_of_upto_n:
                if basket_.count(item) > 1:
                    if item not in current_set and len(current_set) < max_n:
                        current_set.add(item)
                        break
                    if current_set == sets_of_upto_n[-1]:
                        new_set = {item}
                        sets_of_upto_n.append(new_set)
                        break

        return sets_of_upto_n

    def alt_grouping_2(max_n, basket_): # alternative grouping: limit number of max_n groupings to 1
        sets_of_upto_n = [set()]

        for item in basket_:
            if len(sets_of_upto_n[0]) != max_n:
                for current_set in sets_of_upto_n:
                    if item not in current_set and len(current_set) < max_n:
                        current_set.add(item)
                        break
                    if current_set == sets_of_upto_n[-1]:
                        new_set = {item}
                        sets_of_upto_n.append(new_set)
                        break
            else:
                for current_set in sets_of_upto_n[1:]:
                    if item not in current_set and len(current_set) < max_n-1:
                        current_set.add(item)
                        break
                    if current_set == sets_of_upto_n[-1]:
                        new_set = {item}
                        sets_of_upto_n.append(new_set)
                        break
                        
        return sets_of_upto_n
    

    all_groupings = []

    # ascending order basket groupings
    for n in range(5):
        current_grouping = grouping(n+1, basket_sorted)
        all_groupings.append(current_grouping)

    # alt grouping (single books distributed across groupings)
    for n in range(5):
        current_alt_grouping = alt_grouping(n+1, basket_sorted)
        all_groupings.append(current_alt_grouping)

    # descending order basket groupings
    for n in range(5):
        basket_reversed = [k for k in basket_sorted[::-1]]
        current_grouping = grouping(n+1, basket_reversed)
        all_groupings.append(current_grouping)

    # alt grouping (limit number of max_n groupings to 1)
    test_groupings = []
    current_alt_grouping = alt_grouping_2(5, basket_sorted)
    all_groupings.append(current_alt_grouping)
        
    discounted_prices = [1, 0.95, 0.9, 0.8, 0.75]
    all_prices = []

    for current_grouping in all_groupings:
        prices = [len(i)*discounted_prices[len(i)-1]*800 for i in current_grouping]
        all_prices.append(sum(prices))

    return min(all_prices)
