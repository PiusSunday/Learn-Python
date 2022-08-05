'''Structure Keywords: 'def', 'class', 'with', 'as', 'pass', 'lambda' 
'''


'# 1. def: The def keyword is used to define user-defined funtion or methods of a class'

# example: def keyword

# def keyword: create function

def addition(num1, num2):
    print('Sum is', num1 + num2)

# call function
addition(10, 20)



'# 2. pass: The pass keyword is used when a statement is required syntactically but you do not want any command or code to execute.'

# example: pass keyword

# pass keyword: create syntactically empty function
# code to add in future
def sub(num1, num2):
    pass



'# 3. class: The class keyword is used to define a class. A class is a collection of objects which share common attributes and methods.'

'# Object-oriented programming(OOP) is a programming paradigm based on the concept of “objects“. An object-oriented paradigm is to design the program using classes and objects rather than using simple data types and functions.'

# example: class keyword:

# create class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(self.name, self.age)


# create object
s = Student('Jessa', 19)
# call method
s.show()



# 4. with: The with keyword is used to define a context manager. A context manager is an object that defines how to handle the life cycle of a resource. 

# with keyword is used when working with unmanaged resources(like file streams). It allows you to ensure that a resource is “cleaned up” when the code that uses it finishes running, even if exceptions are thrown.

# example: with keyword

# Opening file
with open('sample.txt', 'r', encoding='utf-8') as fp:
    # read sample.txt
    print(fp.read())
  
