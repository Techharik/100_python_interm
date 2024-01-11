# list and dictionary compariations. - Short cut for creating new list with some actions

# example : creating a new list


numbers = [2,3,4]
# new_list = []
# for n in numbers:
#     add_n = n+1
#     new_list.append(add_n)

# print(new_list)

# new_list = [expression for looped item in Array]

new_list = [n+1 for n in numbers]
# print(new_list)
# using range_list
new_list = [n*2 for n in range(1,5)]
# print(new_list)

# ? consitional list comperihension

# new_list = [expression for looped item in Array if condtion]

# example

new_list_if = [n+1 for n in range(1,10) if n%2 == 0]


# print(new_list_if)


# Squared numbers using list comperehension


numbers_list = [1,1,4,6,8,9]


squered_numbers = [n*n for n in numbers_list] 
even_number = [n for n in numbers_list if n%2 == 0]


# print(squered_numbers)
# print(even_number)

with open('./file1.txt') as num1:
    num_list = num1.readlines()
    new_list_num = [n.replace('\n','') for n in num_list ]

with open('./file2.txt') as num2:
    num1_list = num2.readlines()
    new_list_num1 = [n.replace('\n', '') for n in num1_list]

result = [n for n in new_list_num if n in new_list_num1]

print(result)



# ? Dictionsried comperihensions:

# new_dic = {new_key:new_value for item in items_list}

# ! create a new dic in a existing dictionary with conditions.

# new_dic = {new_key:new_value for (key,value) in dic.items() if test}

names = ['hari', 'Sabari','Vijay'];
import random;

new_dic = {stud:random.randint(1,100) for stud in names}

# print(new_dic)

passed_test = {key:value for (key,value) in new_dic.items() if new_dic[key]  > 40}

# print(passed_test)

exerices