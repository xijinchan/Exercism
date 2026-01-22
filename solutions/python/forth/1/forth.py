import math

class StackUnderflowError(Exception):
    """Exception raised when Stack is not full.
       message: explanation of the error.
    """
    def __init__(self, message):
        self.message = message


def evaluate(input_data):
    operators = ['+','-','*','/']
    defined_words = ['dup', 'drop','swap','over']
    output = []
    data_split = []
    built_ins = {}

    for data in input_data:
        data_split = [k for k in data.split()]
        data_split = [int(k) if k.isdigit() == True else (int(k) if len(k) > 1 and k[0] == '-' else k) for k in data_split]
        data_split = [k.lower() if isinstance(k, str) else k for k in data_split]

        if data_split[0] == ':' and data_split[-1] == ';': # create user defined words
            if isinstance(data_split[1], int): raise ValueError('illegal operation')
            if type(data_split[2:-1]) is list:
                for i, k in enumerate(data_split[2:-1]):
                    if k in built_ins:
                        built_ins.update({data_split[1]:built_ins[k]})
                        data_split[2+i] = built_ins[k][0]
                    else:
                        built_ins.update({data_split[1]:data_split[2:-1]})
            else:
                built_ins.update({data_split[1]:data_split[2:-1]})
            continue
        
        data_split_copy = data_split[:]

        def built_ins_parse(list_a): # parse user defined words
            for i in range(len(list_a)):
                if list_a[i] in built_ins:
                    if type(built_ins[list_a[i]]) is list:
                        key = list_a[i]
                        n = len(built_ins[list_a[i]])
                        for j in range(n-1,-1,-1):
                            list_a.insert(i,built_ins[key][j])
                        list_a.pop(i+n)
            return list_a

        data_split_copy = built_ins_parse(data_split_copy)

        data_split = [k for k in data_split_copy]
                
        if len(data_split) < 3 and data_split[-1] in operators:
            raise StackUnderflowError('Insufficient number of items in stack')    
        if len(data_split) < 2 and data_split[-1] in ['dup','drop']:
            raise StackUnderflowError('Insufficient number of items in stack')
        if len(data_split) < 3 and data_split[-1] in ['swap','over']:
            raise StackUnderflowError('Insufficient number of items in stack')


        split_indices = [0]+[i+1 for i, k in enumerate(data_split) if k in operators or k in defined_words] # split list according to operations / words
        if split_indices == [0]:
            if all([isinstance(data_split[0], str), data_split[0] not in defined_words, data_split[0] not in built_ins]): raise ValueError('undefined operation')
            output = data_split
            continue

        data_split = [data_split[split_indices[i]:split_indices[i+1]] for i in range(len(split_indices[:-1]))]

        for operation in data_split:
            if operation[-1] == '+':
                output = [sum(output + operation[:-1])]
            if operation[-1] == '-':
                output = [sum(output + [k if len(operation) > 2 and i == 0 else -k for i, k in enumerate(operation[:-1])])]
            if operation[-1] == '*':
                if output == []: output = [1]
                output = [output[0] * math.prod(operation[:-1])]
            if operation[-1] == '/':
                if operation[-2] == 0: raise ZeroDivisionError('divide by zero')
                if output == []:
                    output = [operation[0] / operation[1]]
                else:
                    output = [output[0] / operation[0]]
            if operation[-1] == 'dup':
                if len(operation) == 1 and len(output) > 0:
                    output.append(output[-1])
                else:
                    output += operation[:-1] + [operation[-2]]
            if operation[-1] == 'drop':
                if len(operation) == 1 and len(output) > 0:
                    output = output[:-1]
                else:
                    output += operation[:-2]
            if operation[-1] == 'swap':
                if len(operation) > 3:
                    output += operation[:-3] + [operation[-2]] + [operation[-3]]
                elif len(operation) == 2:
                    output.insert(-1, operation[0])
                else:
                    output += [operation[-2]] + [operation[-3]]
            if operation[-1] == 'over':
                if len(operation) == 1 and len(output) > 0:
                    output.append(output[-2])
                else:
                    output += operation[:-1] + [operation[-3]]

        output = [int(k) for k in output]
    
    return output