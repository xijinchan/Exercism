class Point:
    def __init__(self, x, y):
        self.x = None
        self.y = None

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class WordSearch:
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def search(self, word):        
        def search_right(start):
            if self.puzzle[start[0]][start[1]:start[1]+len(word)] == word:
                return (Point(start[0], start[1]), Point(start[0], len(word)-1))

        def search_left(start):
            if self.puzzle[start[0]][start[1]+1-len(word):start[1]+1] == word[::-1]:
                return (Point(start[0], start[1]-len(word)-1), Point(start[0], start[1]))

        def search_down(start):
            if ''.join([self.puzzle[k+start[0]][start[1]] for k in range(len(word))]) == word:
                return (Point(start[0], start[1]), Point(start[0]+len(word)-1, start[1]))

        def search_up(start):
            if ''.join([self.puzzle[k-start[0]-1][start[1]] for k in range(len(self.puzzle)-1,len(word)+1,-1)]) == word:
                return (Point(start[0], start[1]), Point(start[0]-len(word), start[1]))

        def search_diagonal_SE(start):
            if ''.join([self.puzzle[start[0]+k][start[1]+k] for k in range(len(word))]) == word:
                return (Point(start[0], start[1]), Point(start[0]+len(word), start[1]+len(word)))

        def search_diagonal_NW(start):
            if ''.join([self.puzzle[start[0]-k][start[1]-k] for k in range(len(word))]) == word:
                return (Point(start[0], start[1]), Point(start[0]-len(word), start[1]-len(word)))

        def search_diagonal_NE(start):
            if ''.join([self.puzzle[start[0]-k][start[1]+k] for k in range(len(word))]) == word:
                return (Point(start[0], start[1]), Point(start[0]-len(word), start[1]+len(word)))

        def search_diagonal_SW(start):
            if ''.join([self.puzzle[start[0]+k][start[1]-k] for k in range(len(word))]) == word:
                return (Point(start[0], start[1]), Point(start[0]+len(word), start[1]-len(word)))

        # search_right() within bounds
        for i, row in enumerate(self.puzzle):
            for k in range(len(row)-len(word)+1):
                if row[k:k+len(word)] == word:
                    return search_right((i,k))

        # search_left() within bounds
        for i, row in enumerate(self.puzzle):
            for k in range(len(word)-1, len(row)):
                output = search_left((i, k))
                if output: return output

        # search_down() within bounds
        for i, row in enumerate(self.puzzle):
            if i <= len(self.puzzle) - len(word):
                for k in range(len(row)):
                    output = search_down((i, k))
                    if output: return output

        # search_up() within bounds
        for i, row in enumerate(self.puzzle):
            if i >= len(word)-1:
                for k in range(len(row)):
                    output = search_up((i, k))
                    if output: return output

        # search_diagonal_SE() within bounds
        for row in range(len(self.puzzle)-len(word)+1):
            for k in range(len(self.puzzle[row])-len(word)+1):
                output = search_diagonal_SE((row,k))
                if output: return output

        # search_diagonal_NW() within bounds
        for row in range(len(self.puzzle)-1, len(word)-2, -1):
            for k in range(len(self.puzzle[row])-1, len(word)-2, -1):
                output = search_diagonal_NW((row,k))
                if output: return output

        # search_diagonal_NE() within bounds
        for row in range(len(self.puzzle)-1, len(word)-2, -1):
            for k in range(len(self.puzzle[row])-len(word)):
                output = search_diagonal_NE((row,k))
                if output: return output

        # search_diagonal_SW() within bounds
        for row in range(len(self.puzzle)-len(word)+1):
            for k in range(len(self.puzzle[row])-1, len(word)-2, -1):
                output = search_diagonal_SW((row,k))
                if output: return output