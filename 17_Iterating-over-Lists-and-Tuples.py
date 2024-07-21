# List of animals
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]

# Variable to store the total number of characters
chars = 0

# Loop through each animal in the list
for animal in animals:
    # Add the length of each animal's name to the total characters
    chars += len(animal)
    
# Calculate and print the total number of characters and the average length of the animal names
print("Total characters: {}, Average length: {}".format(chars, chars / len(animals)))


# List of winners
winners = ["Ashley", "Dylan", "Amina"]

# Loop through the list of winners with their index using enumerate
# The enumerate() function adds a counter to the iterable (winners) and returns it as an enumerate object
for index, person in enumerate(winners):
    # Print the index (1-based) and the person's name
    print("{} - {}".format(index + 1, person))
    

# Function to format a list of email, name pairs into a list of formatted strings
def full_emails(people):
    # Initialize an empty list to store the results
    result = []
    
    # Loop through each pair of email and name in the people list
    for email, name in people:
        # Format the name and email and add to the result list
        result.append("{} <{}>".format(name, email))
    
    # Return the formatted list
    return result

# Call the function with a list of email, name pairs and print the result
print(full_emails([("alex@example.com", "Alex Diego"), ("shay@example.com", "Shay Brandt")]))