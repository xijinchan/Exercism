def saddle_points(matrix):
        if len([k for i, k in enumerate(matrix[:-1]) if len(k) != len(matrix[i+1])]) > 0: raise ValueError("irregular matrix")

        row_max_indices = [(int(n), int(i)) for n, k in enumerate(matrix) for i in range(len(k)) if k[i] == max(k)]
    
        saddles = [{'row': k[0]+1, 'column': k[1]+1} for k in row_max_indices if matrix[k[0]][k[1]] == min([matrix[j][k[1]] for j in range(len(matrix))])]
        return saddles