# The @property decorator in Python is used to create a getter method for an attribute while allowing you to access it like a normal attribute (without calling it explicitly as a method).
class Employee:
    # Constructor method to initialize the Employee object
    def __init__(self, first, last, pay):
        self.first = first  # Employee's first name
        self.last = last    # Employee's last name
        self.pay = pay      # Employee's salary/pay
        
    # Property method to return the full name of the employee
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self,name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None
    
    @property
    def email(self):
        return '{}{}@gmail.com'.format(self.first, self.last)
    
    # Special method to provide an unambiguous representation of the object
    # Useful for debugging and logging
    def __repr__(self):
        return "Employee('{}','{}','60000').".format(self.first, self.last, self.pay)
    
    # Special method to provide a readable string representation of the object
    # Used when printing or converting the object to a string
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
    
    # Special method to define custom behavior for the + operator
    # Allows adding the salaries of two Employee objects
    def __add__(self, other):
        return self.pay + other.pay

# Creating an Employee object with first name, last name, and salary
emp1 = Employee('Corey', 'Schafer', 50000)
# Printing the object, which implicitly calls the __str__ method
print("=======PRINTING EMPLOYEE1=======")
print(emp1)
print("=======PRINTING FULLNAME OF EMPLOYEE1=======")
print(emp1.fullname)
emp1.fullname = 'Steve Jobs'
# Creating another Employee object
emp2 = Employee('Steven', 'Schafer', 60000)
# Printing the object, which implicitly calls the __str__ method
print("=======PRINTING EMPLOYEE2=======")
print(emp2)
print("=======PRINTING EMAIL OF EMPLOYEE2=======")
print(emp2.email)

# del emp2.fullname
# print(emp2.fullname)