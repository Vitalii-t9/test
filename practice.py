# Exercises by python book

# x = 10
# if x>0:
#     print("1")
# else:
#     print("-1")

# x = 5
# y = 9
#
# if x > y:
#     z = x - y
# elif x < y:
#     z = x + y
# else:
#     z = x
# print(z)

# apple = 1
# pear = 2
# orange = 3

# if apple > pear and pear < orange:
#     print("First case")
# elif apple < pear and pear > orange:
#     print("Second case")
# elif apple < orange and pear < orange:
#     print("Third case")
# else:
#     print("Anyone case not happened")

# fib1 = 0
# fib2 = 1
# n = 21
# i = 0
# fib_list = []
# while i < n:
#     fib_sum = fib1 + fib2
#     if 4 <= i <= 20:
#         fib_list.append(fib_sum)
#     fib1 = fib2
#     fib2 = fib_sum
#     i += 1
# print(fib_list)

# i = -1
# n = -21
# while i >= n:
#     if i % 3 == 0:
#         print(i)
#     i -= 1

# name = input("What is your name?: ")
# age = input("How old are you?: ")
# live_in = input("Where are you live?: ")
# print("This is "+name)
# print("It is "+age)
# print("He live in "+live_in)

# ex = "4*100-54 = "
# answ = "346"
# n = 1
# while n:
#     user_answer = input("Try to solve this: " + ex)
#     if user_answer == answ:
#         print("Congrats!!! You are right!!!")
#         n = 0
#     else:
#         print("You are wrong! Try again)")

# phrase = "This is my bike"
# # print(phrase[0], phrase[-1], phrase[2], phrase[-3], len(phrase))
# print(phrase[:7], phrase[5:10])
# i = 0
# while i < len(phrase):
#     if i % 3 == 0:
#         print(phrase[i])
#     i += 1

# f_list = [1, 2, 3, 4, 5, 6]
# s_list = ["one", "two", "three", "four", "five", "six"]
# print(f_list[1])
# s_list[-1] = "last_item"
# print(s_list)
# c_list = f_list + s_list
# print(c_list)
# x_list = c_list[3:9]
# print(x_list)
# x_list += ["new1", "new2"] or x_list[6:7] = ["new1", "new2"]
# print(x_list)

# school = {"1a": 15, "2a": 20, "3a": 12, "4a": 16, "5a": 11, "6a": 23, "7a": 32, "8a": 17, "9a": 26, "10a": 34}
# print(school)
# print("In 4a class "+str(school["4a"])+" students")
# school["2a"], school["3a"], school["4a"] = 1, 3, 5
# print(school)
# del(school["6a"])
# print(school)

# x_list = ["This is first", "This is second", "this is third", "This is fourth"]
#
# for i in x_list:
#     for n in i:
#         print(n, end="-")
#     print()
# x = [1, 2, 3, 44, 54]
#
# for i in range(len(x)):
#     x[i] = float(x[i])
# print(x)


# def countSum():
#     a = int(input("Please enter a first number: "))
#     b = int(input("Please enter a second number: "))
#     c = int(input("Please enter a third number: "))
#     return a+b+c
# f = countSum()
# print(f)

# def funcOne():
#     print("funcOne was launched")
#     def funcTwo():
#         print("funcTwo was launched")
#     return funcTwo()
# funcOne()

# n = 10
# def fun1(num):
#     n = num * 5
#     print(n)
#
# fun1(5)
# fun1(n)
# fun1("Hi")

# def func(n):
#     if n < 3:
#         n *= 10
#         return n
# a = 4
# b = func(a)
# print(b)

