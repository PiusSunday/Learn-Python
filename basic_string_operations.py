## BASIC STRING OPERATIONS

# Strings are bits of text. They can be defined as anything between quotes.

#exp.
astring = "Hello world!"
astring2 = 'Hello world!'

## Special cases of strings

# You can also use single quotes to assign a string. However, you will face problems if the value to be assigned itself contains single quotes. For example to assign the string in these bracket(single quotes are ' ') you need to use double quotes only like this

#exp.
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring)) # That prints out 12, because "Hello world!" is 12 characters long, including punctuation and spaces.


## Some string methods
astring = "Hello world!"

print(astring.index("o")) # This prints out the index of the first occurrence of the letter "o" in the string.

print(astring.count("l")) # This prints out the number of times the letter "l" occurs in the string.

print(astring[3:7]) # This prints out the characters from index 3 to index 7 (exclusive).

print(astring[3:7:2]) # This prints out the characters from index 3 to index 7 (exclusive), but skips every other character.

# [start:stop:step]

print(astring[3:7:1]) # This prints out the characters from index 3 to index 7 (exclusive), but skips 0 character.

print(astring[::-1]) # This prints out the string in reverse order.

print(astring.upper()) # This prints out the string, but in uppercase.
print(astring.lower()) # This prints out the string in lowercase.

print(astring.startswith("Hello")) # This prints out True if the string starts with "Hello" and False otherwise.

print(astring.endswith("asdfasdfasdf")) # This prints out True if the string ends with "asdfasdfasdf" and False otherwise.

afewwords = astring.split(" ")
# This splits the string into a bunch of strings grouped together in a list. Since this example splits at a space, the first item in the list will be "Hello", and the second will be "world!".
print(afewwords)




## EXERCISE
# Try to fix the code to print out the correct information by changing the string.

s = "Strings are awesome!"
# Length should be 20
print("Length of s = %d" % len(s))

# First occurrence of "a" should be at index 8
print("The first occurrence of the letter a = %d" % s.index("a"))

# Number of a's should be 2
print("a occurs %d times" % s.count("a"))

# Slicing the string into bits
print("The first five characters are '%s'" % s[:5])  # Start to 5
print("The next five characters are '%s'" % s[5:10])  # 5 to 10
print("The thirteenth character is '%s'" % s[12])  # Just number 12
print("The characters with odd index are '%s'" % s[1::2])  # (0-based indexing)
print("The last five characters are '%s'" % s[-5:])  # 5th-from-last to end

# Convert everything to uppercase
print("String in uppercase: %s" % s.upper())

# Convert everything to lowercase
print("String in lowercase: %s" % s.lower())

# Check how a string starts
if s.startswith("Str"):
    print("String starts with 'Str'. Good!")

# Check how a string ends
if s.endswith("ome!"):
    print("String ends with 'ome!'. Good!")

# Split the string into three separate strings,
# each containing only a word
print("Split the words of the string: %s" % s.split(" "))
