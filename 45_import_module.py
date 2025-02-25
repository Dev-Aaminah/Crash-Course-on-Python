# import_module.py

print("\n--- Running import_module.py ---")

# Import the __name__ module
import name

# Use the add function from the imported module
result = name.add(10, 20)
print(f"Result of add(10, 20) from imported module: {result}")