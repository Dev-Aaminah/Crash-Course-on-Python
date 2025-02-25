# name.py

# In Python, __name__ is a special built-in variable that holds the name of the current module.
# Its value depends on how the module is being used:
# - If the module is being run as the main program, __name__ is set to '__main__'.
# - If the module is being imported, __name__ is set to the name of the module (i.e., the filename without the .py extension).

# Why is __name__ important?
# 1. Module Execution Control:
#    - It allows you to write code that behaves differently depending on whether the module is run directly or imported.
# 2. Avoiding Unwanted Execution:
#    - When a module is imported, you may not want certain parts of the code (e.g., test code or demonstration code) to run.
# 3. Debugging and Testing:
#    - You can include test code or debugging code in a module that only runs when the module is executed directly.

# ------------------------------------------------------------------------------------
# Example 1: Running a Module Directly
# ------------------------------------------------------------------------------------

print("\n--- Example 1: Running a Module From name.py ---")
print(f"__name__ is: {__name__}")

if __name__ == '__main__':
    print("This module is being run directly.")
else:
    print("This module is being imported.")

# Output when run directly:
# __name__ is: __main__
# This module is being run directly.

# Output when imported:
# __name__ is: __name__
# This module is being imported.

# ------------------------------------------------------------------------------------
# Example 2: Running Code Only When the Module is Executed Directly
# ------------------------------------------------------------------------------------

print("\n--- Example 2: Running Code Only When the Module is Executed Directly ---")

def main():
    print("This is the main function.")

if __name__ == '__main__':
    main()


# Output when run directly:
# This is the main function.

# Output when imported:
# (Nothing happens)

# ------------------------------------------------------------------------------------
# Example 3: Writing Test Code
# ------------------------------------------------------------------------------------

print("\n--- Example 3: Writing Test Code ---")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

if __name__ == '__main__':
    # Test code (only runs when the module is executed directly)
    print("Testing math_operations module:")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"subtract(5, 2) = {subtract(5, 2)}")

# Output when run directly:
# Testing math_operations module:
# add(2, 3) = 5
# subtract(5, 2) = 3

# Output when imported:
# (Nothing happens)

# ------------------------------------------------------------------------------------
# Example 4: Conditional Imports
# ------------------------------------------------------------------------------------

print("\n--- Example 4: Conditional Imports ---")

if __name__ == '__main__':
    import math  # Import math only when running directly
    print(f"Square root of 16 is {math.sqrt(16)}")

# Output when run directly:
# Square root of 16 is 4.0

# Output when imported:
# (Nothing happens)

# ------------------------------------------------------------------------------------
# Example 5: Importing the Module into Another File
# ------------------------------------------------------------------------------------

# To demonstrate what happens when this module is imported, create another file called `import_module.py`:
"""
# import_module.py

print("\n--- Running import_module.py ---")

# Import this module
import __name__

# Use the add function from the imported module
result = __name__.add(10, 20)
print(f"Result of add(10, 20) from imported module: {result}")
"""

# Output when import_module.py is run:
"""
--- Running import_module.py ---

--- Example 1: Running a Module Directly ---
__name__ is: __name__
This module is being imported.

--- Example 2: Running Code Only When the Module is Executed Directly ---

--- Example 3: Writing Test Code ---

--- Example 4: Conditional Imports ---

Result of add(10, 20) from imported module: 30
"""

# ------------------------------------------------------------------------------------
# Key Takeaways
# ------------------------------------------------------------------------------------

# 1. __name__ is a special variable that holds the name of the current module.
# 2. __name__ == '__main__' is used to check if the module is being run directly.
# 3. Use __name__ to control execution:
#    - Run code only when the module is executed directly.
#    - Avoid running unwanted code when the module is imported.
# 4. Great for testing and debugging:
#    - Include test code that only runs when the module is executed directly.

# ------------------------------------------------------------------------------------
# Best Practices
# ------------------------------------------------------------------------------------

# 1. Always use if __name__ == '__main__': for code that should only run when the module is executed directly.
# 2. Keep reusable code in functions and call those functions in the if __name__ == '__main__': block.
# 3. Avoid putting top-level code in modules that might be imported, as it will execute when the module is imported.

# End of script