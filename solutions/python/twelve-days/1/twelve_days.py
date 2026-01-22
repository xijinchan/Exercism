def recite(start_verse, end_verse):

    nth = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']

    gifts = ['a Partridge in a Pear Tree.', 'two Turtle Doves', 'three French Hens', 'four Calling Birds', 'five Gold Rings', 'six Geese-a-Laying', 'seven Swans-a-Swimming', 'eight Maids-a-Milking', 'nine Ladies Dancing', 'ten Lords-a-Leaping', 'eleven Pipers Piping', 'twelve Drummers Drumming']

    def generate_lines(verse):
        first_line = lambda a : 'On the ' + a + ' day of Christmas my true love gave to me: '

        yield first_line(nth[verse - 1])

        for x in range(verse - 1, -1, -1):
            if verse == 1 and x == 0:
                yield gifts[x]
            elif verse > 1 and x == 0:
                yield 'and ' + gifts[x]
            else:
                print(x)
                yield gifts[x] + ', '

    verse_list = []

    for verse in range(start_verse, end_verse + 1):
        lines = generate_lines(verse)
        verse_list.append(''.join(lines))

    return(verse_list)