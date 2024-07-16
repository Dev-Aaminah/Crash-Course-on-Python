# --------------------  while loop to print a table -------------------- #
m = 5
n = 1
while n <= 5:
    print(m, "x", n, " = ", m*n)
    n+=1
   
# --------------------  function to print a table   -------------------- #
 
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1
    
    # Complete the while loop condition
    while multiplier <= 5:
        result = number * multiplier
        
        # Enter the action to take if the result > 25
        if result > 25:
            break
        
        # Print the multiplication result
        print(f"{number} x {multiplier} = {result}")
        
        # Increment the appropriate variable
        multiplier += 1

# Test call to the function
multiplication_table(3)