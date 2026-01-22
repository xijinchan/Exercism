def square_of_sum(number):
    sum = 0
    
    for current_number in range(1, number + 1):
        sum = sum + current_number
    
    return sum ** 2

def sum_of_squares(number):
    squares = 0
    
    for current_number in range(1, number + 1):
        squares = squares + (current_number ** 2)

    return squares

def difference_of_squares(number):
    return square_of_sum(number) - sum_of_squares(number)
