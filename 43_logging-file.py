import logging

logging.basicConfig(filename='employee.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(name)s- %(message)s')

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def email(self):
        return '{}{}@gmail.com'.format(self.first,self.last)
    
    def __repr__(self):
        return "Employee('{}','{}','60000').".format(self.first, self.last, self.pay)
    
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email())
    
    def __add__(self, other):
        return self.pay + other.pay
emp1 = Employee('Corey', 'Schafer', 50000)
emp2 = Employee('Steven', 'Schafer', 60000)

# Log information
logging.info('Employee1: {}'.format(emp1))
logging.info('Employee2: {}'.format(emp2))