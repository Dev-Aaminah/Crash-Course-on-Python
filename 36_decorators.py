# ------------- Decorators in python ------------- #
# A decorator is a function that takes another function as input, adds some functionality to it, and returns the modified function.
# Decorators are often used in Python for tasks like logging, access control, memoization, or enforcing rules.

def decorator_function(original_func):
    def wrapper_function():
        return original_func()
    return wrapper_function

def display():
    print('Display func ran')
    
decorated_display = decorator_function(display)

decorated_display()

# which is actually decorator func here?
# display or decorator_function()

# The actual decorator function in this code is decorator_function().
# Here’s why:

# What is a Decorator Function?
# A decorator function is a function that takes another function (like display()) as input, enhances or modifies its behavior, and returns a new function (like wrapper_function()).

def add_greeting(original_func):
    def wrapper_func(*args, **kwargs):
        print("Hello!")
        original_func(*args, **kwargs)  # Call the original function with its arguments
        print("Good Bye!")
    return wrapper_func  # Return the wrapper function itself

@add_greeting  # Decorate the function
# The @add_greeting is a shorthand for say_name = add_greeting(say_name).

def say_name(name):
    print('My name is {}'.format(name))

# Test the decorated function
say_name("Aaminah")

# ///////////////////

def log_execution(original_func):
    def wrapper_func(*args, **kwargs):
        print("Starting execution")
        original_func(*args, **kwargs)
        print("Execution finished!")
    return wrapper_func

@log_execution
def say_name(name):
    print('My name is {}'.format(name))

# Test the decorated function
say_name("Aaminah")