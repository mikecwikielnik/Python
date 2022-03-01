# 9-10. Imported Restaurant: Using your latest Restaurant class, store it in a module. 

# Make a separate file that imports Restaurant. Make a Restaurant instance, and call one of Restaurant’s methods to show that the import statement is working properly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 180). No Starch Press. Kindle Edition. 

import Restaurant

my_kowloons = Restaurant('Kowloons', 'chinese')

my_kowloons.open_status()

my_kowloons.set_number_served(150)

my_kowloons.customers()