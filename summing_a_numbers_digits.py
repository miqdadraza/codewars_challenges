'''
Write a function named sumDigits which takes a number as input and returns the sum of the absolute value of each of the number's decimal digits. For example:

  sum_digits(10)  # Returns 1
  sum_digits(99)  # Returns 18
  sum_digits(-32) # Returns 5
Let's assume that all numbers in the input will be integer values.
'''

def sum_digits(number):
    # ...
    checks_int = [0,1,2,3,4,5,6,7,8,9]
    checks_str = []
    for i in checks_int: #converting the check list to strings
        n = str(i)
        checks_str.append(n)
        
    nums = []
    
    for i in str(number):
        if i in checks_str: #this step is to avoid signs like - or + to be converted to int
            n = int(i)
            nums.append(n)
    
    abs_nums = []
    for i in nums:
        ab = abs(i)
        abs_nums.append(ab)
    
    sums = sum(abs_nums)
    return sums