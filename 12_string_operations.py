# Correcting a typo in a string and printing the corrected message
message = "A kong string with a silly typo"
# Constructing a new message by replacing the 'k' at index 2 with 'l'
new_message = message[0:2] + "l" + message[3:]
print(new_message)  # Output: A long string with a silly typo

# Working with the string "Cats & Dogs"
pets = "Cats & Dogs"

# Printing the index of the character "&" in the string
print(pets.index("&"))  # Output: 5

# Printing the index of the character "C" in the string
print(pets.index("C"))  # Output: 0

# Printing the index of the substring "Dog" in the string
print(pets.index("Dog"))  # Output: 7

# Printing the index of the character "s" in the string
print(pets.index("s"))  # Output: 3

# Checking for substring existence in the string "Cats & Dogs"
print("Dragons" in pets)  # Output: False
print("Cats" in pets)     # Output: True
