# -*- coding: utf-8 -*-
"""
Created: 2/14/18
Author: bii
"""
#test
#Takes size of the array as input
array_size = int(input("Please input array size: "))

#Initializes an empty array named 'array'
array = []

#Takes
for i in range (array_size):
    a,b = map(int, input().split())
    if (abs((a / b)) % 1 >= 0.5):
        array.append(round(a / b))
    else:
        array.append(a / b)

print()

for i in range (0, array_size):
    print(int(array[i]))