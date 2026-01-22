import math

def rebase(input_base, digits, output_base):
    if input_base < 2: raise ValueError('input base must be >= 2')
    if output_base < 2: raise ValueError('output base must be >= 2')
    if any([k for k in digits if k < 0 or k >= input_base]): raise ValueError("all digits must satisfy 0 <= d < input base")
    if sum(digits) == 0: return [0]
        
    total = sum([(k * (input_base ** (len(digits)-1-i))) for i, k in enumerate(digits)])
    highest_power = int(math.log(total,output_base))

    output = []
    subtotal = total
    
    for k in range(highest_power,-1,-1):
        digit = int(subtotal / (output_base ** k))
        output.append(digit)
        subtotal = subtotal - (digit * (output_base ** k))

    return output