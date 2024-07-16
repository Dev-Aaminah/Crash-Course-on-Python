string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet”


# An optional way to slice an index is by the stride argument, indicated by using a double colon. This allows you to skip over the corresponding number of characters in your index, or if you’re using a negative stride, the string prints backwards.
print(string1[0::2]) # Prints “Getns atlns”
print(string1[::-1]) # Prints “sgnilhtraE ,sgniteerG”

# You can also use the join() function, which is very useful when you want to concatenate elements from a list of strings with a specific delimiter.
greetings = ["Hello", "world"]
print(" ".join(greetings)) # Prints "Hello world"
# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!") # Prints "Hello, Alice!"

