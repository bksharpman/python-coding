# #1.1
# intuple = input()   
# this_tuple = ()
# for x in intuple:
#   this_tuple += (x,)
# print(this_tuple)


# #1.2
# this_tuple = ('q', 'w', 'e', 'r', 't', 'y')
# this_string = "".join(this_tuple)
# print("The string is: ", this_string)


# #1.3
# tuple_A = (1, 2, 3, 4, 5, 6, 7)
# tuple_B = (5, 6, 7, 9, 7, 1, 10, 10)
# half_A = tuple_A[:len(tuple_A)//2]
# half_B = tuple_B[len(tuple_B)//2:]
# concatenated_tuple = half_A + half_B
# print(concatenated_tuple)


# #1.4
# user_input = (55, 6, 777, 54, 6, 76, 7777, 1, 777, 6)

# element_count = {}
# for x in user_input:
#     if x in element_count:
#         element_count[x] += 1
#     else:
#         element_count[x] = 1

# element_occurrences = tuple((key, value) for key, value in element_count.items())
# print("Elements and their occurrences:")
# print(element_occurrences)


# #1.5
# data_objects = (55, 6, 777, 70.0, '7', 'A')

# tuples = []
# current_tuple = ()
# for x in data_objects:
#     if isinstance(x, (int, float)):
#         if current_tuple:
#             tuples.append(current_tuple)
#             current_tuple = ()
#         tuples.append(x)
#     else:
#         current_tuple += (x,)

# if current_tuple:
#     tuples.append(current_tuple)

# for t in tuples:
#     print(t)


# #2.1
# user_input = input()
# user_set = {char for char in user_input}
# print("created set is:")
# print(user_set)


# #2.2
# set_A = {1, 2, 3, 4, 5}
# set_B = {5, 7, 8, 9, 2, 10}
# result_set = set_A.difference(set_B)
# print(result_set)


# #2.3
# set_A = {1, 2, 3, 4, 5}
# set_B = {5, 7, 8, 9, 2, 10}
# set_A.difference_update(set_B)
# print(set_A)


# #2.4
# set_A = {1, 2, 3, 4, 7}
# set_B = {8, 7, 9, 4, 2, 0, 10}
# set_C = {4, 0, 1}
# for x in set_A.copy():
#     if x in set_C:
#         set_A.remove(x)
#         set_B.add(x)
# print("Updated set_A =", set_A)


# #2.5
# import itertools

# A = {1, 2, 3, 4, 5, 6}
# n = 3
# m = 5
# combinations = list(itertools.combinations(A, n))
# sets_list = [set(combination) for combination in combinations[:m]]
# print(sets_list)


# #3.1
# from itertools import groupby

# cars_list = [('BMW', 'X6'), ('Toyota', 'Yaris'), ('Fiat', '500'), ('Fiat', 'Panda'), ('Toyota', 'Camry 30')]

# cars_list.sort(key=lambda x: x[0])

# for manufacturer, models in groupby(cars_list, key=lambda x: x[0]):
#     models_list = list(models)
#     print(f"{manufacturer} {len(models_list)}")
#     for model in models_list:
#         print(f"- {model[1]}")