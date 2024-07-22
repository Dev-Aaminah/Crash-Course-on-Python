# Creating a list of multiples of 7 from 1 to 10
multiples = []
for x in range(1, 11):
    multiples.append(x * 7)
print(multiples)

# Creating the same list using list comprehension
multiple = [x * 7 for x in range(1, 11)]
print(multiple)

# Calculating the length of each language name in the list
languages = ["Python", "Ruby", "Perl", "Go", "Java", "C"]
lengths = [len(language) for language in languages]
print(lengths)

# Creating a list of numbers from 0 to 100 that are divisible by 3
z = [x for x in range(0, 101) if x % 3 == 0]
print(z)

# Function to generate a list of odd numbers from 1 to n inclusive
def odd_numbers(n):
    return [x for x in range(1, n + 1) if x % 2 != 0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []