student = {
    'name': "Alice",
    'country': 'France',
    'dob': '25-08-2000',
    'courses': ['CompSci', 'Math']
}

print(student)
print(student['dob'])
# print(student['phone']) #this will return 'key not found' error. as key 'phone' doesn't exists.

print(student.get('phone', 'Not Found')) #for default values, we can use .get method to avoid key not found

# New entry to our dictionary
student['phone'] = '090078601'
print(student.get('phone'))

# as we've used .get method, if we write it below the above new entry section, then we'll see that it'll update the value of key.

# update value
student['name'] = 'Jane'
print(student) 
#we also have .update method for dictionaries
student.update()

# update multiple values
student.update({'name': 'Smith', 'country': 'France', 'age': 27})
print(student)

# del a key
del student['country']
print(student)

# pop method
age = student.pop('age')
print(age)

# check items of dictionary
print(len(student))

print(student.items())
print(student.values())
print(student.keys())

# loop on dictionaries
for key in student:
    print(key)
    
for key, value in student.items():
    print(key, value)