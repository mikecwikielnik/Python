# 9-11. Imported Admin: Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. 

# Create a separate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 180). No Starch Press. Kindle Edition. 



from user import Privileges

from user import Admin

from my_car import Car

zendaya = Privileges('zendaya', 'cwikielnik', 'brown', 'brown')

zendaya.greet_user()

zendaya.show_privileges()

rolls_royce = Car('Rolls Royce', 'Phantom', 2022)

rolls_royce.read_odometer()


# 9-12. Multiple Modules: Store the User class in one module, and store the Privileges and Admin classes in a separate module. 

# In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 180). No Starch Press. Kindle Edition. 

admin_001 = Admin('first', 'last', 'brown', 'brown')

admin_001.show_permissions('cut', 'copy', 'paste')