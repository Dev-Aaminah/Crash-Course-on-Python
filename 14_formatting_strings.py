# Using the format() method for string formatting in Python
# The format() method allows us to format strings by inserting values into placeholders

name = "Anamta"
number = 90078601

# Basic string formatting with format()
print("Hello {} your number is {}.".format(name, number))

# Using named placeholders in the format() method
# Here we use the length of the name multiplied by 3 to create a lucky number
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name) * 3))

# Another example of using named placeholders in the format() method
print("{name} your lucky number is {number}.".format(name=name, number=len(name) * 3))

# Working with numbers and formatting output
price = 7.5
with_tax = price * 1.09

# Printing raw numbers
print(price, with_tax)

# Formatting numbers to 2 decimal places using format()
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))