# Define a list of values
values = [23, 52, 59, 37, 48]

# Initialize variables to hold the sum and the count of the values
sum = 0
length = 0

# Iterate through each value in the list
for value in values:
    # Add the current value to the sum
    sum += value
    # Increment the count of values
    length += 1

# Print the total sum and the average of the values
print("Total sum: " + str(sum) + " - Average: " + str(sum / length))