
fullname = ('Grace', 'M', 'Hopper')     # modifying isn't allowed in tuples
print(fullname)

def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_second = seconds - hours * 3600 - minutes * 60 
    return hours, minutes, remaining_second
    
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds)# Tuple containing a full name
fullname = ('Grace', 'M', 'Hopper')
print(fullname)  # Print the tuple

# Function to convert seconds into hours, minutes, and seconds
def convert_seconds(seconds):
    # Calculate hours
    hours = seconds // 3600
    # Calculate minutes
    minutes = (seconds - hours * 3600) // 60
    # Calculate remaining seconds
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
    
# Convert 5000 seconds into hours, minutes, and seconds
hours, minutes, seconds = convert_seconds(5000) # here actually we turned tuple in variables. i.e hours, minutes and seconds 
print(hours, minutes, seconds)  # Print the result