# CHAPTER 7 WHILE LOOPS 
# NOTE: chapter 7 has the input() function and ATTOW we didn't know how to get it loaded into the visual code studio.


# Start with users that need to be verified, 
# and an empty list to hold confirmed users. 

from re import X

from numpy import empty


unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
# Move each verified user into the list of confirmed users. 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
    
# Display all confirmed users. 
    print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# remmoving all instances of specific values from a list

pets = ['dog', 'cat', 'dog', 'fish', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# using continue in a loop 

current_number = 0

while current_number < 10:
    current_number += 1         # current number plus one.....x = x + 1 
    if current_number % 2 == 0:
        continue 
    
    print(current_number)
    
current_number = 0

while current_number < 50:
    current_number += 5         # adds 5 to zero then print
    print(current_number)
    
    
current_number = 0

while current_number < 50:        
    print(current_number)        # prints zero then adds 5 
    current_number += 5
    
    
    
    
    
# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 127). No Starch Press. Kindle Edition. 

# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 127). No Starch Press. Kindle Edition. 

# After all the sandwiches have been made, print a message listing each sandwich that was made.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 127). No Starch Press. Kindle Edition. 


sandwich_orders = ['pb&j', 'steak & cheese', 'falaffel']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"\ti have made your {finished_sandwich} sandwich. Come get it!\n")
    
    finished_sandwiches.append(finished_sandwich)

print(f"\t These are all the tickets:\n")
print(f"{finished_sandwiches}")     # you can use print(f"{finished_sandwiches[2]}") to print the 2nd element 


# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 127). No Starch Press. Kindle Edition.    

# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 127). No Starch Press. Kindle Edition. 

# Make sure no pastrami sandwiches end up in finished_sandwiches.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 127). No Starch Press. Kindle Edition. 

sandwich_orders = ['pb&j', 'steak & cheese', 'falaffel', 'pastrami', 'roast beast', 'turkey', 'pastrami', 'chicken salad', 'pastrami']
finished_sandwiches = []

while sandwich_orders:
    finished_sandwich = sandwich_orders.pop()
    print(f"\tI have an order for a {finished_sandwich} sandwich.\n")
    finished_sandwiches.append(finished_sandwich)
    
       
print(f"\t These are all the orders:\n")
print(f"{finished_sandwiches}")   

while 'pastrami' in finished_sandwiches:
    finished_sandwiches.remove('pastrami')

print(f"\t Sorry! We were out of pastrami. These are the only sandwiches we can make. \n")
print(f"\t{finished_sandwiches}")




# for fun

x = 0

while x < 10:
    x += 1
    if x % 2 == 0:      # if you have an even number, raise to a 2nd power- else, divide by 2. 
        x**2
    else:
        x/2 


x = 0 
empty_set = []

while x < 10:
    x += 1
    empty_set.append(x)     # start at 0 & an empty set. while x < 10, add one then append the empty set wit x

print(empty_set)
    
x = 0 
empty_set = []

while x <= 10:          # Used in helping you solving GS HackerRank sample test. 
    if x % 2 == 0:
        empty_set.append(x)     # remember to add the plus one, x += 1. the loop will just continue to stay at zero. 
    else:
        x = x - 1
        empty_set.append(x)
    x += 1

print(empty_set)