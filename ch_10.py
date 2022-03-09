# CHAPTER 10 
"""Files and Exceptions. """


from csv import excel_tab
from itertools import count
from urllib.error import ContentTooShortError
from isort import file
from matplotlib.font_manager import json_dump
from matplotlib.pyplot import text
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

title = 'Alice in Wonderland'

title.split()

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist. ")
else:
    # Count the number of words in a file.
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words. ")

# Very cool! 

# Working with multiple files 

def counted_words(filename):
    """Count the approximate words of a file. """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist. ")
    else:
        # Count the words of a file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words. ")

filename = ['alice.txt', 'goosebumps.txt', 'scarlet.txt', 'frankenstein.txt']

for file in filename:
    counted_words(file)
    
    
# Failing Silently 


def counted_words(filename):
    """"Count words in a file. """
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"This file {filename} has about {num_words} words. ")

filename = ['alice.txt', 'goosebumps.txt', 'scarlet.txt', 'frankenstein.txt']

for file in filename:
    counted_words(file)
    
# 10-6. Addition: One common problem when prompting for numerical input occurs when people provide text instead of numbers. 

# When you try to convert the input to an int, you’ll get a ValueError. Write a program that prompts for two numbers. 

# Add them together and print the result. Catch the ValueError if either input value is not a number, and print a friendly error message. 

# Test your program by entering two numbers and then by entering some text instead of a number.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 201). No Starch Press. Kindle Edition. 
    
def add_num(a,b):
    """
    Add numbers.
    Note: We could not generate a message for the Value Error. We were able to generate a message for ZeroDivision Error instead. 
    """
    try:
        a/b
    except ZeroDivisionError:
        print("Sorry. ")
    else:
        print(a/b)

add_num(1,2)

add_num(5,0)


# 10-7. Addition Calculator: Wrap your code from Exercise 10-6 in a while loop so the user can continue entering numbers 

# even if they make a mistake and enter text instead of a number.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 202). No Starch Press. Kindle Edition. 

# Visual code doesn't allow for input functions 


# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. 

# Write a program that tries to read these files and print the contents of the file to the screen. 

# Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. 

# Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 202). No Starch Press. Kindle Edition. 


filename = 'cats.txt'

with open(filename, 'w') as f:
    f.write('frack frank frick')
    
# filename = 'dogs.txt'

# with open(filename, 'w') as f:
#     f.write('dennis charlie mac')


with open('cats.txt') as f:
    lines = f.readlines()

f_string = ''
for line in lines:
    f_string += line.strip()
    
print(f_string)
print(len(f_string))


def sunny(filename):
    """An attempt to create a try/except block. """
    
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, {filename} Not Available. ")
    else:
        words = contents.split()
        num_words = len(words)
        print(f"This {filename} file has {num_words} words. ")
        
filename = ['cats.txt', 'dogs.txt', 'bird.txt']

for file in filename:
    sunny(file)


try:        # below you have the relative path for animals.txt and the output is 4 words. 
    with open('practice/animals.txt', encoding='utf-8') as f:
        contents= f.read()
except FileNotFoundError:
    pass
else: 
    words = contents.split()
    num_words = len(words)
    print(f"{num_words}")
    

# 10-9. Silent Cats and Dogs: Modify your except block in Exercise 10-8 to fail silently if either file is missing.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 202). No Starch Press. Kindle Edition. 

def silent_pets(filename):

    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = len(words)
        print(f"this {filename} has {num_words} words. ")
    
filename = ['dogs.txt', 'birds.txt', 'cats.txt']

for file in filename:
    silent_pets(file)
    
    
# 10-10. Common Words: Write a program that reads the files you found at Project Gutenberg and determines how many times the word 'the' appears in each text. 

# This will be an approximation because it will also count words such as 'then' and 'there'. 

# Try counting 'the ', with a space in the string, and see how much lower your count is.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 202). No Starch Press. Kindle Edition. 

