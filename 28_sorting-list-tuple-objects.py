# =============== Sort List =============== #
li = [8,5,7,2,4,6,1,3]
print(li)

sorted_li = sorted(li,reverse=True)
print(sorted_li)

# lists have sort() method

# if we don't want to create new variable
list_of_nums = [9,5,1,0,7,3,5,6,8,4]
print('Unsorted List' , list_of_nums)
list_of_nums.sort(reverse=False)
print('Sorted List' , list_of_nums)

# =============== Sort Tuple =============== #
tup = (5,7,8,6,2,2,1,3,6,4,9,0)
# tup.sort() #'tuple' object has no attribute 'sort'
sorted_tuple = sorted(tup)
print(sorted_tuple)

# =============== Sort Dict =============== #
dictionary = {
    'name': 'amina',
    'gender': 'female',
    'degree': 'BSSE',
    'height': 5.4
}

s_dictionary = sorted(dictionary)
print(s_dictionary)

