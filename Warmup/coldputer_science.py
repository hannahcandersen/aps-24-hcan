""" 
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/ouwzxz/problems/cold
Author: Hannah Camilla Andersen (hcan)
Date:   30/01 2024

Description: 
- Input: 
    N: Number of temperatures collected where 1 <= N <= 100
    t: N temperatures t where -1.000.000 <= t <= 1.000.000
- Output: 
    Number of temperatures strictly less than zero.
"""

n = input()
t_lst = list(map(int, input().split())) # Convert from list of strings to list of integers
days = 0 # Number of days with negative temperature

for t in t_lst: 
    if t < 0: 
        days += 1
        
print(days)
    
        

