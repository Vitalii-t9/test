# The different ways to create dictionary
# a = dict(a=0, b=0)
# b = {key:0 for key in "ab"}
# c = dict.fromkeys(["a", "b"], 0)
#
# print(a, b, c)

# The ways to interface with lists
# x = [1, 2, 3, 4, 5]
# del(x[:2])
# x.pop()
# x.append([6, 7, 8])
# x.remove(4)
# print(x)

# t = (1, 2, 3, 4, 5)
#
# print((t[0], t[1:3]))

# myfile = open('text.txt', 'w')
# myfile.write("Hello how are you\n")
# myfile.close()
# myfile = open('text.txt')
# myfile.readline()
#
# >>> X, Y, Z = 43, 44, 45 # Объекты языка Python должны
# >>> S = ‘Spam’ # записываться в файл только в виде строк
# >>> D = {‘a’: 1, ‘b’: 2}
# >>> L = [1, 2, 3]
# >>>
# >>> F = open(‘datafile.txt’, ‘w’) # Создает файл для записи
# >>> F.write(S + ‘\n’) # Строки завершаются символом \n
# >>> F.write(‘%s,%s,%s\n’ % (X, Y, Z)) # Преобразует числа в строки
# >>> F.write(str(L) + ‘$’ + str(D) + ‘\n’) # Преобразует и разделяет символом $
# >>> F.close()

# x = 1, 2, 3, 4, 5
#
# print(type(x))
# print(x)

#
# x = 'spam'
# y = 'eggs'
# print(x, y)
# x, y = y, x
# print(x, y)
#
# D = {1: 'a', 2: 'b'}
# print(D)
# D[3] = "c"
# pri

# import os
# import sys
#
# print(sys.prefix)
#
# print(os.getlogin())

# S = "spam"
# print(S)
# S = "sl" + S[2] + S[3]
# print(S)

# my_file = open('myfile.txt', 'w+')
# my_file.write(" Hello there!!\n How are you?\n Everything is fine))")
# my_file.close()
# my_file = open('myfile.txt')
# print(my_file.read())

# x = [1, 2, 3]
# for i in x:
#     print('hi', end='--')

# while True:
#     reply = input('Enter text:')
#     if reply == 'stop': break
#     try:
#         num = int(reply)
#     except:
#         print('Bad!' * 8)
#     else:
#         print(int(reply) ** 2)
# print('Bye')

# print(x, y, z, sep=’, ‘)

# S = "ABCDEIFGKLMNOPRSTQXYZ"
# s = []
# print(len(S))
# for i in S:
#     s.append(ord(i))
# print(s)
#
# sm = map(ord, S)
#
# print(sm)
# print(sm.__next__())
# print(sm.__next__())
# print(sm.__next__())

# for i in range(50):
#     print('hello %d\n\a' % 1)

# dic = dict(a=23, b=48, c=432, d=393993, e=12)
# print(dic)
# print(dic.values())
# keys = sorted(dic.values())
# print(keys)

L = [1, 2, 4, 8, 16, 32, 64]
x = 5
i = 0
# while i < len(L):
#     if 2**x == L[i]:
#         print("at index", i)
#         break
#     elif i == len(L)-1 and 2**x != L[i]:
#         print("x not found")
#         break
#     else:
#         i += 1

# for i in L:
#     if i == 2**x:
#         print("at index", L.index(i))
#         break
#     elif i == L[-1] and L[-1] != 2**x:
#         print("x not found")

# if 2**x in L:
#     print("at index", L.index(2**x))
# else:
#     print("x not found")

# K = [2**x for x in range(7)]
# print(K)