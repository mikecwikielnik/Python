 # CHAPTER 9 CLASSES
 
 
# Creating the Dog Class

from email import message_from_binary_file
from itertools import count

from numpy import empty, number
from soupsieve import match


class Dog:
    """A simple attempt to model a dog. """
    
    def __init__(self, name, age):
        """Initialize name and age attributes. """
        self.name = name
        self.age = age 
        
        
    def sit(self):
        """Simulate a dog siting in response to a command. """
        print(f"{self.name} is now sitting. ")
        
        
    def roll_over(self):
        """Simulate rolling over in response to a command. """
        print(f"{self.name} rolled over! ")
        

# Making an instance from a Class 

my_dog = Dog('Willie', 6)       # Creating the dog 

print(f"My dog's name is {my_dog.name}.")       # Basic things you can do with the attributes. 
print(f"My dog is {my_dog.age} years old. ")

# Accessing attributes 

my_dog.name     # dot notation is used alot in python 

my_dog.age      # Python looks at my_dog and sees two attributes (name, age) and yields the respective output. 

# Calling methods 

my_dog.sit()        # very cool output! 

my_dog.roll_over()      # another very cool output! 

# Creating multiple instances 

your_dog = Dog('Lucy', 3)       # you should be able to do 46- 54 with next to zero help. Very easy. 

your_dog.sit()

print(f"{your_dog.name} is a good girl! ")

print(f"My {your_dog.name} baby is {your_dog.age} years old! ")

your_dog.roll_over()


# 9-1. Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. 

# Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.

# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 162). No Starch Press. Kindle Edition. 

class Restaurant:
    
    def __init__(self, name, type):
        """Attempt at a creating a class named Restaurant. """
        
        self.name = name
        self.type = type 
        
    def restaurant_name(self):
        """Restaurant name method. """        
        print(f"This is my {self.name}! ")
        
    def cuisine_type(self):
        """Cuisine type method. """
        print(f"Our restaurant has {self.type} food. ")
        
    def open_status(self):
        """Method to say if the restaurant is open. """
        print(f"{self.name} is open til 10 pm. ")
        
my_restaurant = Restaurant('Filippo Ristorante', 'Italian')

my_restaurant.open_status()

my_restaurant.restaurant_name()

my_restaurant.cuisine_type()

# 9-2. Three Restaurants: Start with your class from Exercise 9-1. 

# Create three different instances from the class, and call describe_restaurant() for each instance.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 162). No Starch Press. Kindle Edition. 

your_restaurant= Restaurant('McDonalds', 'American')

your_restaurant.cuisine_type()

your_restaurant.open_status()

your_restaurant.restaurant_name()

# 9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. 

# Make a method called describe_user() that prints a summary of the user’s information. 

# Make another method called greet_user() that prints a personalized greeting to the user. 

# Create several instances representing different users, and call both methods for each user.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 162). No Starch Press. Kindle Edition. 

class User:
    
    def __init__(self, first, last, hair, eye):
        """Creating a user profile. """
        self.first = first
        self.last = last
        self.hair = hair
        self.eye = eye
        
    def describe_user(self):
        """Describe user. """
        print(f"This is {self.first}. \n")
        print(f"{self.first.title()} has {self.hair} hair. \n")
        print(f"{self.first} {self.last}. \n")
        print(f"{self.first} has {self.eye} eye color. \n")
        
    def greet_user(self):
        """Greet user. """
        print(f"HI! {self.first} {self.last} who has {self.hair} hair and {self.eye} eyes. \n")

friend_1 = User('Michael', 'Levenson', 'brown', 'blue')

friend_1.describe_user()

friend_1.greet_user()

friend_2 = User('Santa', 'Claus', 'white', 'green')

friend_2.describe_user()

friend_2.greet_user()

# Working with Classes and Instances 

class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())


# Setting a default value for an attribute 

class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0       # line 202, v important! self is my_new_car 

    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())      
my_new_car.read_odometer()


# Modifying attribute values 

# you can either change an attributes value 1) inside the instance 2) set the value through a method 3) increment the value in the method 

