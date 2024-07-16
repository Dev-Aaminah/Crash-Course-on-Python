def factorial(n):
    # Base case: if n is less than 2, return 1
    if n < 2:
        return 1
    # Recursive case: return n multiplied by the factorial of n-1
    return n * factorial(n - 1)

# Example usage:
print(factorial(5))  # Should print 120