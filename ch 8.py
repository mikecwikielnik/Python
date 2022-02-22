# CHAPTER 8 FUNCTIONS 


from curses import ACS_GEQUAL
from distutils.command.build import build
from posixpath import commonpath
from turtle import color


def greet_user(): 
    """Display a simple greeting. """
    print("Hello World!")

greet_user()

def greet_user(username):       # username is a parameter
    """Display a simple greeting."""
    print(f"Hello, {username.title()}!")
    
greet_user('jesse')         # jesse is an argument 


# 8-1. Message: Write a function called display_message() that prints one sentence telling everyone what you are learning about in this chapter. Call the function, and make sure the message displays correctly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 131). No Starch Press. Kindle Edition. 

def display_message():
    """Displaying a msg."""
    print(f"I am learning about functions in Ch 8.")
    
display_message()

# 8-2. Favorite Book: Write a function called favorite_book() that accepts one parameter, title.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 131). No Starch Press. Kindle Edition. 

def fav_book(book):
    """"Displaying your fav book"""
    print(f"Your favorite book is {book.title()}.")
    
fav_book('the titan')


# Positional Arguments 

def describe_pet(animal, pet):
    """Display pet info."""
    print(f"\nI have a {animal}.")
    print(f"My {animal}'s name is {pet.title()}!")
    
describe_pet('hamster', 'harry')

# multiple function calls

def describe_pet(animal, pet):
    """Display pet info."""
    print(f"\nI have a {animal}.")
    print(f"My {animal}'s name is {pet.title()}.\n")
    
describe_pet('hamster', 'harry')
describe_pet('dog', 'sampson')


# Keyword Arguments 

# keyword arguments are a name-value pair that you pass thru a function. 
# keyword arguments free you from having to worry about order 


describe_pet(animal='hamster', pet='harry')     # these two function calls are the same 
describe_pet(pet='harry', animal='hamster')



# Default Values 

def describe_pet(pet, animal='dog'):
    """Display info about a pet"""
    print(f"\nI have an {animal}.")
    print(f"My {animal}'s name is {pet.title()}.")
    
describe_pet(pet='sampson')     # NOTE pet is first because it is a positionial arugment 
describe_pet('sampson')         # NOTE that default values come after the non-default values. Again, positional arguments 


# Equivalent Function Calls 

# this is more about the argument made here (see above for original)

def describe_pet(pet, animal='dog'):
    """Display info about a pet"""
    print(f"\nI have an {animal}.")
    print(f"My {animal}'s name is {pet.title()}.")
    
describe_pet(pet='sampson')     # NOTE pet is first because it is a positionial arugment 
describe_pet('sampson')         # NOTE that default values come after the non-default values. Again, positional arguments 

# you can add and it works because it is equivalent to the previous two 

describe_pet(pet='sampson', animal='dog')


# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 137). No Starch Press. Kindle Edition. 

# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 137). No Starch Press. Kindle Edition. 

def make_shirt(size,message):
    """Display message and size of shirts"""
    print(f"{message.title()} is printed on all {size}-sized shirts.\n")
    
make_shirt(size='large', message='pink floyd')      # NOTE all the ways you can type the same things 
make_shirt(message='metallica', size='small')

def make_shirt(message, size='medium'):
    """Display message and size of shirts"""
    print(f"{message.title()} is printed on all {size}-sized shirts.\n")

make_shirt(message='pink floyd')
make_shirt('sampson')

# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. (see above examples)

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 137). No Starch Press. Kindle Edition. 



# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. The function should print a simple sentence, such as Reykjavik is in Iceland. 

# Give the parameter for the country a default value. Call your function for three different cities, at least one of which is not in the default country.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 137). No Starch Press. Kindle Edition. 


def describe_city(city='Boston', country='usa'):
    """Display cities and countries. """
    print(f"The city of {city.title()} is in the country of {country.title()}. \n")
    
describe_city()     # NOTE you have the var established and need not an argument

def describe_city(city, country='Ireland'):
    """Display cities and countries"""
    print(f"The city of {city.title()} is in {country.title()}.\n")
    
describe_city('galway')
describe_city('clifden')
describe_city('prague')

# Returning a simple value

def get_formatted_name(first, last):
    """Return a full name, neatly formatted."""
    full_name=f"{first} {last}"
    return  full_name.title()

musician= get_formatted_name('jimi', 'hendrix')
print(musician)

# But when you consider working with a large program that needs to store many first and last names separately, functions like get_formatted_name() become very useful.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 138). No Starch Press. Kindle Edition. 

# You store first and last names separately and then call this function whenever you want to display a full name.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 138). No Starch Press. Kindle Edition. 


