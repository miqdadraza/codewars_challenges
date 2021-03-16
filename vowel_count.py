'''
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
'''

def get_count(input_str):
    num_vowels = 0
    for i in str(input_str):
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u': #basically iterate over the whole string, if its a vowel, add 1 to the count. could have used list also
            
            num_vowels +=1
    return num_vowels

print(get_count("abracadabra"))