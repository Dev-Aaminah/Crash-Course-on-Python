# Comparison of an integer with a string using the '>' operator
try:
    result = 1 > "1"  # This will raise a TypeError
except TypeError as e:
    print(f"TypeError: {e}")  # Output the error message

# Explanation:
# When using the '>' operator, Python expects both operands to be of compatible types (e.g., both numbers).
# Comparing an integer (1) with a string ("1") directly is not allowed, hence a TypeError is raised.

# Comparison of an integer with a string using the '==' operator
result = 1 == "1"
print(f"1 == '1': {result}")  # Output: 1 == '1': False

# Explanation:
# The '==' (equality) operator behaves differently. When comparing different types,
# Python attempts to convert one or both operands to a common type before making the comparison.
# In this case, Python converts the string "1" to an integer (1) and then compares them.
# Since an integer (1) is not equal to a string ("1"), the result is False.

# Why doesn't Python perform similar type conversion for the '>' operator?
# - '>' (Greater Than): This operator is primarily used for numeric comparisons (integers, floats, etc.).
#   It doesn't make sense to compare a number with a non-numeric value like a string.
#   Python avoids implicit type conversion here to prevent unexpected behavior.
# - '==' (Equality): The equality operator is more forgiving. It tries to accommodate different types
#   by converting them if possible. However, it still adheres to certain rules (e.g., comparing numbers with strings).

# Summary:
# Python’s behavior with comparison operators strikes a balance between consistency and practicality.
# While it converts types for equality checks, it avoids doing so for operators like '>'.
# If you encounter scenarios where you need to compare different types, consider explicitly converting them
# beforehand to ensure predictable results.

# Example of explicit type conversion:
try:
    # Convert the string to an integer before comparison
    result = 1 > int("1")
    print(f"1 > int('1'): {result}")  # Output: 1 > int('1'): False
except ValueError as e:
    print(f"ValueError: {e}")  # Handle any conversion errors

# Example of explicit type conversion for equality check:
result = 1 == int("1")
print(f"1 == int('1'): {result}")
