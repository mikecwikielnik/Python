

from itertools import count
from random import getstate
from collections import Counter


def gstest(test_str):
    """
    Attempt to find the max occuring character. 
    """
    string = Counter(test_str)
    # string = max(string, key = string.get)
    print(str(string))

gstest('GeeksforGeeks')

# Counter({'e': 4, 'G': 2, 'k': 2, 's': 2, 'f': 1, 'o': 1, 'r': 1})

gstest('abbbaacc')

# Counter({'a': 3, 'b': 3, 'c': 2})


def gstest(test_str):
    """
    Attempt to find the max occuring character. 
    """
    string = Counter(test_str)
    string = max(string, key = string.get)
    print(f"This is the max occuring character: " + str(string))

gstest('helloworld')  