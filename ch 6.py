# CHAPTER 6 DICTIONARIES 

alien_0 = {'color': 'green', 'points':5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"you just earned {new_points} points!")

alien_0['x_position'] = 0       # adding two new elements to the alien_0 dictionary 
alien_0['y_position'] = 25

print(alien_0)


# starting with an empyt dictionary 

alien_0 = {}                # starting with an empty dictionary 

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)


# modfying values in a dictionary 

alien_0 = {'color': 'green'}
print(f"the alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"the alien is now {alien_0['color']}.")

# dictionary then loop then print 

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"original position: {alien_0['x_position']}.")

# move the alien to the right   
    # determine how far to move the alien base on its current speed. 

if alien_0['speed'] == 'slow':
        x_increment = 1
elif alien_0['speed'] == 'medium':
        x_increment = 2
else: 
    # this must be a fast alien 
    x_increment = 3 

# the new position is the old position plus the increment. 

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"new position: {alien_0['x_position']}")


# removing key-value pairs 


alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}


language = favorite_languages['sarah'].title()
print(f"Sarahs favorite language is {language}")


# using get() to access values 


alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])


point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)


point_value = alien_0.get('points')  # note pg 98 
print(point_value)

# 6-1. Person: Use a dictionary to store information about a person you know. Store their first name, last name, age, and the city in which they live. You should have keys such as first_name, last_name, age, and city. Print each piece of information stored in your dictionary.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 99). No Starch Press. Kindle Edition. 


customer = {'first_name': 'john', 'last_name': 'rockefeller',
                'age': 100, 'city': 'new york city'}
print(customer['age'])
print(customer['city'])
print(customer['first_name'])
print(customer['last_name'])

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number. For even more fun, poll a few friends and get some actual data for your program.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 99). No Starch Press. Kindle Edition. 

covid = {'brown': 2, 'elwell': 11, 'bill': 5, 'levenson': 30, 'phil': 69}

print(covid['bill'])
print(covid['brown'])
print(covid['elwell'])
print(covid['levenson'])
print(covid['phil'])

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 99). No Starch Press. Kindle Edition. 

# Use these words as the keys in your glossary, and store their meanings as values.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 99). No Starch Press. Kindle Edition. 

covid_num = covid['brown']
print(f"Brown's favorite number is {covid_num}!!")

covid_num1 = covid['bill']
print(f"bill is {covid_num1} and browns is {covid_num}")


# Looping through a dictionary
# you can loop thru all of a dictionarys key-value pairs, throught its keys,
# or through its values 


# looping thru all key-value pairs

user_0 = {
    'user': 'efermi',
    'first': 'rico',
    'last': 'suave',
}


for key, value in user_0.items():   # items() returns a list of key-value pairs 
    print(f"\nkey: {key}")      # key is the first element of the ordered pair
    print(f"Value: {value}")    # value is the second element of the ordered pair 


# for k, v in user_0.items()
# the for loop assigns each of these pairs to the 2 var (k,v) provided. 


for key, value in covid.items():    # good example
    print(f"\nName: {key}")         # pg 101, replaced fav lang ex
    print(f"Number: {value}")



for key, value in covid.items():        # good progress 
    print(f"{key.title()}'s favorite number is {value}!")


# looping through the all the keys in a dictionary 

# keys() is when u don't need to work the values


for key in user_0.keys():
    print(key.upper())


for key in covid.keys():        # prints names only
    print(key.title())

for key in covid:       # looping thru keys is defautl
    print(key)          # this and the above ex yields the same output (case sensitive)

# keys() method makes things easier to read 

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, i see you love {language}!")


friends = ['brown', 'elwell']
for name in covid.keys():
    print(f"hi {name.title()}.")

    if name in friends:
        number = covid[name]        # number need not a title! 
        print(f"\t{name.title()}, i see you love {number}")

# hi Brown.
#         Brown, i see you love 2
# hi Elwell.
#         Elwell, i see you love 11
# hi Bill.
# hi Levenson.
# hi Phil.



if 'bill' not in covid.keys():
    print("bill take our poll")
else:                                           # why not elif?  
    print("everyone has taken the poll")        # else is catchall       


if 'mike' not in covid.keys():
    print(f"mike is in another meeting.")
else:
    print(f"mike has taken the poll.")


for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")  # ea1 is thanked

#  This for statement is like other for statements except that we’ve wrapped the sorted() function around the dictionary.keys() method. 
# This tells Python to list all keys in the dictionary and sort that list before looping through it. 
# The output shows everyone who took the poll, with the names displayed in order:

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 103). No Starch Press. Kindle Edition.    


print("the following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# loop prints all the values in the (key, value) ordered pair. 
# Python
# C
# Ruby
# Python


# to review:
# The for statement here pulls each value from the dictionary and assigns it to the variable language.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 104). No Starch Press. Kindle Edition. 

# *** to see unique records in the value set, use set

for language in set(favorite_languages.values()):
    print(language.title())

# C
# Python
# Ruby

# dictionary vs set
# languages = {x:1, y:2, z:3} dictionary
# languages = {x, y, z} set 

# 6-4 Glossary 2: by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 105). No Starch Press. Kindle Edition. 


for key, value in covid.items():
    print(f"\n{key}")
    print(f"\n{value}")

for key, value in covid.items():                # this is better 
    print(f"\n{key} picked number {value}.")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 105). No Starch Press. Kindle Edition. 