def counted_words(filename):
    """An attempt to count a particular word in a text. """
    
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        pass
    else:
        words = contents.split()
        num_words = words.count('the')      # the book hinted at this line with its capitalization example. You did this by yourself. Great job! 
        print(f"{filename} has the word 'the' {num_words} times. ")
        
filename = ['alice.txt', 'frankenstein.txt', 'scarlet.txt']
        
for file in filename:
    counted_words(file)
    


# Storing Data 


import json

numbers = [2,3,5,7,11,13]

# 1

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)

# 2
    
filename = 'numbers.json'

with open(filename) as f:
    numbers = json.load(f)
    
print(numbers)

# This is a simple way to share data between two programs. 

# Saving and Reading User-Generated Data

import json

username = input("What is your name? ")     # You must stop here so you can input a name. 

filename = 'username.json'

with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We'll remember you when you come back, {username}. ")
    
import json 

filename = 'username.json.'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}! ")
    
    
# 3

import json 

# Load the username, if it has been stored 
#   Otherwise, prompt the username and store it. 

filename = 'username.json'
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}! ")
else: 
    print(f"Welcome back, {username}! ")



# Refactoring 

import json

def greet_user():
    """Greet the user by name. """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}! ")

greet_user()


# Let’s refactor greet_user() so it’s not doing so many different tasks.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 206). No Starch Press. Kindle Edition. 


import json 

def get_stored_username():
    """Get stored username if available. """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return username
    
def greet_user():
    """Greet the user by name. """
    username = get_stored_username
    if username:
        print(f"Welcome back, {username}! ")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you whenn you come back, {username}! ")
        
greet_user()


# Final product 


import json 

def get_stored_username():
    """Get stored username if available. """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return username

def get_new_username():
    """Prompt for a new username. """
    username =  input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet the user by name. """
    username = get_stored_username
    if username:
        print(f"Welcome back, {username}! ")
    else: 
        username =  get_new_username()
        print(f"We'll remember you when you come back, {username}! ")
        
greet_user()


# 10-11. Favorite Number: Write a program that prompts for the user’s favorite number. Use json.dump() to store this number in a file. 

# Write a separate program that reads in this value and prints the message, “I know your favorite number! It’s _____.”

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 208). No Starch Press. Kindle Edition. 


import json

user_number = input("What is your favorite number?")    # remember for visual code studio, the hack is to stop here, input number and run rest of code

filename = 'user_number.json'

with open(filename, 'w') as f:
    json.dump(user_number, f)
    print(f"I know you favorite number! It's {user_number}! ")
    

# 10-12. Favorite Number Remembered: Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user.

# If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 208). No Starch Press. Kindle Edition. 

import json 

filename = 'user_number.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Andy Moog had the number {user_number}! ") 
    
    
# 10-13. Verify User: The final listing for remember_me.py assumes either that the user has already entered their username or that the program is running for the first time. 

# We should modify it in case the current user is not the person who last used the program. 

# Before printing a welcome back message in greet_user(), ask the user if this is the correct username. 

# If it’s not, call get_new_username() to get the correct username.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 208). No Starch Press. Kindle Edition. 


import json

def get_stored_username():
    """Get stored username if available. """
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None 
    else:
        return username

def get_new_username():
    """Prompt for a new username. """
    username =  input("what is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """
    Greet the user by name. 
    BTW, this version of greet_user() is completely original work. 
    You developed the program to *your* exact standards. 
    """
    username = get_stored_username
    answer = input(f"Is this your user name {username}? ")      # answer needs a variable so you can assign yes/no to it. 
    if answer == 'yes':
        print(f"Hello {username}. ")
    elif answer == 'no': 
        username =  get_new_username()      # here, we enter the get_new_username method 
        print(f"Welcome back {username}! ")
    else:
        print("You don't have an account. ")        # anything but yes or no will yield this message 
        



get_new_username()
get_stored_username()
greet_user()


