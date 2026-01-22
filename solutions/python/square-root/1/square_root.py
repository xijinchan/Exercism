def square_root(number):
    count = 1
    odd_number = 1
    
    def subtract_odds(remainder, odd_number, count):
        remainder = remainder - odd_number
        
        if remainder == 0:
            return count
        else:
            odd_number += 2
            count += 1
            return subtract_odds(remainder, odd_number, count)

    return subtract_odds(number, odd_number, count)
