class Employee:
    """Collect first and last name and annual salary and store as attributes"""
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self, increase=5000):
        """Adds $5,000 to annual salary but also accepts a different ammount."""
        self.salary = self.salary + increase
    
    def show_employee(self):
        """prints information about employees."""
        print(self.first, self.last, self.salary)

noah = Employee('noah', 'decker', 50000)
noah.show_employee()
noah.give_raise()
noah.show_employee()
noah.give_raise(increase=10000)
noah.show_employee()