# Making an argument optional 

def get_formatted_name(first, middle, last):
    """Display names."""
    full_name= f"{first} {middle} {last}"
    return full_name.title()

actress= get_formatted_name('sarah', 'michelle', 'gellar')
print(actress)

# then 

def get_formatted_name(first, last, middle=''):     # middle='' moved to the third value
    """Display names."""
    if middle:
        full_name= f"{first} {middle} {last}"
    else:
        full_name= f"{first} {last}"
    return full_name.title()

musician=get_formatted_name(first='biggie', last='smalls')
print(musician)

president=get_formatted_name('john', 'kennedy', 'f')        # f is moved to our third argument  
print(president)


# Returning a Dictionary 

def build_person(first, last):
    """Return a dictionary of info about a person. """
    person={'first':first, 'last':last}     # Remember a dictionary's structure! <- this is a dictionary
    return person

musician=build_person('jimi', 'hendrix')
print(musician)     # returns a dictionary: {'first': 'jimi', 'last': 'hendrix'}


def build_person(first, last, age=None):        # None allows you to return a dictionary with an age. see the xxxtentacion example 
    """Return a dictionary of info about a person. """
    person={'first':first, 'last':last}
    if age:
        person['age']=age
    return person

musician=build_person('kurt', 'cobain', age=27) 
print(musician)

musician=build_person('xxx', 'tentacion', 21)
print(musician)

musician=build_person('xxx', 'tentacion')
print(musician)

# Using a function with a While loop 

# this involves the input function. 
# it is unknown ATTOW how to get the visual code to use this 


# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 

# The function should return a string formatted like this: "Santiago, Chile" 

# Call your function with at least three city-country pairs, and print the values that are returned.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 142). No Starch Press. Kindle Edition. 

def city_country(city, country):
    """City and country info"""
    cities= f"{city}, {country}"
    return cities.title()

london=city_country('london', 'england')
print(london)

glasgow=city_country('glasgow', 'scotland')
print(glasgow)

berlin=city_country('berlin', 'germany')
print(berlin)


# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 

# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 142). No Starch Press. Kindle Edition. 

# Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 142). No Starch Press. Kindle Edition. 


def make_album(artist, album):
    """Display artist info"""
    artists={'artist': artist, 'album': album}
    return artists

artist=make_album('jayz', 'in my life vol 1')
print(artist)

# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 

# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. Make at least one new function call that includes the number of songs on an album.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 142). No Starch Press. Kindle Edition. 


def make_album(artist, album, song=None):
    """Display artist info"""
    artists={'artist': artist, 'album': album}
    if song:
        artists['song']=song
    return artists

artist=make_album('jayz', 'in my life vol 1')
print(artist)
 
artist=make_album('metallica', 'hardwired to self-destruct', 13)
print(artist)

artist=make_album('nas', 'illmatic', 10)
print(artist)

# Passing a list 

def greet_users(names):
    """Print a simple greeting to each user in the list. """
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
        
usernames=['hannah', 'ty', 'margot']
greet_users(usernames)


# Modifying a List in a Function

# Start with some designs that need to be printed.

unprinted_desgins=['phone case', 'robot', 'flowers']
completed_models=[]

# Simulate printing each design, until none are left 
# Move each design to completed_models aftet printing.

while unprinted_desgins:
    current_design = unprinted_desgins.pop()
    print(f"Printing Model: {current_design}")
    completed_models.append(current_design)
    
# Display all completed models 

print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)
    
    
# below is more structured code     

unprinted_desgins = ['phone case', 'robot', 'flowers']
completed_model = []


def printed_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing. 
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printed model: {current_design}")
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed.")
    for completed_model in completed_models:
        print(completed_model)

printed_models(unprinted_desgins, completed_models)
show_completed_models(completed_models)


# preventing a function from modifying a list

# this sections code did not work in the visual studio 



# 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 146). No Starch Press. Kindle Edition. 

messages= ['hi', 'wyd', 'amor']

def show_messages(messages):
    """Print short messages. """
    for message in messages:
        print(f"{message}...")

show_messages(messages)

    
# 8-10. Sending Messages: Start with a copy of your program from Exercise 8-9. 

# Write a function called send_messages() that prints each text message and moves each message to a new list called sent_messages as it’s printed.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 146). No Starch Press. Kindle Edition. 

# After calling the function, print both of your lists to make sure the messages were moved correctly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 146). No Starch Press. Kindle Edition. 



messages= ['hi', 'wyd', 'amor']
sent_messages= []

