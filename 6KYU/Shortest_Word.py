# Simple, given a string of words, return the length of the shortest word(s).

# String will never be empty and you do not need to account for different data types.

import math

def find_short(s):
    # your code here
    
    words = s.strip().split(" ")
    
    l = math.inf
    for word in words:
        if len(word) < l:
            l = len(word)
    
    return l # l: shortest word length
