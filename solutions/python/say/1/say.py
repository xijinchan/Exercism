def say(number):
    digits_words = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    tens_words = ['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    columns_words = ['','thousand','million','billion']

    if number == 0: return 'zero'
    if 0 > number or number > 999999999999: raise ValueError('input out of range')

    number_reversed = str(number)[::-1]
    number_split = [str(number_reversed)[i:i+3][::-1] for i in range(0, len(str(number_reversed)), 3)]
    
    def three_digit_fragment(number):
        output = ''
        last_2_digits = int(str(number)[-2:])
    
        if 0 < last_2_digits < 20:
            output = digits_words[last_2_digits - 1]
        elif last_2_digits > 19:
            output = tens_words[int(str(number)[-2:-1])-1]
            if int(str(number)[-1]) != 0: output = output + '-' + digits_words[int(str(number)[-1:])-1]
        if number > 99:
            output = digits_words[int(str(number)[-3:-2])-1] + ' hundred ' + output
            
        return output.strip()

    output = ''

    for fragment in number_split:
        output = three_digit_fragment(int(fragment)) + ' ' + columns_words[number_split.index(fragment)] + ' ' + output

    return output.strip()