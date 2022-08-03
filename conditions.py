## CONDITINS

# Python uses boolean logic to evaluate conditions. The boolean values True and False are returned when an expression is compared or evaluated. For example:

x = 2
print(x == 2)  # prints out True
print(x == 3)  # prints out False
print(x < 3)  # prints out True

# NOTE!!!
# The == operator is used to compare two values. If the values are equal, True is returned. If they are not equal, False is returned.

# The < operator is used to compare two values. If the first value is less than the second value, True is returned. If the first value is not less than the second value, False is returned.

# The > operator is used to compare two values. If the first value is greater than the second value, True is returned. If the first value is not greater than the second value, False is returned.

# The <= operator is used to compare two values. If the first value is less than or equal to the second value, True is returned. If the first value is not less than or equal to the second value, False is returned.

# The >= operator is used to compare two values. If the first value is greater than or equal to the second value, True is returned. If the first value is not greater than or equal to the second value, False is returned.

# The != operator is used to compare two values. If the first value is not equal to the second value, True is returned. If the first value is equal to the second value, False is returned.

## BOOLEAN OPERATORS (and, or, not)

# The boolean operators and (&&), or (||), and not (!) are used to combine boolean values. For example:

name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")


print(not False)  # Prints out True
print((not False) == (False))  # Prints out False



## THE "in" OPERATOR

# The "in" operator is used to check if a value or specified object is found within a sequence or within an iterable object container (string, list, tuple, set, or dictionary). For example:

name = "John"
if name in ["John", "Rick"]:
    print("Your name is either John or Rick.")



## THE "is" OPERATOR

# Unlike the double equals operator "==", The "is" operator is used to check if two objects are the same object, it matches the instances of the values in a variable. For example:

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False


## Python uses indentation to define code blocks, instead of brackets. The standard Python indentation is 4 spaces, although tabs and any other space size will work, as long as it is consistent. Notice that code blocks do not need any termination.

# Here is an example for using Python's "if" statement using code blocks:

statement = False
another_statement = True
if statement is True:
    # do something
    pass
elif another_statement is True:  # else if
    # do something else
    pass
else:
    # do another thing
    pass



## Another example for using Python's "if" statement using code blocks:

x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")


## A statement is evaulated as true if one of the following is correct: 

# 1. The "True" boolean variable is given, or calculated using an expression, such as an arithmetic comparison. 

# 2. An object which is not considered "empty" is passed.

## Here are some examples for objects which are considered as empty: 

# 1. An empty string: "" 

# 2. An empty list: [] 

# 3. The number zero: 0 

# 4. The false boolean variable: False




## EXERCISE

# Change the variables in the first section, so that each if statement resolves as True.


# change this code
number = 20
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
