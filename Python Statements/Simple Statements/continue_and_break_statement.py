## THE CONTINUE AND BREAK STATEMENTS

# break Statement: The break statement is used inside the loop to exit out of the loop.

# example:

numbers = [10, 40, 120, 230]
for i in numbers:
    if i > 100:
        break
    print('current number', i)

# continue Statement: The continue statement skip the current iteration and move to the next iteration.

# example:

numbers = [2, 3, 11, 7]
for i in numbers:
    print('Current Number is', i)
    # skip below statement if number is greater than 10
    if i > 10:
        continue
    square = i * i
    print('Square of a current number is', square)
