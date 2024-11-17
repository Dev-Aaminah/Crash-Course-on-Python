# Python Object-Oriented Programming

class Employee:
    pass

# class is a blueprint for creating instances
# each unique employee that we create is an instance of that class


empoyee1 = Employee() # instance of class employee
empoyee2 = Employee() # instance of class employee

# manually creating employees
empoyee1.first= 'Saba'
empoyee1.last='Emaad'
print(empoyee1.first)

empoyee2.first= 'Test'
empoyee2.last='User'
empoyee2.salary=32000
empoyee2.email='tu@xyz.com'

print(empoyee2.email)

# creating employees using class method
class Employees:
    def __init__(self, firstname, lastname, pay):
        self.firstname = firstname
        self.lastname = lastname
        self.pay= pay
        self.email = firstname+'.'+lastname+'@company.com'
        
    def fullname(self): # self is mandatory
        return '{} {}'.format(self.firstname, self.lastname)
        
emp1= Employees('test','user',32000)
emp2 = Employees('new', 'user', 25000)
print(emp1.email)
print(emp1.fullname())
print(emp2.fullname())

# Exercise to show team
class Team:
    def __init__(self, name):
        self.name = name
        self.email = name +'.'+'@xyz.com'
        
    def show_team(self):
        return '{} {}'.format(self.name, self.email)
    
new_emp1 = Team('Hamna')
print(Team.show_team(new_emp1))

# Bark
class Dog():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        
    def bark(self):
        return f'{self.name} says: woo woo'

puppy = Dog('bunty', 'australian')
print(puppy.bark())