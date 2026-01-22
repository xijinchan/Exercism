"""Functions to help edit essay homework using string manipulation."""


def capitalize_title(title):
    """Convert the first letter of each word in the title to uppercase if needed.

    :param title: str - title string that needs title casing.
    :return: str - title string in title case (first letters capitalized).
    """
    words = title.split()
    print(words)

    output = ''
    for each_word in words:
        if each_word == words[0]:
            output += each_word.capitalize()
        else:
            output += ' ' + each_word.capitalize()

    return output


def check_sentence_ending(sentence):
    """Check the ending of the sentence to verify that a period is present.

    :param sentence: str - a sentence to check.
    :return: bool - return True if punctuated correctly with period, False otherwise.
    """
    return bool(sentence[-1] == '.')


def clean_up_spacing(sentence):
    """Verify that there isn't any whitespace at the start and end of the sentence.

    :param sentence: str - a sentence to clean of leading and trailing space characters.
    :return: str - a sentence that has been cleaned of leading and trailing space characters.
    """
    while sentence[0] == ' ':
        sentence = sentence[1:]

    while sentence[-1] == ' ':
        sentence = sentence[:-1]

    return sentence


def replace_word_choice(sentence, old_word, new_word):
    """Replace a word in the provided sentence with a new one.

    :param sentence: str - a sentence to replace words in.
    :param old_word: str - word to replace.
    :param new_word: str - replacement word.
    :return: str - input sentence with new words in place of old words.
    """
    period = False
    if check_sentence_ending(sentence) is True:
        period = True
        sentence = sentence[:-1]

    words = sentence.split()

    for counter, each_word in enumerate(words):
        if each_word == old_word:
            words[counter] = new_word

    output = ' '.join([str(item) for item in words])

    if period is True:
        output += '.'

    print(output)
    return output


