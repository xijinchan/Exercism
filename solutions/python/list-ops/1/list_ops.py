def append(list1, list2):
    if isinstance(list2, list) == True:
        for element in list2:
            list1.append(element)
    else:
        list1.append(list2)

    return list1


def concat(lists):
    list_concat = []

    # # Flatten arbitrarily deep nested lists
    # for element in lists:
    #     if isinstance(element, list) == True:
    #         list_flattened = concat(element)
    #         list_concat = append(list_concat, list_flattened)
    #     else:
    #         list_concat = append(list_concat, element)

    for element in lists:
        if isinstance(element, list) == True:
                for sub_element in element:
                    list_concat.append(sub_element)
        else:
            list_concat = append(list_concat, element)

    return list_concat

def filter(function, list):
    output = []
    
    for element in list:
        if function(element) == True: output.append(element)

    return output


def length(list):
    count = 0
    
    for item in list:
        count += 1

    return count


def map(function, list):
    output = []
    
    for element in list:
        output.append(function(element))

    return output


def foldl(function, list, initial):
    
    if list == []: return initial
        
    output = function(list[0], initial)
    for element in range(1, len(list)):
        if element == 0: continue
        output = function(list[element], output)
        
    return output


def foldr(function, list, initial):

    if list == []: return initial
        
    output = function(list[len(list) - 1], initial)
    for element in range(len(list) - 1, -1, -1):
        if element == len(list) - 1: continue
        output = function(list[element], output)
        
    return output


def reverse(list):

    output = []
    
    for element in list:
        output.insert(0, element)

    return output
