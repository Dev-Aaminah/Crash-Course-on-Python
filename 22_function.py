def hello_func():
    pass

print(hello_func) #we're not calling function here, as haven't used ()
print(hello_func())

def sum_values():
    first = int(input("Enter first number: "))
    second = int(input("Enter second number: "))
    print(sum([first, second]))
sum_values() 

# Return
def hello_func():
    return "Hello Everyone!"
print(hello_func())
print(hello_func().upper())

# parameters
def hello(greeting, name='You'): # here 'you' is default value. and will be used if no value is provided.
    return "{},{}.".format(greeting, name)

print(hello('Hi', 'Aaminah'))

# In Python, *args and **kwargs are special syntax used in function definitions to handle variable numbers of arguments. They allow you to pass a flexible number of positional and keyword arguments to a function, making the function more versatile.


# <! ----------- *args and **kwargs ----------->
# In Python, *args and **kwargs are special syntax used in function definitions to handle variable numbers of arguments. They allow you to pass a flexible number of positional and keyword arguments to a function, making the function more versatile.

# 1. *args: Handling Variable Positional Arguments
# *args allows a function to accept any number of positional arguments.
# It collects all the extra positional arguments into a tuple, so you can iterate over them or use them as needed.
# Example of *args:
def greet(*args):
    for name in args:
        print(f'Hello, {name}!')
greet("Aaminah", "Atqa", "Anisha")

# 2. **kwargs: Handling Variable Keyword Arguments
# **kwargs allows a function to accept any number of keyword arguments (arguments passed with a key-value pair, like key=value).
# It collects these extra keyword arguments into a dictionary, so you can access them by key.
# Example of **kwargs:
def greeting(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
greeting(name='Aaminah', city='Rawalpindi')