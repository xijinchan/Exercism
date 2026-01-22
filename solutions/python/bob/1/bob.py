import re

def response(hey_bob):
    
    if hey_bob == "" or hey_bob.isspace() is True:
        bob_response = "Fine. Be that way!"
    elif hey_bob == hey_bob.upper() and hey_bob[-1] == "?":
        if re.search('[a-zA-Z]', hey_bob) == None:
            bob_response = "Sure."
        else:
            bob_response = "Calm down, I know what I'm doing!"
    elif hey_bob == hey_bob.upper() and hey_bob[-1] != "?":
        if re.search('[a-zA-Z]', hey_bob) == None:
            bob_response = "Whatever."
        else:
            bob_response = "Whoa, chill out!"
    elif hey_bob[-1] == "?":
        bob_response = "Sure."
    elif "bob" in hey_bob:
        bob_response = "Fine. Be that way!"
    elif hey_bob.endswith(' ') == True:
        if re.search('[?]', hey_bob) != None:
            bob_response = "Sure."
        else:
            bob_response = "Whatever."
    else:
        bob_response = "Whatever."

    return bob_response
