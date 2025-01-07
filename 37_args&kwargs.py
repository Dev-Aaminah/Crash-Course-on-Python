# *args and **kwargs

def order_pizza(size, *toppings, **details):
    print(f"Ordered a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
    print("\n Details of order:")
    for key, value in details.items():
        print(f" - {key}: {value}")
order_pizza("large", "mushroom", "cheese", "olives","pepperoni", delivery=True, payment_method='Cash On Delivery', Tip=5)

# Create a function sum_numbers(*args) that accepts a variable number of numbers and returns their sum.
def sum_numbers(*args):
    return sum(args)
    
print(sum_numbers(1,5,7,8,100))

# Create a function greet_users(*args) that accepts a variable number of user names and prints a greeting for each one.
def greet_users(*args):
    for member in args:
        print(f"Hello {member}")
        
greet_users("Saba", "Dua", "Esba")

# Create a function student_details(**kwargs) that accepts student information like name, age, and grade as key-value pairs and prints them.
def student_details(**kwargs):
    print("Students info:")
    for key,value in kwargs.items():
        print(f" \t {key}: {value}")
        
student_details(name="Sadia", age=13, grade=9)

# Write a function concatenate_strings(*args) that takes a variable number of string arguments and concatenates them into one string.
def concatenate_strings(*args):
    return " ".join(args)

print(concatenate_strings("Hello", "world!", "How", "are", "you?"))