# 1. ?????????????????? ?????????????????????? ???????????? ?????????? ?????? 1 ???? 9. ???????????????? ???????? ?????????????????? ?????????????? x.
# 2. ???????? ???????????????????? ???????? ?????????? ?????? 1 ???? 3 ??????????????, ???? ...
# ??? ?????????????????? ???????????? ??????????. ???????????????? ???????? ?????????????????? ?????????????? s;
# ??? ?????????????????? ?????????????????????? ???????????? ?????????? ???????????????? ??????????. ???????????????? ???????? ?????????????????? ??????????????
# n, ???????????????????? ???????????????????????? ???? ?? ?????????????????????????? ??????;
# ??? ???????????????? ???????? ???????????????????? ?????????? n ??????????;
# ??? 2.4 ?????????????? ?????????????????? ???????????? ??????????.
# 3. ???????? ???????????????????? ???????? ?????????? ?????? 4 ???? 6 ??????????????, ???? ...
# ??? ?????????????????? ?????????????????????? ???????????? ??????????????, ???? ???????? ???????? ???????????? ??????????. ???????????????? ????????
# ?????????????????? ?????????????? m;
# ??? ?????????????????????? ???????????????? ?????????? x ???? ?????????????? m;
# ??? ?????????????? ?????????????????? ??????????????????.
# 4. ???????? ???????????????????? ???????? ?????????? ?????? 7 ???? 9 ??????????????, ???? ???????????????????? ???????????????????? ?????????? x ????
# ?????????????? ?? ?????????? 10 ??????????, ?????? ?????????? ???? ?????????? ???????????????? ?????? 10 ??????????.
# 5. ?? ???????? ?????????? ???????????????? ???????????????? ?????????? "?????????????? ????????????????".
# x = 1
# while x:
#     x = int(input("Please enter int from 1 to 9: "))
#
#     if 1 <= x <= 3:
#         s = input("Please enter any string: ")
#         n = int(input("How much times do you want to repeat this string? Please enter a number : "))
#         l = s
#         for i in range(n-1):
#             s += l
#         print(s)
#
#     elif 4 <= x <= 6:
#         m = int(input("Enter the degree to which your number will be raised: "))
#         x = x**m
#         print(x)
#     elif 7 <= x <= 9:
#         for i in range(10):
#             x += 1
#             print(x)
#     else:
#         print("Invalid number!!!")
#
#     while x:
#         rep = input("Do yo want try again? yes/no: ")
#         if rep.lower().startswith("y"):
#             break
#         elif rep.lower().startswith("n"):
#             print("Thanks, goodbye!!!")
#             x = 0
#         else:
#             print("Please enter the correct answer!!!")

# ???????????????? ????????????????, ?????? ?? ???????????????????? ???????? ????????????????:
# 1. ???????????????? ?????????? ???????????????? "?????????????????????? ???? ?????????????? XXI ????????????????";
# 2. ???????????????????? ?? ?????????????????????? ???????? ??????;
# 3. ???????? ???????????????????? ?????????????? ?????????? ?????? 0 ???? 7, ???? ???????????????? ???????????????? ?????????? "?????? ????
# ???????????????? ??????????????";
# 4. ?????? 7 ???? 18 - "?????? ???? ??????????";
# 5. ?????? 18 ???? 25 - "?????? ?? ?????????????????????? ???????????????????? ????????????";
# 6. ?????? 25 ???? 60 - "?????? ???? ????????????";
# 7. ?????? 60 ???? 120 - "?????? ?????????????????? ??????????";
# 8. ?????????? 0 ?????? ???????????? 120 - ??'?????????????????? ?????????????????? ???????????? "??????????????! ???? ???????????????? ??????
# ??????????! "
# ?? ???????????????? ???????????? ?????????????????????????????? ?????? "????????????????" ???????????????????????? ??????????????????????????: ??????????????,
# ???????????????????????? ?? ????????.

