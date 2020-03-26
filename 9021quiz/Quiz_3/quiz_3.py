# COMP9021 19T3 - Rachid Hamadi
# Quiz 3 *** Due Thursday Week 4


# Reading the number written in base 8 from right to left,
# keeping the leading 0's, if any:
# 0: move N     1: move NE    2: move E     3: move SE
# 4: move S     5: move SW    6: move W     7: move NW
#
# We start from a position that is the unique position
# where the switch is on.
#
# Moving to a position switches on to off, off to on there.

import sys
import numpy as np

on = '\u26aa'
off = '\u26ab'
code = input('Enter a non-strictly negative integer: ').strip()
try:
    if code[0] == '-':
        raise ValueError
    int(code)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_leading_zeroes = 0
for i in range(len(code) - 1):
    if code[i] == '0':
        nb_of_leading_zeroes += 1
    else:
        break

print("Keeping leading 0's, if any, in base 8,", code, 'reads as',
      '0' * nb_of_leading_zeroes + f'{int(code):o}.'
     )
print()

# INSERT YOUR CODE HERE

# find the rule to move
direction = ('0' * nb_of_leading_zeroes + f'{int(code):o}')[::-1]

# list points to store every step in coordinate form and add the origin first
points = [[0,0]]
x = [0,0]

# use a loop to record each point step by step
for i in direction:
    if i == '0':
        x[1] += 1
    if i == '1':
        x[1] += 1
        x[0] += 1
    if i == '2':
        x[0] += 1
    if i == '3':
        x[0] += 1
        x[1] -= 1
    if i == '4':
        x[1] -= 1
    if i == '5':
        x[0] -= 1
        x[1] -= 1
    if i == '6':
        x[0] -= 1
    if i == '7':
        x[0] -= 1
        x[1] += 1
    points.append([x[0],x[1]])

axis_x = []
axis_y = []

for i in points:
    axis_x.append(i[0])
    axis_y.append(i[1])

# normalise the points by parallel move the axis
min_x = min(axis_x)
min_y = min(axis_y)
len_x = max(axis_x) - min_x + 1
len_y = max(axis_y) - min_y + 1
if min_x < 0:
    for i in points:
        i[0] += -min_x

if min_y < 0:
    for i in points:
        i[1] += -min_y

# generate a graph full of "off"
graph = np.asarray([off] * len_x * len_y).reshape(len_y, len_x)

# change "off" to "on", or "on" to "off" follow the given rule
for i in points:
    if graph[i[1]][i[0]] == off:
        graph[i[1]][i[0]] = on
    else:
        graph[i[1]][i[0]] = off

# reverse the matrix and print or print in reverse order
if graph.shape[1] == 1:
    order = graph.shape[0] - 1
    for i in graph[::-1]:
        if i[0] == on:
            break
        order -= 1
    if order >= 0:
        for i in graph[order::-1]:
            print(''.join(i))
else:
    for i in graph[::-1]:
        print(''.join(i))










# print(x)