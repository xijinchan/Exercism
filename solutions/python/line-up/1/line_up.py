def line_up(name, number):
    suffix = ""

    if str(number)[-2:] == "11" or str(number)[-2:] == "12" or str(number)[-2:] == "13":
        suffix = "th"
    elif str(number)[-1] == "1":
        suffix = "st"
    elif str(number)[-1] == "2":
        suffix = "nd"
    elif str(number)[-1] == "3":
        suffix = "rd"
    else:
        suffix = "th"

    output = name + ", you are the " + str(number) + suffix + " customer we serve today. Thank you!"

    return output
