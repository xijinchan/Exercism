def reverse(text):
    reversed_text = ""

    for character in text:
        reversed_text = character + reversed_text

    return reversed_text