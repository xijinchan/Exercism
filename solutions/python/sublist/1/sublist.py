SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif list_two in [list_one[i:i+len(list_two)] for i in range(len(list_one)-len(list_two)+1)] or list_two == []:
        return SUPERLIST
    elif list_one in [list_two[i:i+len(list_one)] for i in range(len(list_two)-len(list_one)+1)] or list_one == []:
        return SUBLIST
    else:
        return UNEQUAL
