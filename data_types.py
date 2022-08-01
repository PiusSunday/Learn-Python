## Python is completely object oriented, and not "statically typed". You do not need to declare variables before using them, or declare their type. Every variable in Python is an object.

# 1. NUMBERS

# Python supports two types of numbers - integers(whole numbers) and floating point numbers(decimals).

myint = 7  # integer number
print(myint)


myfloat = 7.0 # floating number
print(myfloat)
myfloat = float(7)
print(myfloat)


# 2. STRINGS

# Strings are defined either with a single quote or a double quotes.

mystring = 'hello' # single quote
print(mystring)

mystring = "hello" # double quotes
print(mystring)

# The difference between the two is that using double quotes makes it easy to include apostrophes (whereas these would terminate the string if using single quotes)

mystring = "Don't worry about apostrophes"
print(mystring)


# There are additional variations on defining strings that make it easier to include things such as carriage returns, backslashes and Unicode characters.

one = 1
two = 2
three = one + two
print(three)

hello = "hello"
world = "world"
helloworld = hello + " " + world
print(helloworld)


# Assignments can be done on more than one variable "simultaneously" on the same line like this

a, b = 3, 4
print(a, b)


# Although, Mixing operators between numbers and strings is not supported:

# This will not work!
one = 1
two = 2
hello = "hello"

print(one + two + hello)



### PUTTING IT ALL TOGETHER

mystring = "hello"
myfloat = 10.0
myint = 20

# testing code
if mystring == "hello":
    print("String: %s" % mystring)
if isinstance(myfloat, float) and myfloat == 10.0:
    print("Float: %f" % myfloat)
if isinstance(myint, int) and myint == 20:
    print("Integer: %d" % myint)
