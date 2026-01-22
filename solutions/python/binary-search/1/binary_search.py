def find(search_list, value):
    search_list.sort()
    search_finished = False
    loop_check = 0
    prior_index = 0
    
    search_index = int(len(search_list) / 2)
    search_width = int(len(search_list) / 2)

    if len(search_list) == 0:
        raise ValueError("value not in array")

    while search_finished == False:

        if search_list[search_index] == value:
            return search_index
        elif search_list[search_index] > value:
            search_width = search_width / 2
            if search_width < 1:
                search_width = 1
                if loop_check - prior_index == search_index:
                    raise ValueError("value not in array")
                loop_check = prior_index + search_index
                prior_index = search_index
            search_index = search_index - search_width
        elif search_list[search_index] < value:
            search_width = search_width / 2
            if search_width < 1:
                search_width = 1
                if loop_check - prior_index == search_index:
                    raise ValueError("value not in array")
                loop_check = prior_index + search_index
                prior_index = search_index
            search_index = search_index + search_width
            
        if search_index < 0 or search_index > (len(search_list) - 1):
            raise ValueError("value not in array")

        search_index = int(search_index)