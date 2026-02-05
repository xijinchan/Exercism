def tick(matrix):
    
    N = 0
    NE = 0
    E = 0
    SE = 0
    S = 0
    SW = 0
    W = 0
    NW = 0

    output = [row[:] for row in matrix]
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            # W, NW, N, NE, E
            if i == 0:
                N = NE = NW = 0
                if j == 0:
                    W = 0
                else:
                    W = matrix[i][j-1]
                if j == len(matrix[0]) - 1:
                    E = 0
                else:
                    E = matrix[i][j+1]
            else:
                N = matrix[i-1][j]
                if j == 0:
                    NW = 0
                    W = 0
                else:
                    NW = matrix[i-1][j-1]
                    W = matrix[i][j-1]
                if j == len(matrix[0]) - 1:
                    NE = 0
                    E = 0
                else:
                    NE = matrix[i-1][j+1]
                    E = matrix[i][j+1]

            # SW, S, SE
            if i == len(matrix) - 1:
                SE = S = SW = 0
            else:
                S = matrix[i+1][j]
                if j == 0:
                    SW = 0
                else:
                    SW = matrix[i+1][j-1]
                if j == len(matrix[0]) - 1:
                    SE = 0
                else:
                    SE = matrix[i+1][j+1]


            cell = matrix[i][j]
            neighbours = N + NE + E + SE + S + SW + W + NW
                
            if cell == 0 and neighbours == 3:
                output[i][j] = 1
            elif cell == 1 and neighbours == 2 or cell == 1 and neighbours == 3:
                continue
            else:
                output[i][j] = 0  

    return output
