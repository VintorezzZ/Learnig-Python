# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 10:38:29 2020

@author: VintorezzZ
"""

# 1.1 


# fib1 = 0
# fib2 = 1
# # print (fib1)
# # print (fib2)
# n = 100
# i = 0
# while i < n:
#         fib_sum = fib1 + fib2
        
#         if i > 2:
#             print (fib_sum)   
            
#         fib1 = fib2
#         fib2 = fib_sum
#         i += 1


# 1.2


# import numpy as np

# array = np.arange(21)
# print('\nGenerate an array from 0 to 20: ',array)

# array2 = []

# for i in array:
#     if array[i] % 2 == 0:
#         array2.append(array[i])
        
# print('\nOnly even numbers:',array2)

# array3 = np.arange(1, 22)
# array3 *= -1
# print('\nGenerate an array from -1 to -21:',array3)

# print('\nEvery third number:',array3[2::3])


# 1.3


# while True:
#     try:
#         x = float(input("Input X: "))
#     except ValueError:
#         print("Entered incorrect number, try again")
#         continue
#     else:
#         break    
    
# def Function(x):   
#     if x >= -2.4 and x <= 5.7:
#         x *= x
#     else:
#         x = 4     
#     print('Function(x) =',x)       
        
# Function(x)    
            

# 1.4


# array = []
# arr_full = []

# for i in range(0,10):
#     a = i * i + 3
#     arr_full.append(a)
#     if a > 10 and a < 30:
#         array.append(a)

# print('\nAll roots of equation in range(0, 10):',arr_full)
# print('\nEvery second roots in the interval from 10 to 30:',array[1::2])
    
    
# 1.5


# while True:
#     try:
#         number = float(input("Input number: "))
#     except ValueError:
#         print("Entered incorrect number, try again")
#         continue
#     else:
#         break    
    
# print('\nEntered number:',number)
# s = str(number).replace('.','')
# s = [int(i)for i in s]
# print('\nGet rid of the dot and add nums to the array:',s)

# summa = 0

# for i in s:
#     if i % 2 == 0:
#         i*=i
#         summa += i

# print('\nSum of squares of even numbers:',summa)

    
# 1.6


# print('\nInput the answer of this example: 4*100-54')

# while True:
#     try:
#         answer = input()
#         if answer == 'exit':
#             print('\nExit the programm...')
#             break
#         else:
#             answer = int(answer)
#     except ValueError:
#         print("Entered incorrect number, try again")
#         continue
#     else:
#         if answer > 346 and answer < 400:
#             print('Введено немного большее число')
#             continue
#         elif answer > 400:
#             print('Введено очень большое число')
#             continue
#         elif answer < 346 and answer > 300:
#             print('Введено немного меньшее число')
#             continue
#         elif answer < 300:
#             print('Введено очень малое число')
#             continue
#         else:
#             print('\nFinally! Good job.\nExit the programm...')
#             break
        
    

    
    
    
    
    
    
    