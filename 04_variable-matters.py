
# Initialization
x = 1
sum = 0

# First while Loop
while x < 10:
    sum = sum + x
    x = x + 1

# This loop runs as long as x is less than 10.
# During each iteration, the value of x is added to sum, and x is incremented by 1.
# After the loop completes, sum will be the sum of integers from 1 to 9 (i.e., 1 + 2 + 3 + ... + 9).
# The final value of sum will be 45, and x will be 10.

# Second while Loop
product = 1
while x < 10:
    product = product * x
    x = x + 1

# This loop is intended to run as long as x is less than 10.
# However, since x is already 10 after the first loop, this loop will not run at all.
# As a result, product remains 1.

# Printing the Results
print(sum, product)

# Execution Trace
# First Loop:
# x = 1, sum = 0 + 1 = 1, x = 2
# x = 2, sum = 1 + 2 = 3, x = 3
# x = 3, sum = 3 + 3 = 6, x = 4
# x = 4, sum = 6 + 4 = 10, x = 5
# x = 5, sum = 10 + 5 = 15, x = 6
# x = 6, sum = 15 + 6 = 21, x = 7
# x = 7, sum = 21 + 7 = 28, x = 8
# x = 8, sum = 28 + 8 = 36, x = 9
# x = 9, sum = 36 + 9 = 45, x = 10
# Loop ends because x is now 10.

# Second Loop:
# Loop does not run because x is 10, which is not less than 10.

# Output
# The final values of sum and product are 45 and 1, respectively.

# print(sum, product)  # Output: 45 1