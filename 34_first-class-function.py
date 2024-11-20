# First-class functions allow functions to be treated like any other data type:
# Assigning to variables: Functions can be stored in variables, making them easily accessible and reusable.
# Passing as arguments: Functions can be passed as arguments to other functions.
# Returning from functions: Functions can be the result of another function. 

def func(multiple):
    return multiple*multiple

f = func # assigning function to a variable
# parenthesis will not be included while assigning func to a variable.
print(func)
print(f)

print(func(5))
print(f(2))


# Passing functions as argument
def multiples(x):
    return x*x

def number_multiple(func, arg_list):
    result = []
    for i in arg_list:
        result.append(func(i))
    return result
m = number_multiple(multiples, [2,3,4,5,6,7,8,9,10])
print(m)


# return function as function
def logger(msg):
    
    def log_msg():
        print("Log:", msg)
        
    return log_msg

log_hi = logger('Hi!')
log_hi()