cities = {
    'boston':'mass',
    'nyc':'ny',
    'miami':'fl'
}

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 105). No Starch Press. Kindle Edition. 


for key,value in cities.items():
    print(f"\n{key} is in {value}.")

# Use a loop to print the name of each river included in the dictionary.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 105). No Starch Press. Kindle Edition. 


for city in cities.keys():
    print(city)


# Use a loop to print the name of each country included in the dictionary.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 105). No Starch Press. Kindle Edition. 


for city in cities.values():
    print(city)



# NESTING pg 106

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)



# Make an empty list for storing aliens

aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)


for alien in aliens[:3]:
    if alien['color']=='green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15 

# show the first 5 aliens

for alien in aliens[:5]:
    print(alien)

print("...") # not sure why this is here except to segway onto the next item

# show how many aliens have been created

print(f"total number of aliens: {len(aliens)}")



# a list in a dictionary

# store information about a pizza being ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}

# summarize the order 

print(f"you ordered a {pizza['crust']}-crust pizza " # don't forget the space! 
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\n{topping}")


favorite_languages = {
    'jen':['python', 'ruby'],
    'sarah':['c'],
    'edward':['ruby', 'go'],
    'phil': ['python', 'haskell']
}


for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")



# a dictionary in a dictionary 

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}" 
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")



# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 

# Loop through your list of people. As you loop through the list, print everything you know about each person.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 


people = {
    'a': {
        'first': 'john',
        'last': 'rockefeller',
        'age': 100,
        'city': 'new york city',
        },
    'b': {
        'first': 'mike',
        'last': 'cwikielnik',
        'age': 100,
        'city': 'new york city',
        },
    'c': {
        'first': 'andrew',
        'last': 'carnegie',
        'age': 100,
        'city': 'glasgow',
        },
}

for person, person_info in people.items():
    print(f"\nLetter: {person}")
    print(f"{person_info['age']}")
    print(f"{person_info['first']}")
    print(f"{person_info['last']}")
    print(f"{person_info['city']}")






# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 

# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 

pets = {
    '101': {
        'animal': 'cat',
        'color': 'grey',
        'age': 5,
        'location': 'Boston',
    },
    '102': {
        'animal': 'dog',
        'color': 'brown',
        'age': 3,
        'location': 'Boston',
    },
    '103': {
        'animal': 'bird',
        'color': 'blue',
        'age': 1,
        'location': 'New York City',
    },
    '104': {      
        'animal': 'cat',
        'color': 'black',
        'age': 8,
        'location': 'Texas',
    },    
}

for id, pets in pets.items():
    print(f"ID Number: {id}")

    print(f"This {pets['animal']} is {pets['age']} years old.")
    print(f"This {pets['color']} {pets['animal']} is from below:\n{pets['location']}\n")


# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 

# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 


favorite_places = {
                '1001': {
                    'person': 'mike',
                    'location': 'quincy',
                },
                '1002': {
                    'person': 'santa',
                    'location': 'north pole',
                },
}

for one, two in favorite_places.items():
        print(f"ID Number: {one}")
        print(f"This person is named {two['person'].title()}.")
        print(f"{two['person'].title()} lives in {two['location'].title()}!\n")


for one, two in favorite_places.items():
       if one=="1002":                      # prints just the santa entry NOTE: if loop inside a for loop  
        print(f"ID Number: {one}")
        print(f"This person is named {two['person'].title()}.")
        print(f"{two['person'].title()} lives in {two['location'].title()}!\n")

for one, two in favorite_places.items():
       if two['location']=="north pole":    # prints just the santa entry NOTE: if loop inside a for loop  && NOTE: the value loop at a deeper level of ['location'] draws the santa record
        print(f"ID Number: {one}")
        print(f"This person is named {two['person'].title()}.")
        print(f"{two['person'].title()} lives in {two['location'].title()}!\n")



# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each person’s name along with their favorite numbers.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 

covid = {
        'brown':
            'nums': 1,2,3,
        'elwell':
            'nums': 11,12,14, 
        'bill':
            'nums': 15,16,17,
        'levenson':
            'nums': 30,60,90, 
        'phil':
            'nums': 69,70,71,
}

for person, nums in covid.items():
    print(f"{person.title()} loves {nums}.")


# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as keys in your dictionary.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 112). No Starch Press. Kindle Edition. 

states= {
    'ma':{
        'capitol': 'boston',
        'best': 'quincy',
    },
    'nh':{
        'capitol': 'manchester',
        'best': 'portsmouth'
    },
    'ri':{
        'capitol': 'provdience',
        'best': 'newport'
    },
}


for one, two in states.items():
    print(f"{one.title()}'s best city is {two['best'].title()}!!!")
    print(f"{two['capitol'].title()} is the capitol.\n")