def send_messages(messages):        # you don't need two inputs
    """Prints small messages. """
    while messages:
        local_messages= messages.pop()      # it is ALL ABOUT the local variable in the loops 
        print(f"These are the {local_messages}.")
        sent_messages.append(local_messages)
        
send_messages(messages)

print(messages)
print(sent_messages)


# 8-11. Archived Messages: Start with your work from Exercise 8-10. Call the function send_messages() with a copy of the list of messages. 

# After calling the function, print both of your lists to show that the original list has retained its messages.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 146). No Starch Press. Kindle Edition. 


# no wonder why you couldn't do this
# that section doesn't work in the visual code studio 


# Passing arbitrary numbers of arguments 

def make_pizza(*toppings):
    """Print the list of toppings that have been requested"""
    print(toppings)
    
make_pizza('pepperoni')
make_pizza('mushrooms', 'peppers', 'extra cheese')


# now we can replace the print() all with a looop that runs through the list

def make_pizza(*toppings):
    """Summarize the pizza we are about to make. """
    print("\nMaking a pizza with the following toppings")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'peppers', 'extra cheese')


# Mixing positional and arbitrary arguments


def make_pizza(size, *toppings):        # parameter name is *args 
    """Summarize the pizza we are about to make. """
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'peppers', 'extra cheese')


# Using arbitrary keyword arguments

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user. """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info    # the dbl asteriks create an empty dict. called user_info & pack whatever name-value pairs in user_info into that dict. 

user_profile = build_profile('albert', 'einstein', 
                            location= 'princeton', field= 'physics')    # **kwargs used to collect non-specific keyword arguments 
print(user_profile)


# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. 

# The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich thats being ordered.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 150). No Starch Press. Kindle Edition. 

# Call the function three times, using a different number of arguments each time.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 150). No Starch Press. Kindle Edition. 


def build_sandwiches(type, **toppings):
    """Build a sandwich type with x toppings. """
    toppings['type']= type
    return toppings

bodega_sandwich= build_sandwiches('turkey', x= 'lettuce', y= 'pickles', z= 'red onion') # very important step. you have to define the toppings for the printed dictionary 

print(bodega_sandwich)

pret_sandwich= build_sandwiches('grilled cheese', x='cheese')

print(pret_sandwich)

chappy_sandwich= build_sandwiches('BLT', x= 'bacon', y= 'lettuce', z= 'tomato', a= 'avocado')

print(chappy_sandwich)

# 8-13. User Profile: Start with a copy of user_profile.py from page 149. 

# Build a profile of yourself by calling build_profile(), using your first and last names and three other key-value pairs that describe you.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 150). No Starch Press. Kindle Edition. 


mike= build_profile('mike', 'cwikielnik', location= 'bushwick', age= '32', tvshow= 'peaky blinders')

print(mike)

# 8-14. Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. 

# It should then accept an arbitrary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. 

# Your function should work for a call like this one:
    
# car = make_car('subaru', 'outback', color='blue', tow_package=True)

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 150). No Starch Press. Kindle Edition. 



def build_cars(manufacturer, model, **features):
    """Build a car dictionary with x features. """
    features['manufacturer']= manufacturer      # what is inside the function here is about adding the static variables to the empty dictionary- features
    features['model']= model        # adding electric below is less important
    return features

car_1= build_cars('subaru', 'outback', electric = 'yes')

print(car_1)


# Storing your functions in Modules 


def make_pizza(size, *toppings):        # parameter name is *args 
    """Summarize the pizza we are about to make. """
    print(f"\nMaking a {size}-inch pizza with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'peppers', 'extra cheese')


# Importing specific functions

#       from module_name import function_name 

#       from module_name import function_0, function_1, function_2

# Using as to give a function an alias

#       from pizza import make_pizza as mp

# anytime we want to call make_pizza() we write mp() instead. 

# General Syntax for providing an alias is: 

#       from module_name import function_name as fn 

# Using as to give a module an alias

# import pizza as p 

#       p.make_pizza(16, 'pepperoni')

# General syntax for this approach is: 

#       import module_name as mn


# Immporting all functions in a module 

#       from pizza import * 

#       make_pizza(16, 'pepperoni') 
#       make_pizza(12, 'mushrooms', 'peppers', 'extra cheese')

# Styling functions

# def function_name(parameter_0, parameter_1='default value') if you specify a default value for a parameter, no spaces should be used on either side of the equal sign 

# function_name(value_0, parameter_1='value') same convention should be used for keyword arguments in function calls 






# Import on Visual Code Studio is not able to *import* functions so on pages 154, questions 8-15 thru 8-17 weren't able to be completed. 


