def answer(question):
    answer = None

    # parse question into math notation
    question = question.replace("What is ", "")
    question = question.replace("What is","")
    question = question.replace("?", "")

    if "plus" in question:
        question = question.replace("plus", "+")
    if "minus" in question:
        question = question.replace("minus", "-")
    if "multiplied by" in question:
        question = question.replace("multiplied by", "*")
    if "divided by" in question:
        question = question.replace("divided by", "/")

    question_split = question.split(" ")
    print("question_split = ", question_split)
    
    # Errors
    if any(character.isalpha() for character in question) is True:
        raise ValueError("unknown operation")
    if "+ +" in question:
        raise ValueError("syntax error")
    if question_split[0] == "+":
        raise ValueError("syntax error")

    error = False
    for i in range(0,len(question_split)):
        try:
            if isinstance(int(question_split[i]), int) is True and isinstance(int(question_split[i + 1]), int) is True:
                error = True
                break
        except:
            continue
    if error is True:
            raise ValueError("syntax error")

    # Evaluate parsed math problem
    question_split_recombined = ""

    try:        
        no_of_numbers = 0

        for i in range(0,len(question_split)):

            if no_of_numbers > 0 and no_of_numbers % 2 == 0:
                question_split_recombined = str(eval(question_split_recombined))
                no_of_numbers = 1

            question_split_recombined = question_split_recombined + str(question_split[i])
            print("question_split_recombined = ", question_split_recombined)

            try:
                if isinstance(int(question_split[i]), int) is True: no_of_numbers += 1
            except:
                continue

        answer = eval(question_split_recombined)
        return answer

    except:
        raise ValueError("syntax error")