# Modifying an attribute's value directly 

my_new_car.odometer_reading = 23        # dot notation see __init__ function 

my_new_car.read_odometer()

# Modifying an Attribute's Value through a Method 

class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update needs an input 
        """Set the odometer reading to the given value. """
        self.odometer_reading = mileage
    
    
my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())  
my_new_car.update_odometer(23)    
my_new_car.read_odometer()


# another example 

class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update_odometer needs an input 
        """
        Set the odometer reading to the given value.
        Reject the chanage if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer! ")

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())  
my_new_car.update_odometer(23)    
my_new_car.read_odometer()

my_new_car.update_odometer(4)

my_new_car.update_odometer(100)

my_new_car.update_odometer(50)

# Incrementing an Attributes value through a method 


class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update_odometer needs an input 
        """
        Set the odometer reading to the given value.
        Reject the chanage if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer! ")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading. """
        self.odometer_reading += miles 
        
my_used_car = Car('Honda', 'Accord', 2004)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# 9-4. Number Served: Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. 

# Print the number of customers the restaurant has served, and then change this value and print it again. 

# Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again. 

# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 167). No Starch Press. Kindle Edition. 



class Restaurant:
    
    def __init__(self, name, type):
        """Attempt at a creating a class named Restaurant. """
        self.name = name
        self.type = type 
        self.number_served = 0 
        
    def restaurant_name(self):
        """Restaurant name method. """        
        print(f"This is my {self.name}! ")
        
    def cuisine_type(self):
        """Cuisine type method. """
        print(f"Our restaurant has {self.type} food. ")
        
    def open_status(self):
        """Method to say if the restaurant is open. """
        print(f"{self.name} is open til 10 pm. ")
        
    def customers(self):
        """Method to say how many customers were served. """
        print(f"We have served {self.number_served} tonight. ")
        
    def set_number_served(self, served):
        """Setting the min number needed to serve to break even. """
        self.number_served = served 
        
    def more_customers(self, more):
        """We have more guests coming. """
        self.number_served += more
        
        
        
my_restaurant = Restaurant('Filippo Ristorante', 'Italian')

my_restaurant.open_status()

my_restaurant.restaurant_name()

my_restaurant.cuisine_type()

my_restaurant.customers()

my_restaurant.number_served = 75 

my_restaurant.customers()

your_restaurant = Restaurant('Arbys', 'Sandwiches')

your_restaurant.set_number_served(150)

your_restaurant.customers()

your_restaurant.more_customers(500)

your_restaurant.customers()

# 9-5. Login Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 162). 

# Write a method called increment_login_attempts() that increments the value of login_attempts by 1. 

# Write another method called reset_login_attempts() that resets the value of login_attempts to 0. Make an instance of the User class and call increment_login_attempts() several times. 

# Print the value of login_attempts to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure it was reset to 0.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 167). No Starch Press. Kindle Edition. 


class User:
    
    def __init__(self, first, last, hair, eye):
        """Creating a user profile. """
        self.first = first
        self.last = last
        self.hair = hair
        self.eye = eye
        self.login_attempts = 0
        
    def describe_user(self):
        """Describe user. """
        print(f"This is {self.first}. \n")
        print(f"{self.first.title()} has {self.hair} hair. \n")
        print(f"{self.first} {self.last}. \n")
        print(f"{self.first} has {self.eye} eye color. \n")
        
    def greet_user(self):
        """Greet user. """
        print(f"HI! {self.first} {self.last} who has {self.hair} hair and {self.eye} eyes. \n")

    def increment_login_attempts(self):
        """Increment login attempmts. """
        self.login_attempts += 1
        print(f"{self.login_attempts}")
    
    def reset_login_attempts(self):
        """Resetting login attempts. """
        self.login_attempts = 0 
        print(f"{self.login_attempts}")

friend_1 = User('Michael', 'Levenson', 'brown', 'blue')

friend_1.describe_user()

friend_1.greet_user()

friend_2 = User('Santa', 'Claus', 'white', 'green')

friend_2.describe_user()

friend_2.greet_user()

