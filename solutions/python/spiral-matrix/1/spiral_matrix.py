def spiral_matrix(size):
    
    map = [[None for k in range(size)] for m in range(size)]
    direction = 0
    x, y = 0, 0

    def new_coordinates(y, x, direction):        
        def path_check(y, x):
            if direction == 0 and x + 1 < size: new_x, new_y = x + 1, y # right
            if direction == 1 and y + 1 < size: new_x, new_y = x, y + 1 # down
            if direction == 2 and x - 1 > -1: new_x, new_y = x - 1, y # left
            if direction == 3 and y - 1 > -1: new_x, new_y = x, y - 1 # up
            try:
                return new_y, new_x
            except:
                return y, x

        new_y, new_x = path_check(y, x)

        try:
            if map[new_y][new_x] == None:
                x, y = new_x, new_y
                return y, x, direction
        except:
            pass
        
        direction = (direction + 1) % 4
        y, x = path_check(y, x)

        return y, x, direction

    for k in range(size ** 2):
        map[y][x] = k + 1
        y, x, direction = new_coordinates(y, x, direction)

    return map    
    