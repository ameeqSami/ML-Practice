# def sum(a, b):
#     return a+b

def avg(a, b):
    return (a+b)/2

def is_armstrong(number):
    # Convert number to string to easily iterate and find length
    str_num = str(number)
    num_digits = len(str_num)
    
    # Calculate the sum of digits raised to the power of num_digits
    total_sum = sum(int(digit) ** num_digits for digit in str_num)
    
    # Return True if the sum equals the original number
    if total_sum == number:
        return 'true'
    else: 
        return 'false' 

