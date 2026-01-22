def flatten(iterable):
    flattened = []
    for item in iterable:
        if isinstance(item, list):
            flattened.extend(flatten(item))
        elif item != None:
            flattened.append(item)
    return flattened
