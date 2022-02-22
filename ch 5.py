# CHAPTER 5

from typing_extensions import Required


cars=['adui', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

car = 'bmw'
car == 'bmw'

# == is the equality operator. true returns if they match 

car = 'audi'
car == 'bmw'    # false, if else 

car ='Audi'
car.lower() == "audi"   # lower fn doesn't change the value originally stored in car 
car

requested_topping='mushrooms'
if requested_topping != 'pepperoni':
    print("fuck that pepperoni")

# numerical comparions

age = 18
age == 18

answer = 17

if answer != 42:
    print("Wrong Answer!")

x=5

x>2
x>6
x>=5
x<=99


1<2 and 100<101 # it should be clear that you can do this variables too 

2<1 and 100<101 # false

1<2 or 100<101


banned = ['alex', 'john']
user = 'mike'

if user not in banned:
    print(f"{user.title()}, you can post a response if you wish.")

# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test. Your code should look something like this:

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 78). No Starch Press. Kindle Edition.

car = 'lambo' 
print("Is car == 'lambo'? I say true.")
print(car == 'lambo')

print("is the car an audi? I don't think so.")
print(car == 'audi')

print(car == 'cadillac')
print(car == 'toyota')
print(car == 'honda')
print(car == 'rock')
print(car == 'LAMBO')
print(car == 'Lambo')
print(car == 'lamb')
print(car == 'lambo')


2<1
print(car == 'LAMBO'.lower())  #true 

2<1 or 1<100
# car == 'lambo'

if car == 'lambo':
    print("ski got his lambo")

if car != 'audi':
    print("this is a lambo!")     # this is your first if/else loop
else:
    print("I thought it was an audi.")

print(car == 'audi')

age = 19

if age >= 18:                       # note the colon 
    print("you are over 18")
    print("stop")


age =17
if age < 18:
    print("you can't buy cigarettes")
    print("and you should probably stay in school.")
else: 
    print("no")

age = 12

if age <4:
    price = 0
elif age <18:
    price = 25
else:
    price = 40

print(f"your cost is ${price}.") 

# After the price is set by the if-elif-else chain, a separate unindented print() call uses this value to display a message reporting the person’s admission price.

x == 10000

if x < 10:
    y = 0
elif x > 10 and x < 100:     # good if-elif-else chain 
    y = 1
elif x > 101 or x == 10000:
    y = 2
else:            # you actually proved you can skip else block by accident 
    y = 3        # ELSE is viewed as 'catch all' stmt 

print(f"you are {y} years old.")

# 5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 84). No Starch Press. Kindle Edition. 

alien_color = ['green', 'yellow', 'red']

# Write an if statement to test whether the alien’s color is green. If it is, print a message that the player just earned 5 points.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 84). No Starch Press. Kindle Edition. 

if 'green' in alien_color:
    print("\nyou have earned 5 points!")

if 'green' in alien_color:
    print('yes')
elif 'black' in alien_color:
    print('no')

if 'black' in alien_color:
    print('noo')

for color in alien_color:
    if color != 'green':      # if-elif loop inside a for loop
        print('not green')    # no way you could have done this at hunter 
    elif color == 'green':
        print('green')

# green
# not green
# not green

# If the alien’s color isn’t green, print a statement that the player just earned 10 points.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 84). No Starch Press. Kindle Edition. 

if 'green' != alien_color:  # you can use logic with strings! 
    print('\nyou have earned 10 points!')

# Write one version of this program that runs the if block and another that runs the else block.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 84). No Starch Press. Kindle Edition. 

for color in alien_color:
    if color != 'green' and color != 'red':
        print("\nnot green or red")
    else:                   # note the colon after else. 'catch all' stmt
        print("\nyellow")

for color in alien_color:
    if color == 'green':
        print('true')
    else:
        print('false')

for color in alien_color:
    if color == 'green' or color == 'yellow':
        print('true')
    else:
        print('false')

# 5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elif-else chain.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 85). No Starch Press. Kindle Edition. 

# If the alien is green, print a message that the player earned 5 points.

# If the alien is yellow, print a message that the player earned 10 points.

# If the alien is red, print a message that the player earned 15 points.

# Write three versions of this program, making sure each message is printed for the appropriate color alien.

color == 'green'

if 'green' in alien_color:
    print("\n5 points!")
elif 'yellow' in alien_color:   # loop ends at first stmt
    print("\n10 points!")
elif 'red' in alien_color:
    print("\n15 points!")
                                # how to test multiple conditions 
if 'green' in alien_color:
    print("\n5 points!")
if 'yellow' in alien_color: # here a msg is printed for each color
    print("\n10 points!")
if 'red' in alien_color:
    print("\n15 points!")

# 5-6. Stages of Life: Write an if-elif-else chain that determines a person’s stage of life. Set a value for the variable age, and then:

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 85). No Starch Press. Kindle Edition.

# If the person is less than 2 years old, print a message that the person is a baby.

# If the person is at least 2 years old but less than 4, print a message that the person is a toddler.

# If the person is at least 4 years old but less than 13, print a message that the person is a kid.

age = 1
if age < 2:
    print("baby")
age = 3
if age > 2 and age < 4:
    print("toddler")
age = 7
if age > 4 and age < 13:
    print("kid")

# 5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 85). No Starch Press. Kindle Edition. 

fruits = ['blueberries', 'plums', 'raspberries', 'apples', 'bananas']

# Make a list of your three favorite fruits and call it favorite_fruits.

# Write five if statements. Each should check whether a certain kind of fruit is in your list. If the fruit is in your list, the if block should print a statement, such as You really like bananas!

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 85). No Starch Press. Kindle Edition. 

for fruit in fruits:
    if fruit == 'blueberries':
        print(f"you really like {fruit.upper()}!")
    if fruit == "plums":
        print(f"\nyou really like {fruit.upper()}!!")
    if fruit == 'raspberries':
        print(f"\nyou really like {fruit.upper()}!!!")
    if fruit == 'apples':
        print(f"\nyou really like {fruit.upper()}!!!!")
    if fruit == 'bananas':
        print(f"\nyou really like {fruit.upper()}!!!!!")


alpha = ['a', 'b', 'c', 'd']
if 'a' in alpha:
    print('a')
if 'b' in alpha:
    print('b')
if 'c' in alpha:
    print('c')
if 'd' in alpha:
    print('d')


requested_toppings = requested_topping

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for topping in requested_toppings:
    print(f"Adding {topping}.") # f makes the {topping} set print

print("\nFinished making your pizza!")

for topping in requested_toppings:
    if topping == 'green peppers':
        print("Sorry we don't have green peppers.") # no f == no set printing
    else:
        print(f"Adding {topping}!") # put the f ! 

print("\nFinished making your pizza!")


requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza")
else:
    print("Are you sure you don't want toppings?")  

# if we had a non-empty set, 'Adding {requested_topping}' is the output

available_toppings = ['mushrooms', 'olives', 'green peppers', 
                        'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else: 
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished your pizza!")

# i want to load data and use these loops.
# how does creating lists and loops help drive innovation?

