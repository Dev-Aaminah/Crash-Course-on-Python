# Sets are values that are unordered and also have no duplicates.

fruits = {'Banana', 'Pineapple', 'Strawberry'}
print(fruits) # the order of set item can change on run time

fruit = {'Banana', 'Mango', 'Strawberry', 'Banana'}
print(fruit) #it didn't print the duplicate 'Banana'. 

print('Pineapple' in fruits)

# Similar items in both sets
print(fruit.intersection(fruits))

# Different items in both sets
print(fruit.difference(fruits))
print(fruits.difference(fruit))

# Combine all courses
print(fruits.union(fruit))