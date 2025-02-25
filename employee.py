import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s- %(message)s')

file_handler = logging.FileHandler('employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
# logging.basicConfig(filename='employee.log',
#                     level=logging.INFO,
#                     format='%(asctime)s - %(name)s- %(message)s')

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        logger.info('Created Employee: {}'.format(self.fullname, self.email()))
        
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