friend_1.increment_login_attempts()

friend_1.reset_login_attempts()

friend_1.login_attempts     # this is interesting because this is how you call that the login attempts went straight to zero. You can prove it by running increment again. 

friend_1.hair       # dot notation used to call specific items in our original __init__ method 

# Inheritance 

# You can inherit one class from another. 

# Now, you have the parent class and child class. Child class can have any or all of the attributes and methods of its parents class- can also define new attributes and methods of its own. 


class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update_odometer needs an input 
        """
        Set the odometer reading to the given value.
        Reject the chanage if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer! ")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. """
    
    def __init__(self, make, model, year):
        """Initialize attributes of a parent class. """
        super().__init__(make, model, year)     # Car is the superclass and ElectricCar is subclass 

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())


# Defining attributes 


class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update_odometer needs an input 
        """
        Set the odometer reading to the given value.
        Reject the chanage if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer! ")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. """
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kwh battery. ")
 

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
        
my_tesla.describe_battery()

# Overriding Methods from the Parent Class

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. """
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery_size = 75
        
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kwh battery. ")
 
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks. """
        print("This car doesn't need a gas tank! ")
    
# Instances as Attributes 

class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update_odometer needs an input 
        """
        Set the odometer reading to the given value.
        Reject the chanage if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer! ")
            
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes. """
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kwh battery. ")
        
    def get_range(self):
        """Print a statement about the range this battery provides. """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315 
        print(f"This car can go about {range} miles on full charge. ")
    

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. """
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()        # you need to study this further because it provides the ability to use methods in the Battery class. 
        
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kwh battery. ")
 

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
        
my_tesla.battery.describe_battery()
    
my_tesla.battery.get_range()

# 9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. 

# Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of the class will work; 

# just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. 

# Create an instance of IceCreamStand, and call this method.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 174). No Starch Press. Kindle Edition. 

class Restaurant:
    
    def __init__(self, name, type):
        """Attempt at a creating a class named Restaurant. """
        self.name = name
        self.type = type 
        self.number_served = 0 
        
    def restaurant_name(self):
        """Restaurant name method. """        
        print(f"This is my {self.name}! ")
        
    def cuisine_type(self):
        """Cuisine type method. """
        print(f"Our restaurant has {self.type} food. ")
        
    def open_status(self):
        """Method to say if the restaurant is open. """
        print(f"{self.name} is open til 10 pm. ")
        
    def customers(self):
        """Method to say how many customers were served. """
        print(f"We have served {self.number_served} tonight. ")
        
    def set_number_served(self, served):
        """Setting the min number needed to serve to break even. """
        self.number_served = served 
        
    def more_customers(self, more):
        """We have more guests coming. """
        self.number_served += more


class IceCreamStand(Restaurant):
    """An attempt at inheriting the Restaurant class. """
    
    def __init__(self, name, type):
        """
        Initializing attributes from parent class.
        Then adding a new attribute flavors 
        """
        super().__init__(name, type)
        self.flavors = 2
        
    def flavors_method(self):
        """Print the ice cream flavors. """
        print(f"We have {self.flavors} flavors: vanilla and chocolate. ")
        
my_restaurant = IceCreamStand('Filippo Ristorante', 'Italian')      # Remember to use the class with the methods you want. Restaurant does not give you flavors but IceCreamStand does. 

my_restaurant.flavors_method()


# 9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162) or Exercise 9-5 (page 167). 

# Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. 

# Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 174). No Starch Press. Kindle Edition. 


class User:
    
    def __init__(self, first, last, hair, eye):
        """Creating a user profile. """
        self.first = first
        self.last = last
        self.hair = hair
        self.eye = eye
        self.login_attempts = 0
        
    def describe_user(self):
        """Describe user. """
        print(f"This is {self.first}. \n")
        print(f"{self.first.title()} has {self.hair} hair. \n")
        print(f"{self.first} {self.last}. \n")
        print(f"{self.first} has {self.eye} eye color. \n")
        
    def greet_user(self):
        """Greet user. """
        print(f"HI! {self.first} {self.last} who has {self.hair} hair and {self.eye} eyes. \n")

    def increment_login_attempts(self):
        """Increment login attempmts. """
        self.login_attempts += 1
        print(f"{self.login_attempts}")
    
    def reset_login_attempts(self):
        """Resetting login attempts. """
        self.login_attempts = 0 
        print(f"{self.login_attempts}")

class Admin(User):
    """Attempt to show the permissions of the user. """
    
    def __init__(self, first, last, hair, eye):
        """
        Initializing attributes of parent class.
        Then adding new attributes that shows permissions. 
        """
        super().__init__(first, last, hair, eye)
    
    def show_permissions(self, item_1, item_2, item_3):
        """Attempt to show permissions of user"""
        self.item_1 = item_1
        self.item_2 = item_2
        self.item_3 = item_3
        print(f"{self.first} can {item_1}, {item_2}, {item_3} all of these records.")
        

friend_1 = Admin('Michael', 'Levenson', 'brown', 'blue')

friend_1.describe_user()        # Notice here how you were able to call User methods via the class Admin. 

friend_1.greet_user()

friend_1.show_permissions('add', 'delete', 'edit')

friend_3 = Admin('Texas', 'Chainsaw', 'black', 'red')

friend_3.greet_user()

friend_3.show_permissions('view', 'print', 'export to pdf')

# 9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. 

# Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. 

# Create a new instance of Admin and use your method to show its privileges.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 174). No Starch Press. Kindle Edition. 


class Privileges(User):
    """
    Attempt to write another class. 
    """
    
    def __init__(self, first, last, hair, eye):
        """
        Initializing attributes from the parent class Admin. 
        """
        super().__init__(first, last, hair, eye)
        self.priv_1 = 3
        
    def show_privileges(self):
        """Show the number of privileges a user has. """
        print(f"This user has {self.priv_1}.")
        
friend_3 = Privileges('Texas', 'Chainsaw', 'black', 'red')

friend_3.greet_user()

friend_3.show_privileges()


# 9-9. Battery Upgrade: Use the final version of electric_car.py from this section. Add a method to the Battery class called upgrade_battery(). 

# This method should check the battery size and set the capacity to 100 if it isn’t already. 

# Make an electric car with a default battery size, call get_range() once, and then call get_range() a second time after upgrading the battery.

# You should see an increase in the car’s range.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 174). No Starch Press. Kindle Edition. 


class Car:
    """A simple attempt to represent a car. """
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car. """
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0      
        
    def get_descriptive_name(self):
        """Return a neatly descriptive formatted name. """
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage. """
        print(f"This car has {self.odometer_reading} miles on it") 

    def update_odometer(self, mileage):     # update_odometer needs an input 
        """
        Set the odometer reading to the given value.
        Reject the chanage if it attempts to roll the odometer back. 
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else: 
            print("You can't roll back an odometer! ")
            
