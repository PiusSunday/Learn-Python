## DEL STATEMENT

# The del statement can be used to delete variables, objects, and even entire namespaces.

# SYNTAX

# del target_list

# target_list - The name of the variable, object, or namespace to be deleted. Once the variable is deleted, we can’t access it.


# Example

x = 10
y = 30
print(x, y)

# delete x and y
del x, y

# try to access it
print(x, y)

# Output:

# First print
10, 30

# Second print

# NameError: name 'x' is not defined
