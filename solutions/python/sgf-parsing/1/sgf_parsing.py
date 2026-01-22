import re

class SgfTree:
    def __init__(self, properties=None, children=None):
        self.properties = properties or {}
        self.children = children or []

    def __eq__(self, other):
        if not isinstance(other, SgfTree):
            return False
        for key, value in self.properties.items():
            if key not in other.properties:
                return False
            if other.properties[key] != value:
                return False
        for key in other.properties.keys():
            if key not in self.properties:
                return False
        if len(self.children) != len(other.children):
            return False
        for child, other_child in zip(self.children, other.children):
            if child != other_child:
                return False
        return True

    def __ne__(self, other):
        return not self == other


def parse(input_string):
    if input_string == "": raise ValueError("tree missing")
    if input_string == "()": raise ValueError("tree with no nodes")
    if input_string == ";": raise ValueError("tree missing")
    if input_string == "(;)": return SgfTree()
    if len(input_string) < 7: raise ValueError("properties without delimiter")
    if input_string.islower(): raise ValueError("property must be in uppercase")

    def split_text(text, delimiter):
        square_brackets = False
        text_formatted = text
        to_delete = []
        for i, k in enumerate(text): # remove round brackets outside property values
            if k == '[':
                square_brackets = True
            if k == ']':
                square_brackets = False
            if k in ['(',')'] and square_brackets == False:
                to_delete.append(i)
        for i in to_delete[::-1]:
            text_formatted = text_formatted[:i] + text_formatted[i+1:]
        text_formatted = text_formatted.replace("\\\n", "")
        text_formatted = text_formatted.replace('\t',' ')
        to_delete = []
        for i, k in enumerate(text_formatted):
            if all([k == '\\', text_formatted[i:i+2] != '\\\\']):
                to_delete.append(i)
                continue
        for i in to_delete[::-1]:
            text_formatted = text_formatted[:i] + text_formatted[i+1:]
        pattern = f"{delimiter}(?![^()]*\))(?![^[]*\])" # split by valid semicolons
        split_output = re.split(pattern, text_formatted)[1:]
        return split_output
        

    # split by semicolons and brackets
    input_string_split = split_text(input_string[1:-1], ';')
    if len(input_string_split) == 1:
        first_node = input_string_split
        child = None
    elif len(input_string_split) == 2:
        first_node, child = input_string_split
        first_node = [first_node]
        child = [child]
    else:
        first_node, *child = input_string_split
        first_node = [first_node]

    def parse_node(input_string_split):
        k_split = []
        # split by keys (capital letters)
        for k in input_string_split:
            k_subsplit = []
            brackets_open_count = 0
            brackets_closed_count = 0
            element_start_index = 0
            for i, char in enumerate(k):
                if i == 0:
                    continue
                if i == len(k)-1:
                    k_subsplit.append(k[element_start_index:])
                if char in ['[','(']:
                    brackets_open_count += 1
                    continue
                if char in [']',')']:
                    brackets_closed_count += 1
                    continue
                if all([char.isalpha(), char.isupper(), brackets_open_count == brackets_closed_count]):
                    k_subsplit.append(k[element_start_index:i])
                    element_start_index = i
            k_split.append(k_subsplit)    
    
        # merge properties into one list
        input_string_list = []
        for j in k_split:
            key_name = ''
            for m in j:
                properties_merged = []
                brackets_open_count = 0
                brackets_closed_count = 0
                element_start_index = 0
                child_tree = []
                for i, char in enumerate(m):
                    if i == 0:
                        continue
                    if i == len(m)-1:
                        properties_merged.append(m[element_start_index:-1])
                    if all([char == '[', brackets_open_count > 0, brackets_open_count == brackets_closed_count]):
                        properties_merged.append(m[element_start_index:i-1])
                        element_start_index = i+1
                    if char == '(' and brackets_open_count == brackets_closed_count:
                        properties_merged.append(m[element_start_index:i-1])
                        child_tree = m[i:]
                        break
                    if char in ['[', '(']:
                        brackets_open_count += 1
                        if brackets_open_count == 1:
                            element_start_index = i+1
                            key_name = m[:i]
                        continue
                    if char in [']', ')']:
                        brackets_closed_count += 1
                        continue
                node_info = [key_name, properties_merged, child_tree] if child_tree else [key_name, properties_merged]
                input_string_list.append(node_info)
        return input_string_list

    def create_parent_child_tree(first_node, child):
        properties_dict = {}
        first_node = parse_node(first_node)
        # first node
        for p in first_node:
            key = p[0]
            if key.isupper() is False:
                raise ValueError('property must be in uppercase')
            value = p[1]
            properties_dict[key] = value
    
        # child node todo: add recursive if multiple children
        if child:
            child_node_list = []
            for k in child:
                child_properties_dict = {}
                child_node = parse_node([k])
                for p in child_node:
                    key = p[0]
                    if key.isupper() is False:
                        raise ValueError('property must be in uppercase')
                    value = p[1]
                    child_properties_dict[key] = value
    
                child_node = SgfTree(child_properties_dict)
                child_node_list.append(child_node)
        else:
            child_node = None
    
        if child_node:
            output = SgfTree(properties_dict, child_node_list)
        else:
            output = SgfTree(properties_dict)
        
        return output

    output = create_parent_child_tree(first_node, child)
    return output