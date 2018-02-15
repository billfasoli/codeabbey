# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 21:50:20 2018
@author: bii
"""

#Take the inital input size of the array
array_size = int(input("Please input array size: "))

#Take the initial array as a single string
array = input("Please input array: ")
#Use list comprehension to convert string input into array
array = [int(i) for i in array.split()]

#Sums up all elements of the array
array_sum = 0
for i in range (array_size):
    array_sum = array_sum + array[i]

#Prints the sum of the array
print("The sum of the array is: ", array_sum)