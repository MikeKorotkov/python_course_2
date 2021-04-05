# string = '4,6,234,65'
# print(str.split(string))

#######################################

# lst = [1,5345,323,54353,2342342356,4674657,'re4231',545435]
# print(lst[0])
# print(lst[-1])

#######################################

# n = 5
# power = 3
# var_lst = []
# for i in range(1, power+1):
#     var = n ** i
#     var_lst.append(var)
# print(sum(var_lst))

#######################################

# some_lst = [1,345,67887,34234,234,345,237,54353,67568]
# for item in some_lst:
#     print(item)
#     if item == 237:
#         break

#######################################

# lst1 = [1,345,67887,34234,234,345,237,54353,67568]
# lst2 = [1,5345,323,54353,2342342356,234,4674657,'re4231',545435]
# same_items = []
# for item in lst1:
#     for item2 in lst2:
#         if item == item2:
#             same_items.append(item)
# print(same_items)

#######################################

# some_number = 12343534652424
# new_string = str(some_number)
# res = 0
#
# for item in new_string:
#     res += int(item)
#
#
# print(res)

#######################################

# string = '213qqjdoa4542jnvvqfvqkpq'
# res = 0
# for item in string:
#     if item == 'q':
#         res += 1
#
# print(res)

#######################################

# lst = [1,5,7,8,9,0,3,2,4,5,6]
#
# print((lst[::-1]))

#######################################

# lst = []
# queue_size = 5
#
#
# def add_to_queue(lst, new_elem):
#     if len(lst) >= queue_size:
#         lst.pop(0)
#     lst.append(new_elem)
#
#
# add_to_queue(lst, 1)
# add_to_queue(lst, 2)
# add_to_queue(lst, 3)
# print(lst)
# add_to_queue(lst, 4)
# add_to_queue(lst, 5)
# add_to_queue(lst, 6)
# print(lst)

#######################################

# a = 12
# b = 20
#
# for item in range(b, 0, - 1):
#     if a % item == 0 and b % item == 0:
#         res = item
#         break
#
# print(res)

#######################################

# size = 5
# lst = [1, 2, 3, 4, 5]
#
#
# def change(change_size, lst):
#     if change_size >= size:
#         return
#
#     lst += lst[:change_size]
#     lst[:change_size] = []
#
#
# change(3, lst)
#
# print(lst)

#######################################

# lst = [1,7, 3, 3, 2, 5, 4]
#
# for index, value in enumerate(lst):
#     if value in lst[index + 1:]:
#         print(True)
#         break
#     else:
#         print(False)
#         break

#######################################

# lst = [1, 5, 7, 123, 43656, 87, 20, 3463, 202341, 20]
# for index, value in enumerate(lst):
#     if value == 20:
#         lst[index] = 200
#         break
# print(lst)

#######################################

lst = ['', 'sdfdfdsdfsdf', '213hbnmc,s','', 1234]

for item in lst:
    if item == '':
        lst.pop(item)
print(lst)