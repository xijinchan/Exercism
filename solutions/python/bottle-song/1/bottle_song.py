def recite(start, take=1):
    numbers_words = {
        10: 'Ten',
        9: 'Nine',
        8: 'Eight',
        7: 'Seven',
        6: 'Six',
        5: 'Five',
        4: 'Four',
        3: 'Three',
        2: 'Two',
        1: 'One',
        0: 'No'
    }

    text = []
    bottle_text = 'bottles'
    bottles_count = start

    for verse in range(take):
        a = f'{numbers_words[bottles_count]} green {bottle_text[:-1] if bottles_count == 1 else bottle_text} hanging on the wall,'
        c = 'And if one green bottle should accidentally fall,'
        d = f'There\'ll be {numbers_words[bottles_count-1].lower()} green {bottle_text[:-1] if bottles_count-1 == 1 else bottle_text} hanging on the wall.'
        text += [a,a,c,d]
        if verse < take-1: text += [""]
        bottles_count -= 1

    return text