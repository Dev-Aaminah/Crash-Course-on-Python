# Define a function to convert Fahrenheit to Celsius
def to_celsius(x):
    return (x - 32) * 5 / 9

# Iterate through a range of Fahrenheit values from 0 to 100 in steps of 10
for x in range(0, 101, 10):
    # Print the Fahrenheit value and its corresponding Celsius value
    print(x, to_celsius(x))