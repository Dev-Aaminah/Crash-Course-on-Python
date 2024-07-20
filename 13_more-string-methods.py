# message = "Hello"
# print(message.lower())

# print("SADia".upper())

# answer = input("Enter Something: \n")
# if answer == 'yes':
#     print("User said yes")
# else:
#     print("User said 'YES'")
    
# # Strip
# new_string = input("Enter a string with spaces and tab spaces : ")
# print(new_string.strip())
# print(new_string.lstrip())
# print(new_string.rstrip())

# # count
# string_input = input("Enter string you want to count alphabet for. \n")
# string_count = input("Enter character which you want to count: ")
# print("In ", string_input, " '", string_count, " ' occurs", string_input.count(string_count))

# Endswith
print("Your string ends with.".endswith("."))   # True

# isNumeric
print("Amina".isnumeric())   # False
print("123456".isnumeric())   # True

# int to convert into actual number from string
number = '090078601'
print(type(number)) # output will be 'string'
print(type(int(number)))    # output will be 'int'

# join
str1 = "Amina "
str2 = "Bibi"
print(" ".join([str1, str2]))
print(" ".join(["This", "is", "a", "string"])) # the " " at the start of this includes spaces between each item in the above list
print("...".join(["This","is","another","string."]))

# split
print("Hello Everyone, I am here :)".split())