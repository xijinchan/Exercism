# Globals for the directions
# Change the values as you see fit
EAST = (1,0)
NORTH = (0,1)
WEST = (-1,0)
SOUTH = (0,-1)

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos, y_pos)

    def move(self, string):
        orientation_NESW = [(0,1),(1,0),(0,-1),(-1,0)]
        RL_translation = {'L': -1, 'R':1}
        current_orientation_index = orientation_NESW.index(self.direction)
        displacement = (0,0)
        
        for k in string:
            if any([k == 'R', k == 'L']):
                current_orientation_index = (current_orientation_index + RL_translation[k]) % 4
            if k == 'A': displacement = tuple(map(sum, zip(displacement, orientation_NESW[current_orientation_index])))

        end_coordinates = tuple(map(sum, zip(self.coordinates, displacement)))
        
        self.coordinates = end_coordinates
        self.direction = orientation_NESW[current_orientation_index]