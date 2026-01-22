def count_words(sentence):    
    sentence_formatted = ''
    
    for character in sentence:
        if character.isalpha() is True or character.isnumeric() is True or character == ' ' or character == "'":
            if character == '"':
                continue
            else:
                sentence_formatted += character.lower()
        elif character == ',' or character == '\t' or character == '_':
            sentence_formatted += ' '
    
    sentence_formatted = " ".join(sentence_formatted.split())
    sentence_formatted = sentence_formatted.strip("'")
    sentence_split = sentence_formatted.split(" ")

    word_dict = dict.fromkeys(sentence_split)

    for word in sentence_split:
            if word != word.strip("'"):
                sentence_split[sentence_split.index(word)] = word.strip("'")
                old_key = word
                new_key = word.strip("'")
                del word_dict[old_key]
                count = sentence_split.count(old_key) + sentence_split.count(new_key)
                word_dict[new_key] = count
            else:
                count = sentence_split.count(word)
                word_dict[word] = count
    
    return word_dict