class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes. """
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kwh battery. ")
        
    def get_range(self):
        """Print a statement about the range this battery provides. """
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315 
        print(f"This car can go about {range} miles on full charge. ")
    
    def upgrade_battery(self):
        """Attempt to create a method to check the battery life. """
        if self.battery_size:
            self.battery_size += 25         # Increase in the question gave you a hint about this increment in battery size. 
            print(f"The battery size is {self.battery_size}. ")
        else:
            print(f"The battery size is {self.battery_size}. ")
    

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles. """
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class. 
        Then initialize attributes specific to an electric car. 
        """
        super().__init__(make, model, year)
        self.battery = Battery()        # you need to study this further because it provides the ability to use methods in the Battery class. 
        
    def describe_battery(self):
        """Print a statement describing the battery size. """
        print(f"This car has a {self.battery_size}-kwh battery. ")
 

my_tesla = Battery()

my_tesla.describe_battery()

my_tesla.get_range()

my_tesla.upgrade_battery()

my_tesla.describe_battery()

my_tesla.get_range()


# Importing Classes 

# import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


# Storing multiple classes in a module 

# """A set of classes used to represent gas and electric cars. """

# from car import Car, ElectricCar

# my_beetle = Car('volkswagen', 'beetle', 2019)
# print(my_beetle.get_descriptive_name())


# my_honda = ElectricCar('honda', 'accord', 2022)
# print(my_honda.get_descriptive_name())


# # importing entire module  

# import car

# my_cadillac = car.Car('cadillac', 'luxury sedan', 2022)
# my_cadillac.get_descriptive_name()

# my_toyota = car.ElectricCar('toyota', 'prius', 2021)
# print(my_toyota.get_descriptive_name())

# Using Aliases

# import ElectricCar as EC          # import pamdas as pd
# my_tesla = EC('tesla', 'roadster', 2019)


### Questions 9-10, 9-11, 9-12 are their own files. 

# The Python Standar Library 

from random import choices, randint, random

from random import choice

players = ['bergeron', 'marchand', 'pastrnak', 'mcdavid', 'crosby']

first_up = choice(players)

first_up


# 9-13. Dice: Make a class Die with one attribute called sides, which has a default value of 6. 

# Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and roll it 10 times. Make a 10-sided die and a 20-sided die. 

# Roll each die 10 times.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 181). No Starch Press. Kindle Edition. 


class Die:
    """An attempt to make a 6 sided die. """
    
    def __init__(self, default = 6):
        """
        Initialize dice attributes. 
        """
        self.default = default
        
    def roll_dice(self):
        """Prints number between 1, 6 for a six sided die. """
        self.num = randint(1,6)
        print(f"this die has rolled a {self.num}. ")
        
    def die_loop(self):
        """
        A loop to print the 6 sided die, 10 times. 
        It will be a different die than roll_dice() if you keep the loop in this method. 
        It will be the same die as roll_dice() if you comment the loop. 
        """
        x = 0
        while x < 11:
            self.num = randint(1,6)
            print(f"This die is a {self.num}. ")
            x += 1
        else:
            print(f"all done. ")
        
die_a = Die()

die_a.roll_dice()

die_a.die_loop()

class Die_B: 
    """An attempt to make a die of any size. """
    
    def __init__(self):
        """Initialize attributes. """
        self.die = 0
        
    def roll_dice(self):
        """Prints any number sided die. """
        self.die = randint(1,100)
        print(f"This die has {self.die} sides. ")
        
    def die_loop(self):
        """Print the outcome ten times. """
        x = 0 
        while x < 11:
            self.die = randint(1,20)
            print(f"This die has rolled a {self.die}. ")
            x += 1
        else:
            print("All done. ")

die_b = Die_B()

die_b.roll_dice()

die_b.die_loop()



# 9-14. Lottery: Make a list or tuple containing a series of 10 numbers and five letters. 

# Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 181). No Starch Press. Kindle Edition. 



class Lottery:
    
    def __init__(self):
        """Initializing inputs. """
        # you have proved you don't need anything but perhaps this method def __init__(self):
        
    def lottery_ticket(self):
        """Print a lottery ticket. """
        list = ['a', 'b', 'c', 'd', 'e']
        x = 0 
        while x < 1:
            a = choice(list)
            b = choice(list)
            c = randint(0,9)
            d = randint(0,9)
            print(f"These is the winning ticket: {a} {b} {c} {d}. ")
            x += 1
        else:
            print("All done. ")



lottery_a = Lottery()

lottery_a.lottery_ticket()


# 9-15. Lottery Analysis: You can use a loop to see how hard it might be to win the kind of lottery you just modeled. 

# Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. 

# Print a message reporting how many times the loop had to run to give you a winning ticket.

# Matthes, Eric. Python Crash Course, 2nd Edition (p. 181). No Starch Press. Kindle Edition. 

from random import choice, randint, random


list_2 = ['a', 'b']
x = 0
empty_list = []

while x < 100:
    letter = choice(list_2)
    num = randint(1,2)
    empty_list.append(letter)
    empty_list.append(num)
    if empty_list == ['a', 1]:
        print("Match! ")
        break
    else:
        empty_list = []
        print("We did not have a match. ")
    x +=1
    
print(f"It took {x+1} loops ")
    
print(empty_list)
