# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:50:20 2018
@author: bill
"""

#Takes size of the array as input
array_size = int(input("Please input array size: "))

#Initializes an empty array named 'array'
array = []

#Takes each 'triplet' element of the array and compares
#it against each other triplet to find the lowest
#value and assigns lowest value to the array element
for i in range (array_size):
    a,b,c = map(int, input().split())
    if (a <= b) and (a <= c):
        array.append(a)
    else:
        if b <= c: 
            array.append(b)
        else: 
            array.append(c)
    
#Comment the white space
print("\nAnswer:")

#Prints the array
for i in range (array_size):
        print(array[i])
