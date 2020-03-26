# COMP9021 19T3 - Rachid Hamadi
# Quiz 2 *** Due Thursday Week 3


import sys
from random import seed, randrange
from pprint import pprint

try:
    arg_for_seed, upper_bound = (abs(int(x)) + 1 for x in input('Enter two integers: ').split())
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
mapping = {}
for i in range(1, upper_bound):
    r = randrange(-upper_bound // 8, upper_bound)
    if r > 0:
        mapping[i] = r
print('\nThe generated mapping is:')
print('  ', mapping)
# sorted() can take as argument a list, a dictionary, a set...
keys = sorted(mapping.keys())
print('\nThe keys are, from smallest to largest: ')
print('  ', keys)

cycles = []
reversed_dict_per_length = {}

# INSERT YOUR CODE HERE
sub_list = []
for i in mapping:
    temp = i
    sub_list.append(temp)
    if temp == mapping[temp]:
        cycles.append([temp])
    else:
        while mapping[temp] in mapping:
            if mapping[temp] != sub_list[0]:
                if mapping[temp] not in sub_list:
                    sub_list.append(mapping[temp])
                    temp = mapping[temp]
                    if temp == mapping[temp]:
                        break
                else:
                    sub_list = []
                    break
            else:

                if sorted(sub_list) not in cycles:
                    cycles.append(sub_list)
                sub_list = []
                break

    sub_list = []

value = list(set(mapping.values()))

for i in value:
    new_value = []
    count = 0
    for j in mapping:
        if mapping[j] == i:
            count += 1
            new_value.append(j)
    print(new_value)

    if count > 0:
        if count not in reversed_dict_per_length:
            reversed_dict_per_length[count] = {}
            reversed_dict_per_length[count][i] = new_value
        else:
            reversed_dict_per_length[count][i] = new_value





print('\nProperly ordered, the cycles given by the mapping are: ')
print('  ', cycles)
print('\nThe (triply ordered) reversed dictionary per lengths is: ')
pprint(reversed_dict_per_length)


