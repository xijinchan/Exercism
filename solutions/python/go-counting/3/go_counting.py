WHITE = 'W'
BLACK = 'B'
NONE = ' '

class Board:
    """Count territories of each player in a Go game

    Args:
        board (list[str]): A two-dimensional Go board
    """

    def __init__(self, board):
        self.board = board
        self.board_padded = ['+' * (len(self.board[0])+2)] + ['+' + k + '+' for k in self.board] + ['+' * (len(self.board[0])+2)]
        print(''.join([k + '\n' for k in self.board_padded]))

    def territory(self, x, y):
        """Find the owner and the territories given a coordinate on
           the board

        Args:
            x (int): Column on the board
            y (int): Row on the board

        Returns:
            (str, set): A tuple, the first element being the owner
                        of that area.  One of "W", "B", "".  The
                        second being a set of coordinates, representing
                        the owner's territories.
        """
        if any([x < 0, x > len(self.board[0])-1, y < 0, y > len(self.board)-1]): raise ValueError('Invalid coordinate')
        if self.board[y][x] == 'B' or self.board[y][x] == 'W': return (' ',set())            

        # maze path-finder, hug-left wall
        next_coordinate_NESW = [(0,-1),(1,0),(0,1),(-1,0)]
        current_coordinate = [x+1,y+1] # padded board
        next_coordinate = [k for k in current_coordinate]
        current_direction = 0
        first_stone = None
        counter = 0
        loops = 0
        encircle = True
        territory = []

        # go to edge of the space
        def find_next():
            next_coordinate[0] = current_coordinate[0] + next_coordinate_NESW[current_direction][0]
            next_coordinate[1] = current_coordinate[1] + next_coordinate_NESW[current_direction][1]
            return self.board_padded[next_coordinate[1]][next_coordinate[0]]
        
        next_ = find_next()
        
        while next_ == ' ':
            current_coordinate = [k for k in next_coordinate]
            next_ = find_next()
        
        first_position = [k for k in current_coordinate] # first left wall hug coordinate

        def find_left(current_coordinate, current_direction):
            left_coordinate_y = current_coordinate[0] + next_coordinate_NESW[(current_direction - 1) % 4][0]
            left_coordinate_x = current_coordinate[1] + next_coordinate_NESW[(current_direction - 1) % 4][1]
            return self.board_padded[left_coordinate_x][left_coordinate_y]

        while True:
            counter += 1
            current_position_tuple = (current_coordinate[0]-1,current_coordinate[1]-1) #remove padding
            if current_position_tuple not in territory:
                territory.append(current_position_tuple)
                
            next_ = find_next()

            # if looped back to first_position (first left wall hug coordinate)
            if all([counter > 4, current_coordinate[0] == first_position[0], current_coordinate[1] == first_position[1]]):
                loops += 1
                if loops > 3: # if arrived back at first position after all 4 possible NESW paths exhausted
                    break

            # add left wall hug
            left = find_left(current_coordinate, current_direction)
            if left == ' ': # turn left
                current_direction = (current_direction - 1) % 4
                next_ = find_next()
                current_coordinate = [k for k in next_coordinate]
                continue
            if next_ == ' ':
                current_coordinate = [k for k in next_coordinate]
                continue
            if next_ == 'B' or next_ == 'W':
                if first_stone == None:
                    first_stone = next_
                elif next_ != first_stone:
                    encircle = False
                    break
            
            current_direction = (current_direction + 1) % 4

        if encircle == False:
            stone = ' '
        else:
            stone = first_stone

        return (stone, {k for k in territory})

    def territories(self):
        """Find the owners and the territories of the whole board

        Args:
            none

        Returns:
            dict(str, set): A dictionary whose key being the owner
                        , i.e. "W", "B", "".  The value being a set
                        of coordinates owned by the owner.
        """
        blanks = []
        
        for y, k in enumerate(self.board):
            for x, m in enumerate(k):
                if m == ' ': blanks.append([x,y])

        territories_dict = {}

        for n in blanks:
            a = [k for k in self.territory(n[0], n[1])]
            if a[0] == None: a[0] = ' '
            if a[0] not in territories_dict:
                territories_dict[a[0]] = a[1]
            else:
                territories_dict[a[0]].update(a[1])

        for k in ['W', 'B', ' ']:
            if k not in territories_dict: territories_dict[k] = set()

        return territories_dict
            