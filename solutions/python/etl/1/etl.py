def transform(legacy_data):
    new_data = {}
    
    for entry in legacy_data:
        for letter in legacy_data[int(entry)]:
            new_data[letter.lower()] = entry

    print(new_data)
    return new_data