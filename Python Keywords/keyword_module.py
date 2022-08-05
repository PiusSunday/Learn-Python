''' KEYWORD MODULE'''

## Python keyword module allows a Python program to determine if a string is a keyword.

# iskeyword(s): Returns True if s is a keyword

''' example: '''

import keyword
print(keyword.iskeyword('if'))
print(keyword.iskeyword('range'))

# output: True False


''' Also, keyword module provides following functions to identify keywords. '''

# 1. keyword.kwlist: It return a sequence containing all the keywords defined for the interpreter.


# 2. keyword.issoftkeyword(s): Return True if s is a Python soft keyword. New in version 3.9

# 3. keyword.softkwlist: Sequence containing all the soft keywords defined for the interpreter.
