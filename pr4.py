# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:50:20 2018
@author: bii
"""

array_size = int(input("Please input array size: "))
array = []

for i in range (0, array_size):
    a,b = map(int, input().split())
    if a < b:
        array.append(a)
    else:
        array.append(b)

print("\nAnswer:")

for i in range (0, array_size):
        print(array[i])