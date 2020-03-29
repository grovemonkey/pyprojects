# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 19:52:02 2019

@author: Bill Smith
"""

#rock paper scissors

# for num in range (2, 1000, 3):
#     for x in range (2, num):
#         if num % x == 0:
#             print(num, 'equals', x, '*', num//x)
#             break
#     else:
# #         print(num, 'is a prime number')

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#         print(a, end = ' ')
#         a,b = b, a+b
#     print()
# # fib(10000)
# bob = ['bob smith', 42, 39999, 'software']
# sue = ['Sue smith', 49, 23444, 'hardware']
# people = [bob, sue]
# for person in people:
#     print(person)
#     print(person[0].split()[-1])
#     person[2] *= 2
#     print(person[2])

while True:
    print('Type UserName')
    name = input()
    if name != 'grovemonkey':
        continue
    print('hello, sam. what is the password? (it is a fish)')
    password = input()
    if password == 'bean':
        break
print('access granted')


      





