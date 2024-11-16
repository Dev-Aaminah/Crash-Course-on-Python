print('Imported my_module...')

test = 'Test String'

def find_index(to_search, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_search):
        if value == target:
            return i
    return -1


def search_student(tosearch, tofind):
    for i, value in enumerate(tosearch):
        if value == tofind:
            print(tofind, 'found' )
            return
    print('Not Found')
    
