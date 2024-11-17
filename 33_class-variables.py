# class variables are the variables that are shared among all the instances of a class

class Employee:
    raise_amount = 1.04 # class variable
    num_of_employee = 0
    
    def __init__(self, name, pay, age):
        self.name = name
        self.age = age
        self.pay = pay
        self.email = name+'.'+'@gmail.com'
        
        Employee.num_of_employee += 1
        
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

emp1 = Employee('Aliyana',50000, 20)

print(f'before raise {emp1.pay}')
emp1.apply_raise()
print(f'after raise {emp1.pay}')

emp2 = Employee('Rida',50000, 25)
print(f'before raise {emp2.pay}')
emp2.raise_amount = 1.08 #change raise amount for an instance instead of class
emp2.apply_raise()
print(f'after raise {emp2.pay}')

print(emp2.__dict__)

print(f'Number of employees {Employee.num_of_employee}') 