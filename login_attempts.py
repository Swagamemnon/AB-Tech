# define class user
class User:
    """creates user profile with set attributes"""
    def __init__(self, first_name, last_name, age, occupation):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation
        self.login_attempts = 0

   # create method to describe attributes of user
    def describe_user(self):
        """describes users attributes"""
        print(
            f'''\n{self.first_name} {self.last_name} is {self.age} years old and
            works as a {self.occupation}.'''
            )
        
    #create method to greet user 
    def greet_user(self):
        """Composes a greeting to user"""
        print(f"Hey {self.first_name}, how is your day going?")

    # create method to increment login attempts
    def increment_login_attempts(self):
        """Add incremental login attempts."""
        self.login_attempts = self.login_attempts + 1
        print(f"You have attempted to login {self.login_attempts} times.")

    # create method to reset login attempts to 0
    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0

# create a user to demonstrate increment logins and reset login methods
noah = User('noah', 'decker', 33, 'forester')
noah.increment_login_attempts()
noah.increment_login_attempts()
noah.increment_login_attempts()
noah.reset_login_attempts()
print(noah.login_attempts)