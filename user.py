# User module

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
        