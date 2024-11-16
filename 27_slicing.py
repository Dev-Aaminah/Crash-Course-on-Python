my_list = [0, 1 , 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1 , 2, 3, 4, 5, 6, 7, 8, 9
#         -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

print(my_list[3])
print(my_list[-7])
print(my_list[0:7])  # [start: end]
print(my_list[-10:-3])
print(my_list[2:-5])
print(my_list[0:9])
print(my_list[0:])
print(my_list[:-1])

print(my_list[0:9:4]) # [start: end :step]
print(my_list[-1:2:-1]) # [9, 8, 7, 6, 5, 4, 3]
print(my_list[::-1]) # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# slice a string
sample_url = 'https://abc.com'
print(sample_url)

print(sample_url[-4:])
print(sample_url[8:])
