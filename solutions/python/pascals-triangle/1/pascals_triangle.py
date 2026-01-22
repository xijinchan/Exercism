def rows(row_count):
    if row_count < 0: raise ValueError('number of rows is negative')
    if row_count == 0:
        return []
    if row_count == 1:
        return [[1]]

    previous_rows = rows(row_count - 1)

    current_row = [[1, *[sum(rows(row_count - 1)[-1][k-1:k+1]) for k in range(1, row_count - 1)], 1]]

    return previous_rows + current_row