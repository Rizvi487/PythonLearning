# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers, return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# def ProductSum(number1, number2):
#     # number1 = int(input("Enter the number: "))
#     # number2 = int(input("Enter the number: "))
#     if number1 * number2 <= 1000:
#         product = number1 * number2
#         print(f'The result is ',product)
#     else:
#         Sum = number1 + number2
#         print(f'The result is ',Sum)
#
#
# ProductSum(20, 30)
# # ProductSum(40,30)

# Exercise 2: Print the sum of the current number and the previous number

# print("Printing current and previous number sum in a range(10)")
# Prev_Num = 0
# for i in range(0,11):
#     sum = Prev_Num + i
#     print("Current Number", i, "Previous Number", Prev_Num, "Sum: ", sum)
#     Prev_Num = i

# Exercise 3: Print characters from a string that are present at an even index number

# def EvenChar(Word):
#     print("Original String is: ", Word)
#     list_word = list(Word)
#     # print(list_word)
#     print("Printing only even index chars")
#     for i in list_word[::2]:
#         print(i)
#
# # EvenChar("Rizwan")
# EvenChar("pynative")

# Exercise 4: Remove first n characters from a string
#
# def remove_chars(Word, n):
#     print("Original String: ", Word)
#     x = Word[n:]
#     return x
# print("Removing characters from a string")
# # print(remove_chars("Rizwan",3 ))
# # print(remove_chars("Rizwan",))
# Exercise 5: Check if the first and last number of a list is the same

# def FirstLast(lists):
#     print("Given List: ", lists)
#     first_num = lists[0]
#     last_num = lists[-1]
#     if first_num == last_num:
#         return True
#     else:
#         return False
# lists = [10, 20, 30, 40, 9]
# print("result is", FirstLast(lists))

# Exercise 6: Display numbers divisible by 5 from a list

# def DivBy5(lists):
#     print("Given List is : ", lists)
#     print("Divisble by 5: ")
#     for num in lists:
#         if num % 5 == 0:
#             print(num)
#     else:
#         print('There are no numbers divisible by 5 in the given list')
#
# # DivBy5([1,2,20,5])
# DivBy5([8,3,2])

# Exercise 7: Return the count of a given substring from a string

# def count_str(statement):
#     print("Given String: ", statement)
#     count = 0
#     for i in range(len(statement)-1):
#         count += statement[i:i+4] == 'Emma'
#     return count
# count = count_str("Emma is good developer. Emma is a writer")
# print("Emma appeared ", count, "times")
#
# # count = count_str("Rizwan is good boy. Rizwan is great")
# # print("Rizwan appeared ", count, "times")

# Exercise 8: Print the following pattern
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

# for i in range(6):
#     for j in range(i):
#         print(i,end=" ")
#     print("\n")

# Exercise 9: Check Palindrome Number

# def PalindromeCheck(num):
#     print("Original number: ", num)
#     original_num = num
#     rev_num = 0
#     while num > 0:
#         remain = num % 10
#         rev_num = (rev_num * 10) + remain
#         num = num //10
#     if original_num == rev_num:
#         print('Given num is Palindrome')
#     else:
#         print('Given num is not Palindrome')
#
# PalindromeCheck(151)
# Exercise 10: Create a new list from two list using the following condition

# def New_list(list1, list2):
#     result_list = []
#     for num in list1:
#         if num % 2 != 0:
#             result_list.append(num)
# #             # print(result_list)
# #     for num in list2:
# #         if num % 2 == 0:
# #             result_list.append(num)
# #
# #     return result_list
# #
# # list1 = [10, 20, 25, 30, 35]
# # list2 = [40, 45, 60, 75, 90]
# # print(New_list(list1, list2))
#
# # Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# #
# # def revNum(num):
# #     print("Given Number ", num)
# #     while num > 0:
# #         digit = num % 10
# #         num = num // 10
# #         print(digit, end="")
# #
# # # revNum(7536)
# # revNum(8127)
#
# # Exercise 12: Calculate income tax for the given income by adhering to the rules below
# # def calculateTax(income):
# #     tax_payable = 0
# #     if income <= 10000:
# #         tax_payable = 0
# #     elif income <= 20000:
# #         x = income - 10000
# #         tax_payable = x * 10/100
# #     else:
# #         tax_payable = 0
# #         tax_payable = 10000 * 10 / 100
# #         tax_payable += (income - 20000) * 20 / 100
# #
# #     print("Total tax to pay is", tax_payable)
# #
# # calculateTax(45000)
# # calculateTax(40000)
# # Exercise 13: Print multiplication table from 1 to 10
# # for i in range(1, 11):
# #     # print(i)
# #     for j in range(1,11):
# #         print(i * j, end=" ")
# #     print("\t\t")
# # Exercise 14: Print a downward Half-Pyramid Pattern of Star (asterisk)
# # for i in range(6, 0, -1):
# #     print(i)
# #     for j in range(0, i - 1):
# #         print(j)
# #         # print("*", end=" ")
# #     print("\n")
# # Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# def exponent(base, exp):
#     result = pow(base,exp)
#     print("base= ", base)
#     print("exponent= ", exp)
#     print(base, " raises to the power of ", exp, ":", result)
#
# exponent(2,5)
# exponent(5,4)

