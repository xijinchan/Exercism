def grep(pattern, flags, files):
    output = []

    for file in files:
        f = open(file)
        f_split = (file, f.read().split('\n')) # (filename, lines.split)

        if '-l' in flags: # 'filename'
            if len([k for k in f_split[1] if pattern in k]) > 0: output.append(f_split[0] + '\n')
            continue
        elif '-i' in flags: # case-insensitive
            results = [(i + 1, k) for i, k in enumerate(f_split[1]) if pattern.lower() in k.lower()]
        elif '-x' in flags: # match entire lines
            results = [(i + 1, k) for i, k in enumerate(f_split[1]) if k == pattern]
        else:
            results = [(i + 1, k) for i, k in enumerate(f_split[1]) if pattern in k] #[(linenumber, line)]
    
        if '-v' in flags: # invert
            if results == []:
                results = [(i + 1, k) for i, k in enumerate(f_split[1]) if k!= '']
            else:
                results = [(i + 1, k) for i, k in enumerate(f_split[1]) if (i + 1, k) not in results and k != '']
        if results == []: continue
        if '-n' in flags: # line number
            results = [('',str(k[0]) + ':' + k[1]) for k in results]
            
        if len(files) > 1: # multiple files: add filename
            results = [(k[0],file + ':' + k[1]) for k in results]

        results_formatted = '\n'.join([k[1] for k in results]) + '\n'
        output.append(results_formatted)

    if output != []:
        if output[-1] == '\n': output = output[:-1]

    return ''.join(output)