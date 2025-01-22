# Special methods are also called magic methods or dunder methods in Python.
# "Dunder" stands for "double underscore," as these methods begin and end with double underscores.

# __init__ is the constructor method in Python.
# It is automatically called when an object is created, used to initialize the object's attributes.
# Example: Assigning initial values to instance attributes.

# __repr__ provides an unambiguous string representation of an object.
# This is mainly used for debugging and development.
# The returned string should ideally include enough detail to recreate the object.

# __str__ provides a human-readable string representation of an object.
# This is used when you want a friendly description of the object (e.g., in print statements).

# Example code to demonstrate these special methods:

class Book:
    def __init__(self, title, author, pages):
        # __init__ initializes instance attributes when an object is created
        self.title = title
        self.author = author
        self.pages = pages

    def __repr__(self):
        # __repr__ provides an unambiguous string representation
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    def __str__(self):
        # __str__ provides a readable representation of the object
        return f"'{self.title}' by {self.author}, {self.pages} pages"

# Creating an object of the Book class
book = Book("1984", "George Orwell", 328)

# Demonstrating __repr__
print(repr(book))  # Output: Book(title='1984', author='George Orwell', pages=328)

# Demonstrating __str__
print(str(book))   # Output: '1984' by George Orwell, 328 pages

# When you use print(), __str__ is automatically called.
print(book)        # Output: '1984' by George Orwell, 328 pages

# When you use the object in a REPL or debugger, __repr__ is used.
book  # Output: Book(title='1984', author='George Orwell', pages=328)

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def email(self):
        return '{}{}@gmail.com'.format(self.first,self.last)
    
    def __repr__(self):
        return "Employee('{}','{}','60000').".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email())
    
    def __add__(self, other):
        return self.pay + other.pay
emp1 = Employee('Corey', 'Schafer', 50000)
print(emp1)

emp2 = Employee('Steven', 'Schafer', 60000)
print(emp2)

print(emp1.__repr__())
print(emp1.__str__())
# Special method for arithematic
print(1+2)
print('a'+'b')

print(int.__add__(1,2))
print(str.__add__('a','b'))

print(emp1+emp2)

print(len('Aaminah'))
print('Aaminah'.__len__())