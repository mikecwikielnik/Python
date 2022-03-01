# CHAPTER 10 
"""Files and Exceptions. """


from isort import file
from sympy import content


with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)

print(contents.rstrip())        # strips the white space at the end of the string. 

# File paths 

with open('practice/txt_practice.txt') as file_object:      # relative file path, drilling down a level within py_files folder  
    contents = file_object.read()
print(contents.rstrip())



file_path = 'C:/Users/mikec/Google Drive/Py_files/practice/fives.txt'       # absolute path. NOTE: google drive 
with open(file_path) as file_object:
    contents = file_object.read()
print(contents.rstrip())


# Reading line by line 


# we assign the name of the file we’re reading from to the variable filename. This is a common convention when working with files. 

# Because the variable filename doesn’t represent the actual file—

# it’s just a string telling Python where to find the file—you can easily swap out 'pi_digits.txt' for the name of another file you want to work with.

# After we call open(), an object representing the file and its contents is assigned to the variable file_object . We again use the with syntax to let Python open and close the file properly.

# To examine the file’s contents, we work through each line in the file by looping over the file object.  

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 187). No Starch Press. Kindle Edition. 

filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line)
        
# or you can print like this: removes the white characters

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
        
# Making a list of lines from a file 

filename = 'practice/fives.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())
    
# the readlines() method takes each line from the file and stores it in a list. 

# This list is then assigned to lines, which we can continue to work with after the with block ends.  we use a simple for loop to print each line from lines.

# Because each item in lines corresponds to each line in the file, the output matches the contents of the file exactly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 188). No Starch Press. Kindle Edition. 


# Working with a File's Contents 

filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.rstrip() # using strip() will collapse the string

print(pi_string)

print(len(pi_string))


# 10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. 

# Write a program that reads the file and prints what you wrote three times. 

# Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and 

# then working with them outside the with block.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 191). No Starch Press. Kindle Edition. 


with open('practice/fives.txt') as file_object:     # Read the entire file 
    contents = file_object.read()
print(contents.strip())

with open('practice/txt_practice.txt') as file_object:      # Looping over the file object
    for line in file_object:
        print(line.strip())
        
with open('practice/txt_practice.txt') as file_object:      # Storing lines in a list and working with list outside of block
    lines = file_object.readlines()
    
line_string = ''
for line in lines:
    line_string += line.strip()

print(line_string)


# 10-2. Learning C: You can use the replace() method to replace any word in a string with a different word.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 191). No Starch Press. Kindle Edition. 

with open('practice/animals.txt') as file_object:
    contents = file_object.read()
    contents = contents.replace('Snake', 'Cat')
print(contents.strip())


# Writing to a file 

# Writing to an empty file 

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. ")
    
    
# Writing Multiple Lines 

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")
    file_object.write("I love creating new games. \n")

# Appending to a file 

filename = 'programming.txt'

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets.")
    file_object.write("I love creating apps that can run in browser. ")


# 10-3. Guest: Write a program that prompts the user for their name. 

# When they respond, write their name to a file called guest.txt.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 193). No Starch Press. Kindle Edition. 


filename = 'guest_list.py'

with open(filename, 'w') as file_object:
    file_object.write("# I am at my desk.")
    
    
# 10-4. Guest Book: Write a while loop that prompts users for their name.

# When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt.

# Make sure each entry appears on a new line in the file.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 193). No Starch Press. Kindle Edition.

with open(filename, 'a') as file_object:
    file_object.write('\nBoston Bruins are playing hockey!')
    file_object.write('New England Patriots are playing football \n 28-3. ')
    
# Exceptions 

# Handling the ZeroDivisionError Exception 

print(5/0)

# Using try-except blocks 

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by 0! ")
    
# Handling the FileNotFoundError Exception

filename = 'alice.txt'

with open(filename, encoding='utf-8') as f:
    contents = f.read()

filename = 'alice.txt'

try:
    with open(filename, encoding='utc-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist. ")
    
    
# Analyzing Text 

