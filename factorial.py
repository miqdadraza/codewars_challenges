'''
In mathematics, the factorial of a non-negative integer n, denoted by n!, is the product of all positive integers less than or equal to n. For example: 5! = 5 * 4 * 3 * 2 * 1 = 120. By convention the value of 0! is 1.

Write a function to calculate factorial for a given input. If input is below 0 or above 12 throw an exception of type ArgumentOutOfRangeException (C#) or IllegalArgumentException (Java) or RangeException (PHP) or throw a RangeError (JavaScript) or ValueError (Python) or return -1 (C).
'''

def factorial(n):
    
    if n == 0:
        return 1
    if n < 0 or n > 12:
        raise ValueError
        
    num_list = [] #initializing a new list
    while len(num_list) < n: #basically since factorials are going to be all the numbers until n, so the list has to be less than n elements
        for i in range(n):
            num_list.append(n-i)
        
    mult = 1
    for j in num_list:
        mult *= j
    
    return mult

