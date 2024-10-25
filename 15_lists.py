# Initialize a list of programming languages
x = ["Python", "JavaScript", "C", "C++", "C#", "Ruby", "Go"]
print(x)  # Print the entire list
print(type(x))  # Print the type of x, which should be a list
print(len(x))  # Print the length of the list

# Check for the presence of an element in the list
print("C" in x)  # Check if 'C' is in the list

# Accessing elements in the list by index
print(x[6])  # Print the element at index 6 (last element)

# Slicing the list
print(x[1:6])  # Print elements from index 1 to 5
print(x[:5])  # Print the first 5 elements
print(x[3:])  # Print elements from index 3 to the end

# Working with another list: fruits
fruits = ["Pineapple", "Banana", "Apple", "Melon"]

# Adding elements to the list
fruits.append("Kiwi")  # Append 'Kiwi' to the end of the list
print(fruits)  # Print the updated list

fruits.insert(0, "Mango")  # Insert 'Mango' at the beginning of the list
print(fruits)  # Print the updated list

# Clearing all elements from the list
fruits.clear()  # Clear the list
print(fruits)  # Print the empty list

# Inserting an element at a specific index in an empty list
fruits.insert(7, "Peach")  # This will create an index gap
print(fruits)  # Print the list with 'Peach' at index 7

# Reinitializing the list with fruits
fruits = ["Pineapple", "Banana", "Apple", "Melon"]

# Removing elements from the list
# fruits.remove("Pear") # This will throw an error because 'Pear' is not in the list

fruits.pop(2)  # Remove the element at index 2
print(fruits)  # Print the updated list

# Replacing an element in the list
fruits[2] = "Strawberry"  # Replace the element at index 2 with 'Strawberry'
print(fruits)  # Print the updated list

print("Sorted list")
fruits.sort()
print(fruits)

print("Sorted list in reverse")
fruits.sort(reverse=True)
print(fruits)

print("Sorted version of list instead of altering original list")
# sorted(fruits) # sorted() function does not return the list in place. It returns the sorted version of list. Achieve this we'll need it to store in a variable.
# print()

sorted_fruits = sorted(fruits)
print(sorted_fruits)

# indexing
fruits_index = fruits.index('Banana')
print(fruits_index)

# in , not in operator
print('Art' in fruits)
print('Banana' not in fruits)

for fruit in fruits:
    print(fruit)
    
# enumerate function
# it returns two values, index and value

for index, fruit in enumerate(fruits, start=1) :
    print(index, fruit)
    
print(fruits)
fruits_string = ', '.join(fruits)
print(fruits_string)