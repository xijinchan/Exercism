def find_fewest_coins(coins, target):
    output = []
    if target == 0: return []
    if target < 0: raise ValueError("target can't be negative")
    if min(coins) > target: raise ValueError("can't make target with given coins")

    def find_change(coins, target): # add large to small coins to make up target
        subtotal = target
        change = []
        previous_subtotal = None

        while subtotal >= 0:
            for k in reversed(coins):
                if k <= subtotal:
                    if subtotal - k != 0 and subtotal - k < min(coins): continue
                    change.append(k)
                    previous_subtotal = subtotal
                    subtotal -= k
                    break
            if previous_subtotal == subtotal: break
            previous_subtotal = subtotal

        if sum(change) != target: return []
        return change

    for k in range(len(coins),0,-1): # for combinations of coins upto each coin
        change = find_change(coins[:k], target)
        change.sort()
        if output == []: output = change # first found change
        if change != [] and len(change) < len(output): output = change # if fewer coins change found

    if output == [] and target != 0: # 2nd pass if none found, cycle through smallest change combinations
        for k in range(0,int(target/min(coins))+1): # for all multiples of smallest coin under target
            for m in range(len(coins),1,-1): # for combinations of coins above smallest coin
                change = [min(coins)] * k
                target_two = target - sum(change)
                change += find_change(coins[1:m], target_two)
                if sum(change) != target: continue
                if output == []: output = change # first found change
                if change != [] and len(change) < len(output): output = change # if fewer coins change found

    if sum(output) != target: raise ValueError("can't make target with given coins")

    return output
