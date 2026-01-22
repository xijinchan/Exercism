def largest_product(series, size):
    if size > len(series): raise ValueError('span must be smaller than string length')
    if any([series == '', size == 0]): return 1
    if any([k.isalpha() for k in series]): raise ValueError('digits input must only contain digits')
    if size < 0: raise ValueError('span must not be negative')

    digits = [series[k:k+size] for k in range(len(series)-size+1)]

    def product(list):
        total = list[0]
        for k in list[1:]:
            total = total * k
        return total
    
    max_product = max([product([int(m) for m in k]) for k in digits])

    return max_product