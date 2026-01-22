def two_fer(name=None):
    if name is None:
        output = "One for you, one for me."
    else:
        output = "One for " + name + ", one for me."

    return output
