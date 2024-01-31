""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ouwzxz/problems/fizzbuzz
Author: Hannah Camilla Andersen (hcan)
Date:   30/01 2024

"""

input_lst = input().split()
x = int(input_lst[0])  # divisor 1 
y = int(input_lst[1])  # divisor 2
n = int(input_lst[2])  # count from 1 to N (1 <= X < Y <= N <= 100)

for i in range(1, n + 1): 
    if (i % x == 0) and (i % y == 0): 
        print("FizzBuzz")
    elif (i % x == 0): 
        print("Fizz")
    elif (i % y == 0):
        print("Buzz")
    else: 
        print(i)

    
 
