"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/cqrk6f/problems/rijeci
Author: Hannah Camilla Andersen (hcan)
Date:  17/02 2024

Description:
The machine first displays the word A.
After he pressed the button the first time, the word changed to B
After he pressed the button the second time, the word changed to BA
The machine alters the word in a way that 
all the letters B get transformed to BA 
and all the letters A get transformed to B.
- Input:
    - K: Number of times the button is pressed (1 <= K <= 45)
- Output:
    - After K times of pressing the button, how many letters A and how much letters B will be displayed on the screen?
"""

from functools import lru_cache

@lru_cache(maxsize=None) # Memoization
def solve(k):
    # Base case:
    if k == 1: # A -> B
        return 0, 1
    if k == 2: # B -> BA
        return 1, 1
    
    ## Recursive case:
    # B -> BA. Therefore A becomes the number of previous B's
    # A -> B. Therefore B grows with the number of previous A's
    a_prev, b_prev = solve(k-1)
    return b_prev, a_prev + b_prev

k = int(input())
a, b = solve(k)
print(a, b)

