'''
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
'''

def xo(s):
    xs = 0 #initialize xs and os
    os = 0
    for char in s:
        if char in ('x', 'X'): 
            xs +=1
        if char in ('o', 'O'):
            os +=1
    if xs == os: #if the number of xs and os are the same, return True. This will also work if both are still 0.
        return True
    else:
        return False
    