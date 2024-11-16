# to import everything from a module
# from module_name import *
# here * means to import everything

from my_module import search_student as ss

import sys #helps to find the track of a module

students=['Aqsa', 'Sana', 'Maria']
index = ss(students, 'Maria')

print(sys.path) #checks for module path