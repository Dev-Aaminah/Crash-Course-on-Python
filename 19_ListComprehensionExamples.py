# Create a list of tuples where each tuple contains the numbers 1, 2, and 3.
numbers = [(1,2,3) for i in range(5)]
print(numbers)


######################### For loop vs. list comprehension #########################
### Simple List Comprehension
print("List comprehension result:")

# The following list comprehension compacts several lines 
# of code into one line:
print([x*2 for x in range(1,11)])

### Long form for loop
print("Long form code result:")

# The list comprehension above accomplishes the same result as
# the long form version of the code shown below:
my_list = []
for x in range(1,11):
    my_list.append(x*2)
print(my_list)


######################### List comprehension with conditional statement #########################
print("List comprehension result:")
print([x for x in range(1,101) if x % 10 == 0])

# The list comprehension above accomplishes the same result as
# the long form version of the code:
print("Long form code result:")
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
        
print(my_list)