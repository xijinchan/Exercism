
class ConnectGame:
    def __init__(self, board):
        self.board = board.replace(' ', '').split('\n')
        self.board.reverse()
        # pad board edges
        self.board = ['.' * (len(self.board[0]) + 2)] + ['.' + k + '.' for k in self.board] + ['.' * (len(self.board[0]) + 2)]

    def get_winner(self):
        if 'O' not in self.board[-2] and 'X' not in [k[-2] for k in self.board]: return ''
        if all([len(self.board[0]) == 3, self.board[1][1] == 'O']): return 'O'
        if all([len(self.board[0]) == 3, self.board[1][1] == 'X']): return 'X'

        board_transposed = [''.join(list(a)) for a in zip(*self.board)]

        def trace_path(board, piece):
            end_positions = [(i, 1) for i, k in enumerate(board[1]) if k == piece]

            # directions = [up, left, down-left, down, right, up-right]
            direction = [(0,1), (-1,0), (-1,-1), (0,-1), (1,0), (1,1)]
            
            # left wall hug
            def left_wall_check(position, current_direction, piece):
                left = direction[(direction.index(current_direction) + 1) % 6]
                left_coordinate = [sum(x) for x in zip(position, left)]
                return board[left_coordinate[1]][left_coordinate[0]]

            current_direction = direction[0]
            current_position = None

            # starting from end
            for end_position in end_positions:
                end = False
                output = ''
                current_position = end_position
                turn_count = 0
                
                while end == False:
                    new_position = tuple(sum(x) for x in zip(current_position, current_direction))
                                       
                    if all([left_wall_check(current_position, current_direction, piece) != piece, board[new_position[1]][new_position[0]] == piece]):
                        current_position = new_position
                        if current_position == end_position: end = True
                        if current_position[1] == len(board) - 2:
                            end = True
                            output = True
                    elif left_wall_check(current_position, current_direction, piece) == piece:
                        current_direction = direction[(direction.index(current_direction) + 1) % 6]
                    else:
                        current_direction = direction[(direction.index(current_direction) - 1) % 6]
                        turn_count += 1
                        if turn_count == 7: # stop endless turns
                            end = True
                if end == True: break
                    
            return output
       
        if trace_path(self.board, 'O') == True: return 'O'
        if trace_path(board_transposed, 'X') == True: return 'X'
        return ''
