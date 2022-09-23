# Complete the square sum function so that it 
# squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

import math

def square_sum(numbers):
    #your code here
    
    sum = 0
    for i in numbers:
        sum = sum + math.pow(i, 2)
        
    return sum
