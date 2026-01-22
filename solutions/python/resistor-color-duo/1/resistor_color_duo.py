'''Returns band color value for first 2 colors passed as argument'''

color_encodings = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def value(colors):
    encoding = ""
    count = 0

    for color in colors:
        count += 1
        if count == 3:
            break
        encoding = encoding + str(color_encodings.index(color))

    return int(encoding)
    
