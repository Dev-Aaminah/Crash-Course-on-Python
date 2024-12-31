# Creating a Generator Function A generator function is defined like a normal function but uses the yield statement instead of return. Each time yield is executed, the state of the function is saved, and it can resume from where it left off.

def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count+=1
        
for number in count_up_to(4):
    print(number)
    
# another generator function
def alphabets(vowels):
    for i in vowels:
        yield i
        
for i in alphabets(['a','e','i','o','u']):
    print(i)
    
# same above code with list comprhension
print("List Comprehnsion generator function")
alphs = [x for x in ['a','e','i','o','u']]
for i in alphs:
    print(i)
    
# You can see that generator do not hold all the values in memory at once. But there is a simple list() func for it.
print(list(alphs))