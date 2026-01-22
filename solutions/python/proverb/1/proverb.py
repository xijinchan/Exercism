def proverb(*input_data, qualifier):
    if input_data is (): return []
    text = []

    a, *_ = input_data
    q = ' ' + qualifier if qualifier != None else ''
    text = [f'For want of a {input_data[k]} the {input_data[k+1]} was lost.' for k in range(len(input_data[:-1]))] + [f'And all for the want of a{q} {a}.']

    return text