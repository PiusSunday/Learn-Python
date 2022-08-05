' Variable Handling Keywords: "del", "global", "nonlocal" '


'# 1. del keyword: the del keyword is used to delete the specified variable or object.'

'# 2. global keyword: the global keyword is used to declare a variable as global. A global variable is a variable that is defined outside of the method (block of code). That is accessible anywhere in the code file.'


'# 3. Nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.'


# example:

price = 900  # Global variable


def test1():  # defining 1st function
    print("price in 1st function :", price)  # 900


def test2():  # defining 2nd function
    print("price in 2nd function :", price)  # 900


# call functions
test1()
test2()

# delete variable
del price
