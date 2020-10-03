# -*- coding: utf-8 -*-


# 1.1


# surname = input("Input your surname: ").capitalize()
# name = input("Input your name: ").capitalize()
# patronymic = input("Input your patronymic: ").capitalize()

# while True:
#     try:
#         yearOfAdmission = int(input("Input year of admission: "))
#     except ValueError:
#         print("Entered incorrect number, try again")
#         continue
#     else:
#         break

# diplomBacalavra = yearOfAdmission + 4
# magistrDisert = diplomBacalavra + 2

# nickname = (surname [::-1]).capitalize()

# print('\nSurname: {0} \nName: {1} \nPatronymic: {2} \
#         \nДиплом бакалавра Вы получите в {3} году \
#         \nЗащита магистерской диссертации может состояться в {4} году \
#         \nПсевдоним {5}'.format(surname, name, patronymic, diplomBacalavra, magistrDisert, nickname))


# 1.2
       
       
# string = "this is the biggest string you've ever seen"
# print(string) 
# lenght =  len(string)              
# print('Длина строки:',lenght)
# print('Первый символ:',string[0])
# print('Последний символ:',string[-1])
# print('Третий символ с начала:',string[2])
# print('Третий символ с конца:',string[-3])
# print('Первые 8 символов:',string[0:8])
# center = int(lenght/2)
# print('4 символа из центра:',string[center:center + 4])
# print('Символы с индексами кратными 3м:',string[::3])
# count = string.count(string[0])
# print('Количество вхождений первого символа:',count)


# 1.3


# groups = {'3711':12,'3712K':17,'3713K':20,'3721':21,'3715':15}

# print(groups)

# groups['3711'] = 11
# groups['3712K'] = 45
# groups['3713K'] = 32

# print(groups)

# groups['4712'] = 9
# groups['4613'] = 14

# print(groups)

# del groups['3712K']

# print(groups)

# print('Студентов в 4613 группе:',groups['4613'])


# 1.4


# s = """ У лукоморья дуб зелёный,
#  Златая цепь на дубе том. """
 
# print(s)
 
# number = s.count('у')
# print('\nБуква "у" встречается ' + str(number) + ' раза')

# def find_all(a_string, sub):
#     result = []
#     k = 0
#     while k < len(a_string):
#         k = a_string.find(sub, k)
#         if k == -1:
#             return result
#         else:
#             result.append(k)
#             k += 1 #change to k += len(sub) to not search overlapping results
#     return result


# print('Буква "у" встречается в этих индексах: ',find_all(s, 'у'))


# 1.5


# string = input("Input numbers separated by commas: ")

# print('\nEntered string:',string)

# lst = string.split(',')

# print('\nSplit string by commons and create a new array:',lst)

# print('\nSum of the first and last element of the array:',int(lst[0]) + int(lst[-1]))


# 1.6


# while True:
#     try:
#         arrayOfNums = int(input("Input a three-digit number: "))
#     except ValueError:
#         print("Entered incorrect number, try again")
#         continue
#     else:
#         break

# print('\nEntered number:',arrayOfNums)
    
# arrayOfNums = str(arrayOfNums)    
    
# lst = list(arrayOfNums)

# print('\nConvert the array to str array:',lst)
    
# lst = [int(i)for i in lst]

# print('\nConvert the str array to int array:',lst)


# print('\nSum of the digits:',sum(lst))