# def askAge():
#
#     while True:
#         users_age = input("How old are you?: ")
#         if not users_age.isnumeric():
#             print("Error!!! You can enter only int numbers!!!")
#         else:
#             break
#     return int(users_age)
#
#
#
#
# def respOninput(x):
#     if 0 <= x < 7:
#         print("?????? ???? ???????????????? ??????????????")
#     elif 7 <= x < 18:
#         print("?????? ???? ??????????")
#     elif 18 <= x < 25:
#         print("?????? ?? ?????????????????????? ???????????????????? ????????????")
#     elif 25 <= x < 60:
#         print("?????? ???? ????????????")
#     elif 60 <= x < 120:
#         print("?????? ?????????????????? ??????????")
#     else:
#         print("??????????????! ???? ???????????????? ?????? ??????????! "*5)
#
# print("Welcome to '?????????????????????? ???? ?????????????? XXI ????????????????")
# x = 1
# while x:
#     respOninput(askAge())
#     while True:
#         rep = input("Do yo want try again? yes/no: ")
#         if rep.lower().startswith("y"):
#             break
#         elif rep.lower().startswith("n"):
#             print("Thanks, goodbye!!!")
#             x = 0
#             break
#         else:
#             print("Try again!!! You can enter only yes or no!")


# D = {1: 'a', 2: 'b', 3: 'c'}
# print(tuple(D.values()))
# print(D.keys())
# print(D.items())

# keys = ['spam', 'eggs', 'toast']
# vals = [1, 3, 5]
# D3 = dict(zip(keys, vals))
# m = max(1, 45, 32)
# print(m)


# def sorta_sum(a, b):
#   if a+b in list(range(10, 20)):
#     return 20
#   return a+b
#
# sorta_sum(1,4)
# sorta_sum(10,5)

# def near_ten(num):
#   l = [-2, -1, 0, 1, 2]
#   for i in l:
#     if (num+i) %10 == 0:
#       return True
#     return False

# m = [1, 2, 3]
# print(sum(m))
# del(m[0], m[1])
# print(m)
# print(sum(m))

# lis = [1, 13, 2, 13]
#
# print(lis.index(13))
# print(lis[:0])

# m = 'catdog'
# print(m.count("cat"))

# n = "cozexxcope"
#
# print(n.)

# def count_code(str):
#   x = ["co" + i + "e" for i in str]
#   count = 0
#   for i in x:
#     if i in str:
#       count += str.count(i)
#
#   return count
#
# print(count_code("cozefarcodegdhrcone"))

# m = "gf"
# print(m[0])
# m.is

# def xyz_there(str):
#   if len(str) == 3 and str == "xyz":
#     return True
#
#   elif len(str) > 3:
#     m = []
#
#     for i in range(len(str)):
#       m.append(str[i:i + 4])
#       if str[i] == ".":
#
#
#
#     for n in m:
#
#       if ((n[0].isalpha() or n[0].isdigit()) and n[1:] == "xyz") or n[:3] == 'xyz':
#         return True
#
#       elif (n[0] == "." and n[1:] == "xyz") or "xyz" not in str:
#         return False
#
#   else:
#     return False
#
# print(xyz_there('1.xyz.xyz2.xyz'))
# m = [1,2,34]
# print(m)
# del(m[m.index(1):m.index(1)+2])
# print(m)

# def sum13(nums):
#   nl = nums
#
#   for i in range(len(nl)):
#     if nl[i] == 13:
#       del (nl[nl.index(i):nl.index(i) + 2])
#       print(nl)
#   return sum(nl)

# m = [1, 3, 4, 13, 12, 12, 32, 1, 13]
#
# print(m.index(13))
# print(m.index(13))

# L = [1, 2]
# b = L
# print(L)
# b[0] = "new"
# print(L)

# def output(a:int):
#     print(a)
#
# print(output.__annotations__)

# def action(x):
#     print(x)
#     return (lambda y: x+y)
#
#
# print(action(5)(4))
#
# MAP Function
# L = range(-10, 10)
# def sum_numbers(x):
#     return x + 5
# K = list(map(sum_numbers, L))
# print(K)

# Filter Function
# L = range(10,1000)
#
# def devided_by_2(x):
#     if x % 101 == 0:
#         return x
# O = list(filter(devided_by_2, L))
# print(O)
from functools import reduce
print(reduce((lambda x, y: x + y), [], 0))