def recite(start_verse, end_verse):
    animals = ['fly','spider','bird','cat','dog','goat','cow','horse']
    second_lines = ['I don\'t know why she swallowed the fly. Perhaps she\'ll die.',
                'It wriggled and jiggled and tickled inside her.',
                'How absurd to swallow a bird!',
                'Imagine that, to swallow a cat!',
                'What a hog, to swallow a dog!',
                'Just opened her throat and swallowed a goat!',
                'I don\'t know how she swallowed a cow!',
                'She\'s dead, of course!'
                ]

    def middle_lines(animal, animal_index):
        if animal == 'spider':
            output.append(f'She swallowed the {animals[animal_index+1]} to catch the {animal} that wriggled and jiggled and tickled inside her.')
        else:
            output.append(f'She swallowed the {animals[animal_index+1]} to catch the {animal}.')

    output = []

    for verse in range(start_verse, end_verse + 1):
        for animal_index in range(verse-1,-1,-1):
            animal = animals[animal_index]
            if animal_index == 7:
                output.append(f'I know an old lady who swallowed a {animal}.')
                output.append(second_lines[7])
                break
            if animal_index == verse-1:
                output.append(f'I know an old lady who swallowed a {animal}.')
            elif animal_index == verse-2:
                output.append(second_lines[animal_index+1])
                middle_lines(animal, animal_index)
            else:
                middle_lines(animal, animal_index)
            
            if animal_index == 0: output.append(second_lines[0])
        if start_verse != end_verse and verse != end_verse: output.append('')

    return output
