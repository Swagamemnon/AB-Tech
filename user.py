# define class user
class User:
    """creates user profile with set attributes"""
    def __init__(self, first_name, last_name, age, occupation):
        """Initialize user attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.occupation = occupation

   # create method to describe attributes of user
    def describe_user(self):
        """describes users attributes"""
        # need to figure out how to split this line
        print(
            f'''\n{self.first_name} {self.last_name} is {self.age} years old and
            works as a {self.occupation}.'''
            )
        
    #create method to greet user 
    def greet_user(self):
        """Composes a greeting to user"""
        print(f"Hey {self.first_name}, how is your day going?")

# create 3 users
gabe = User('Gabe', 'Matza', 33, 'unemployed bum')
hannah = User('Hannah', 'Watkins', 28, 'contract utility forester')
norah = User('Norah', 'Decker', 17, 'high school student')

# several instances of users
print(f"Gabe's last name is {gabe.last_name}.")
print(f"Hannah is {hannah.age} years old.")
print(f"Norah is a {norah.occupation}.")

# call methods on each user
gabe.describe_user()
hannah.describe_user()
norah.describe_user()

gabe.greet_user()
hannah.greet_user()
norah.greet_user()