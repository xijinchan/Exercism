def gamestate(board):
    # if no. of O > no. of X, invalid
    X_count = 0
    O_count = 0
    
    for row in board:
        for c in row:
            if c == 'X': X_count += 1
            if c == 'O': O_count += 1

    if O_count > X_count: raise ValueError("Wrong turn order: O started")
    if X_count == O_count + 2: raise ValueError("Wrong turn order: X went twice")

    X_wins = False
    O_wins = False
    
    # if 3 in a row, win. Vertical X
    if (board[0][0] == board[1][0] == board[2][0] == "X" or
        board[0][1] == board[1][1] == board[2][1] == "X" or
        board[0][2] == board[1][2] == board[2][2] == "X"):
        if X_count == O_count: raise ValueError("Impossible board: game should have ended after the game was won")
        X_wins = True

    # if 3 in a row, win. Vertical O
    if (board[0][0] == board[1][0] == board[2][0] == "O" or
        board[0][1] == board[1][1] == board[2][1] == "O" or
        board[0][2] == board[1][2] == board[2][2] == "O"):
        if X_count > O_count: raise ValueError("Impossible board: game should have ended after the game was won")
        O_wins = True

    if X_wins == O_wins == True: raise ValueError("Impossible board: game should have ended after the game was won")
    if X_wins == True or O_wins == True: return 'win'

    # if 3 in a row, win. Horizontal X
    if (board[0][0] == board[0][1] == board[0][2] == "X" or
        board[1][0] == board[1][1] == board[1][2] == "X" or
        board[2][0] == board[2][1] == board[2][2] == "X"):
        if X_count == O_count: raise ValueError("Impossible board: game should have ended after the game was won")
        X_wins = True

    # if 3 in a row, win. Horizontal O
    if (board[0][0] == board[0][1] == board[0][2] == "O" or
        board[1][0] == board[1][1] == board[1][2] == "O" or
        board[2][0] == board[2][1] == board[2][2] == "O"):
        if X_count > O_count: raise ValueError("Impossible board: game should have ended after the game was won")
        O_wins = True

    if X_wins == O_wins == True: raise ValueError("Impossible board: game should have ended after the game was won")
    if X_wins == True or O_wins == True: return 'win'

    # if 3 in a row, win. Diagonal X
    if (board[0][0] == board[1][1] == board[2][2] == "X" or
        board[2][0] == board[1][1] == board[0][2] == "X"):
        if X_count == O_count: raise ValueError("Impossible board: game should have ended after the game was won")
        return 'win'

    # if 3 in a row, win. Diagonal O
    if (board[0][0] == board[1][1] == board[2][2] == "O" or
        board[2][0] == board[1][1] == board[0][2] == "O"):
        if X_count > O_count: raise ValueError("Impossible board: game should have ended after the game was won")
        return 'win'
        
    # if 5 "X"s and 4 "O"s, draw
    if X_count == 5 and O_count == 4:
        return 'draw'
    # if empty squares, ongoing
    if X_count + O_count < 9:
        return 'ongoing'
