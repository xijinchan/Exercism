class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix_string_split = self.matrix_string.split('\n')
        matrix_row = matrix_string_split[index - 1].split(' ')
        matrix_row = [int(k) for k in matrix_row]
        return matrix_row

    def column(self, index):
        matrix_string_split = self.matrix_string.split('\n')
        matrix_formatted = [k.split(' ') for k in matrix_string_split]
        matrix_column = [int(k[index - 1]) for k in matrix_formatted]
        return matrix_column