''' Operator Keywords: 'and', 'or', 'not', 'in', 'is' '''


'''# The logical "and" keyword returns True if both expressions are True. Otherwise, it will return. False. '''

'''# The logical "or" keyword returns a boolean True if one expression is true, and it returns False if both values are false.'''

'''# The logical "not" keyword returns boolean True if the expression is false'''


# example:

x = 10
y = 20

# and to combine to conditions
# both need to be true to execute if block
if x > 5 and y < 25:
    print(x + 5)

# or condition
# at least 1 need to be true to execute if block
if x > 5 or y < 100:
    print(x + 5)

# not condition
# condition must be false
if not x:
    print(x + 5)



''' is keyword: '''

'''# The is keyword returns return True if the memory address first value is equal to the second value.'''

# example:

# is keyword demo
x = 10
y = 11
z = 10
print(x is y)  # it compare memory address of x and y
print(x is z)  # it compare memory address of x and z


''' in keyword: '''

'''# The in keyword returns True if it finds a given object in the sequence (such as list, string).'''

# example:

my_list = [11, 15, 21, 29, 50, 70]
number = 15
if number in my_list:
    print("number is present")
else:
    print("number is not present")

