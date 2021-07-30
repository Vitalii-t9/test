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

apple = 1
pear = 2
orange = 3

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


def countSum():
    a = int(input("Please enter a first number: "))
    b = int(input("Please enter a second number: "))
    c = int(input("Please enter a third number: "))
    return a+b+c
f = countSum()
print(f)












