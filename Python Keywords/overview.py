'''
KEY WORDS IN PYTHON
'''

'''
   Python keywords are reserved words that have a special meaning associated with them and can’t be used for anything but those specific purposes. Each keyword is designed to achieve specific functionality.
'''

'''
   Python keywords are case-sensitive.

- All keywords contain only letters (no special symbols)

- Except for three keywords ('True', 'False', 'None'), all keywords have lower case letters
'''


'''
   Get the List of Keywrods
'''

'''
    We can use the following two ways to get the list of keywords in Python
'''

''' 1. keyword module: The keyword is the buil-in module to get the list of keywords. Also, this module allows a Python program to determine if a string is a keyword. '''

# example:
import keyword
print(keyword.kwlist)

''' 2. help() function: Apart from a keyword module, we can use the help() function to get the list of keywords '''

# example:
print(help("keywords"))



'''NOTE!!!'''

## You cannot use any of the above keywords as identifiers in your programs. If you try to do so, you will get an error. An identifier is a name given to an entity, For example, variables name, functions name, or class name.
