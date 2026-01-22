'''Returns "One for name, one for me", with "you" substituted for blank name values'''

def two_fer(name=None):
    if name is None:
        output = "One for you, one for me."
    else:
        output = "One for " + name + ", one for me."

    return output
