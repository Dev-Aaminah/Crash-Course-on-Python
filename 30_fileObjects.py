#file objects

f = open('test.txt', mode='r') # not recommended way, for recommended way check file 31
print(f)
print(f.name)
print(f.mode)

f.close() #always close explicitly
