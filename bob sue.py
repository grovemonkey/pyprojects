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
#     # print(person)
#     # print(person[0].split()[-1])
#     # person[2] *= 2
#     print(person[2])

# while True:
#     print('Type UserName')
#     name = input()
#     if name != 'grovemonkey':
#         continue
#     print('hello, sam. what is the password? (it is a fish)')
#     password = input()
#     if password == 'bean':
#         break
# print('access granted')
# name = ''
# while not name:
#     print('enter your name: ')
#     name = input()
# print('how many will youhave?')
# numofguest = int(input())
# if numofguest:

# open the file
# search all the words line by line
# find words with len >= 20
# print those words
# line = []
# linenum = 0 #starting point for the search
# with open('C:/Users/Bill Smith/Documents/Python Scripts/words.txt') as myfile:
#     for line in myfile:
#         linenum += 1
#         if len(line) >= 20:
#             print(line)
#         else:
#             continue


def avoids(word, forbidden):
    for letter in word[2]:
        if letter in forbidden:
            print(letter)
            return False
        return True

def uses_only(word, available): #checks if left is in right uses_only('testing', eeetesting) it will return True
    for xw in word:
        if xw not in available:
            return False
        return True
def uses_all(word, required):# right is in left('testing", 'eeetesting') will return False
    for letter in required:
        if letter not in word:
            return False
        return True
def is_abecedarian(word):
    previous = word[0]
    for c in word:
        if c < previous:
            print(word)
            return False
        previous = c
    return True

addr = 'monty@python.org'
uname, domain = addr.split('@')


def min_max(t):
    return min(t), max(t)

dope = 5000
s = [0, 1, 2]
t = [0, 1, 2]

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False


d = dict(zip('abcdef', range(5)))
for key, val in d.items():
    print (val, key)
    


