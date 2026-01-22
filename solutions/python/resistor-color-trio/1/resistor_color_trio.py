def label(colors):
    values = {
        'black': 0,
        'brown': 1,
        'red': 2,
        'orange': 3,
        'yellow': 4,
        'green': 5,
        'blue': 6,
        'violet': 7,
        'grey': 8,
        'white': 9,
    }

    print(colors)

    resistance = int(''.join([str(values[k]) for k in colors[:2]])) * (10 ** [values[k] for k in colors[-1:]][0])
    print(resistance)

    if resistance > 999:
        resistance = str(int(resistance / 1000)) + ' kiloohms'
    else:
        resistance = str(resistance) + ' ohms'

    return resistance