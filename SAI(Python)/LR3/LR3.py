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


# 1.6


# import time

# print('\ntime.time():',time.time())

# seconds = time.time()
# minutes = seconds/60
# hours = minutes/60
# days = hours/24
    
# print("\nдни : {0}  часы : {1}  минуты : {2}  секунды: {3}".
#       format(round(days), round(hours), round(minutes), round(seconds)))


# 1.7


# import time

# d = [ "понедельник", "вторник", "среда", "четверг",
#  "пятница", "суббота", "воскресенье" ]
# m = [ "", "января", "февраля", "марта", "апреля", "мая",
#  "июня", "июля", "августа", "сентября", "октября",
#  "ноября", "декабря" ]
# t = time.localtime() # Получаем текущее время
# print( "\nСегодня: %s %s %s %s %02d:%02d:%02d" %
#  ( d[t[6]], t[2], m[t[1]], t[0], t[3], t[4], t[5]))















