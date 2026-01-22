def recite(start, take=1):
    output = []
    no_of_bottles = start

    phrase_1 = [' bottle of beer on the wall', ' bottles of beer on the wall',]
    phrase_2 = ['Go to the store and buy some more, ', 'Take it down and pass it around, ', 'Take one down and pass it around, ']

    for k in range(take):
        if no_of_bottles > 1:
            output.extend([str(no_of_bottles) + phrase_1[1] + ', ' + str(no_of_bottles) + phrase_1[1][:16] + '.', phrase_2[2]])
        elif no_of_bottles == 1:
            output.extend([str(no_of_bottles) + phrase_1[0] + ', ' + str(no_of_bottles) + phrase_1[0][:15] + '.', phrase_2[1]])
        else:
            output.extend(['No more' + phrase_1[1] + ', ' + 'no more' + phrase_1[1][:16] + '.', phrase_2[0] + '99' + phrase_1[1] + '.'])
            break

        no_of_bottles -= 1

        if no_of_bottles > 1:
            output[-1] += str(no_of_bottles) + phrase_1[1] + '.'
        elif no_of_bottles ==1:
            output[-1] += str(no_of_bottles) + phrase_1[0] + '.'
        else:
            output[-1] += 'no more' + phrase_1[1] + '.'

        if take > 1 and k != take-1: output.append('')

    return output