def sum_of_integers(n):
    # Check if the input is less than 1
    # If n is less than 1, return 0 since there are no positive integers to sum
    if n < 1:
        return 0
    
    # Initialize the variables
    i = 1  # This variable will be used to iterate from 1 to n
    sum = 0  # This variable will hold the sum of integers from 1 to n
    
    # This while loop runs as long as i is less than or equal to n
    # It adds the value of i to sum and increments i by 1 in each iteration
    while i <= n:
        sum = sum + i
        i += 1
    
    # After the loop completes, return the calculated sum
    return sum

# Calls to the function with different test cases
print(sum_of_integers(3))  # should print 6 (1 + 2 + 3)
print(sum_of_integers(4))  # should print 10 (1 + 2 + 3 + 4)
print(sum_of_integers(5))  # should print 15 (1 + 2 + 3 + 4 + 5)