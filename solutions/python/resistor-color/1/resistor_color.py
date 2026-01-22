color_list = ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]

def color_code(color):
    if color in color_list:
        return color_list.index(color)

def colors():
    return color_list
