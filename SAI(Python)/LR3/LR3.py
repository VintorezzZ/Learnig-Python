# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 20:47:12 2020

@author: VintorezzZ
"""


# 1.1



# def CelsiusToFahrenheit(tc):
#     tf = 9/5 * tc + 32
#     return tf

# while True:
#     try:
#         tc = float(input('Input a Celsius degrees: '))
#     except ValueError:
#         print("Entered incorrect number, try again")
#         continue
#     else:
#         break  

# tf = CelsiusToFahrenheit(tc)
# print(str(tc) + ' tc = ' + str(tf) + ' tf')


# 1.2


# def func(*arr):
#     count = len(arr)
#     summ = 0
#     for i in arr:
#         summ += i
#     sr_arifm = summ/count
#     a = sr_arifm/count
#     print('\nCount of elements:',count)
#     print('Sum of elements:',summ)
#     print('Srednee arifmeticheskoe:',sr_arifm)
#     return a

# print('Отношение их среднеарифметического значения к диапазону изменения элементов',func(1,2,3,4,5))
    

# 1.3


# def IsPalindrom(s):
#     if s == s [::-1]:
#         print(str(s) + ' = ' + str(s [::-1]) +' \nThis is a palindrom')
#     else:
#          print(str(s) + ' = ' + str(s [::-1]) +' \nThis is not a palindrom')

# IsPalindrom('топот')


# 1.4


# import myModule

# myModule.PloshadOfTriangle()


# 1.5


# import sys

# def IsUnique(*nums):
#     print('\n' + str(nums))
#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] == nums[j]:
#                 print("\nЕсть одинаковые")
#                 sys.exit()
#     print('\nВсе числа уникальны')
            
# IsUnique(1,2,3,4,5,6,6)



