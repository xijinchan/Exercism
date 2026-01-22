def translate(text):

    def pigify_word(text):
        output = ""
        
        if text[0] in ["a","e","i","o","u"] or text[0:2] == "xr" or text[0:2] == "yt":
            output = text + "ay"
        else:
            consonant_start = ""
            
            if text[1:3] == "qu":
                output = text[3:] + text[0:3] + "ay"
            elif text[0:2] == "qu":
                output = text[2:] + text[0:2] + "ay"
            else:
                for character in range(0,len(text)):
                    if text[character] not in ["a","e","i","o","u","y"]:
                        consonant_start = consonant_start + text[character]
                    else:
                        if character != 1 and text[character - 1] == "y":
                            print("text[character - 1] == y")
                            output = text[character - 1:] + consonant_start[:-1] + "ay"
                            break
                        else:
                            if text[0] == "y":
                                output_start = text[1:] + "y"
                            else:
                                output_start = text[character:]
                            output = output_start + consonant_start + "ay"
                            break
    
        return output

    text_wordlist = text.split(' ')
    text_translated = ""
    
    for word in text_wordlist:
        if word != text_wordlist[-1]:
            text_translated = text_translated + pigify_word(word) + " "
        else:
            text_translated = text_translated + pigify_word(word)

    return text_translated

