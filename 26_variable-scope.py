'''
LEGB
Local, Enclosing, Global, Built-in
'''

#Locals - variable defined inside a function
def outer():
    x = 10  # Local to 'outer'

#Enclosing - variables defined in local scope of an enclosing function
def outer():
    x = 10  # Enclosing for 'inner'
    def inner():
        print(x)  # Looks for x in Enclosing scope of 'outer'

#Global - variable defined with a keyword global or at the top of a module
x = 20  # Global scope
def example():
    print(x)  # Python looks in the Global scope if 'x' isn't found locally

#Built-in - are names that are pre-assigned in python
def example():
    print(len([1, 2, 3]))  # 'len' is found in the Built-in scope


x = 'global x'

def test():
    x= 'local x'
    print(x)
    
test()
print(x)

# --------------- Global --------------- #
y = 'global y'
def test_func():
    global y
    y = 'local y'
    print(y)
test_func()
print(y)

# --------------- Built-in --------------- #
import builtins
print(dir(builtins))

for i in dir(__builtins__):
    print(i)
    
m = min([2,3,45,66,7,8,9,1])
print(m)