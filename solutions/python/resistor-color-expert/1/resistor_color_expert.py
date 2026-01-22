def resistor_label(colors):
    if colors == ['black']: return '0 ohms'

    color_bands = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    tolerance = {
        'grey' : '0.05',
        'violet' : '0.1',
        'blue' : '0.25',
        'green' : '0.5',
        'brown' : '1',
        'red' : '2',
        'gold' : '5',
        'silver' : '10'
    }

    values = [str(color_bands.index(k)) for k in colors]
    tolerance_value = values[-1]

    multiplier = values[-2]
    zeros = ['0'] * int(multiplier)
    
    resistance = ''.join([k for k in values[0:-2]]) + ''.join(zeros)

    if len(resistance) > 7:
        sig_figs = resistance[0:2] + '.' + ''.join([k for k in resistance[2:] if k is not '0'])
        resistance = sig_figs + ' megaohms'
    elif len(resistance) > 6:
        sig_figs = resistance[0] + '.' + ''.join([k for k in resistance[1:] if k is not '0'])
        resistance = sig_figs + ' megaohms'
    elif len(resistance) > 4:
        sig_figs = resistance[0:2] + '.' + ''.join([k for k in resistance[2:] if k is not '0'])
        if sig_figs[-1] == '.': sig_figs = sig_figs[:-1]
        resistance = sig_figs + ' kiloohms'
    elif len(resistance) > 3:
        sig_figs = resistance[0] + '.' + ''.join([k for k in resistance[1:] if k is not '0'])
        if sig_figs[-1] == '.': sig_figs = sig_figs[:-1]
        resistance = sig_figs + ' kiloohms'
    else:
        resistance += ' ohms'

    result = resistance + ' ±' + tolerance[colors[-1]] + '%'

    return result