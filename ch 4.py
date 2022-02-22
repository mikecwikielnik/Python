cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

len(cars)
print(cars[100]) # index will be out of range


# start of chapter 4

# FOR LOOPS 

magicians = ['alice', 'david', 'carolina']  # for every magician in the list of magicians, 
for magician in magicians:                  # print the magician's name
    print(magician)

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:                  
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")

# the last line wont be indented and will just be ran once

magicians = ['alice', 'david', 'carolina'] 
for magician in magicians:                 
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}!\n")
print(f"Thanks for coming out tonight!")

# pizza loop

pizza = ['la vera', 'dominos', 'vezza']
for za in pizza:       # here you can use za in pizza 
    print(f"{za.title()} is the best pizza!")
    print(f"I hate that {za.title()}!\n")
print("I just love pizza!")


# animal loop

animal = ['dog', 'cat', 'monkey']
for pet in animal:
    print(f"{pet.title()} would be a great pet!")
print(f"Any of these animals would make a great pet!")


for value in range(1,10000):
    print(value-100)

numbers = list(range(1,7)) # python has an 'off one' error. 
print(numbers)

even_numbers = list(range(0,11,2)) # range fn starts with 0 and adds 2 to it repeatedly until 
print(even_numbers)                # 11 is reached or passed. 


squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares)

squares = []     # a more succinct chunk of code than above ^ 
for value in range(1,11):
    squares.append(value**2) # here is where we omit lines from previous code 

print(squares)

# list comprehension

squares=[value**2 for value in range (1,11)]
print(squares)

# try it yourself 

# 4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20, inclusive.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 

for value in range(1,21): # two things 1) the off-one error
    print(value)            # the for loop needs that indent to do the loop

# 4-4. One Million: Make a list of the numbers from one to one million, and then use a for loop to print the numbers. (If the output is taking too long, stop it by pressing CTRL-C or by closing the output window.)

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 

## at the time of writing, we decided that one million is too high a number to print
## we tried 10,000 and other limits 

for value in range(1,10000):
    print(value)

# 4-5. Summing a Million: Make a list of the numbers from one to one million, and then use min() and max() to make sure your list actually starts at one and ends at one million. Also, use the sum() function to see how quickly Python can add a million numbers.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 

milli = []
for value in range(1,1000001): # don't forget that damn semi-colon
    milli.append(value)         # also don't forget the off-one! 
sum(milli)                      ## Note: 1) you need the colon to induce the loop. 2) In list comprehension on the left and below, you don't.
min(milli)                      ## For ex, here, you could do the whole loop inside milli and the summary stats outside the loop like u would. 
max(milli)

# 4-6. Odd Numbers: Use the third argument of the range() function to make a list of the odd numbers from 1 to 20. Use a for loop to print each number.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 



for value in range(1,22,2):
    print(value)

# 4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to print the numbers in your list.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 

for value in range(3,33,3):
    print(value)


# 4-8. Cubes: A number raised to the third power is called a cube. For example, the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that is, the cube of each integer from 1 through 10), and use a for loop to print out the value of each cube.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 


for value in range(1,10):
    print(value**3)


# 4-9. Cube Comprehension: Use a list comprehension to generate a list of the first 10 cubes.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 60). No Starch Press. Kindle Edition. 

squares=[value**2 for value in range (1,11)]
print(squares)


cubes=[value**3 for value in range(1,10)]
print(cubes)

cubes[0]

# slicing lists

players=['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])


print(players[1:4]) #off one error

print(players[2:])

print(players[-3:])

# Looping through a list

for player in players[:3]:
    print(player.title())


my_foods=['pizza', 'falafel', 'cake']
friend_foods= my_foods[:]

print("My favorite foods are:")  # make sure your variables are CONSISTENT !! 
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friends favorite foods are:")
print(friend_foods)

# this doesn't work

friend_foods = my_foods

print (friend_foods)
print (my_foods)


# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 65). No Starch Press. Kindle Edition. 


# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 65). No Starch Press. Kindle Edition. 

print("The first three items in the list are:")
print(players[:4])

print("Three items from the middle of the list are:")
print(players[1:4])

# look at the place in the brackets

print("The last three items in the list are:")
print(players[:-1])

print("The last three items in the list are:")
print(players[-1:])




# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 65). No Starch Press. Kindle Edition. 

# Add a new pizza to the original list.

# Add a different pizza to the list friend_pizzas.

# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.


pizza = ['la vera', 'dominos', 'vezza']

print(pizza)
pizza

friend_pizza = pizza[:]

print(friend_pizza)
print(pizza)


pizza.append('millys')
friend_pizza.append('little italys')

for za in pizza[:]:   # you are printing ZA not pizza 
    print(za.title())


print("my favorite pizzas are:")
for za in pizza[:]:
    print(za.title())

print("My friends favorite pizzas are:")
for za in friend_pizza[:]:
    print(za.title())

for za in pizza[:3]:   
    print(za.title())


print(za)  # here za is whatever the loop printed za as last 


# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 65). No Starch Press. Kindle Edition. 

for food1 in my_foods[:]:
    print(food1.title())

for food2 in friend_foods[-1:]:
    print(food2.upper())

# Defining a Tuple A tuple looks just like a list except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 66). No Starch Press. Kindle Edition. 

dimensions=(200, 50)

print(dimensions[0])
print(dimensions[1])

dimensions[0]= 250

for dimension in dimensions:
    print(dimension)


print("original dimensions:")
for dimension in dimensions:
    print(dimension)

print("\nModified dimensions")
dimensions= (400, 100)
for dimension in dimensions: 
    print(dimension)

# 4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 68). No Starch Press. Kindle Edition. 

buffets= ('eggs', 'bacon', 'sausage', 'potatoes')

# Use a for loop to print each food the restaurant offers.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 68). No Starch Press. Kindle Edition. 

for fets in buffets:  # don't need the bracket before the semi colon in tuples. 
    print(fets)

# Try to modify one of the items, and make sure that Python rejects the change.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 68). No Starch Press. Kindle Edition. 

buffets[0]= 'toasts'  # planned rejection

# The restaurant changes its menu, replacing two of the items with different foods. Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 68). No Starch Press. Kindle Edition. 


buffets= ('eggs', 'bacon', 'toast', 'cholula')
print("\n New Menu")

for fets in buffets:
    print(fets)
