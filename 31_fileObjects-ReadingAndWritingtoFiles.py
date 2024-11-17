# File Objects

with open('test.txt' , 'r') as f:
    # f_contents = f.read()
    # print(f_contents)
    
    # what if we don't want to read everything from a file
    f_lines = f.readline() # it gives first line
    print(f_lines)
    f_lines = f.readline() # it gives second line
    print(f_lines)
    f_lines = f.readline() # it gives third line
    print(f_lines)

# print(f.name)
# print(f.mode)
# print(f.closed)
# print(dir(f))

# efficient way to read all the contents from a file

with open('test.txt', 'r') as file:
    
    for line in file:
        print(line, end='')
        
        
# print specific characters al at once

with open('test.txt', 'r') as file_:
    print('\n Printing first 150 characters')
    f_line = file_.read(150)
    print(f_line)