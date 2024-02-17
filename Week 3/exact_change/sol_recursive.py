"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/cqrk6f/problems/exactchange2
Author: Hannah Camilla Andersen (hcan)
Date:  14/02 2024

Description:
If the cashier has no change, while paying the minimum amount, 
you would also like to minimize the number of coins or bills that you pay out.
- Input:
    - T: Number of test cases
    - T * Test cases: 
        - P: Target price (max 10.000)
        - N: Number of coins (max 100)
        - N * V: Values of each coin (max 10.000) 
- Output:
    - For each test case, output a single line containing two integers: the total amount paid (in cents), 
      and the total number of coins and bills used.
      
Does not pass on Kattis because of time limit exceeded.
"""

from functools import lru_cache

MAX_VALUE = 10000000

@lru_cache(maxsize=None)
def recursion(target, i):
    # Base case: we can always achieve the price 0 with 0 coins
    if target == 0:
        return 0
    # Base case: we can not achieve a negative price, or ran out of coins
    if target < 0 or i < 0:
        return MAX_VALUE
    a = recursion(target, i - 1)
    b = recursion(target - coins[i], i - 1)
    # Take the minimum of the two cases
    if a < b + 1:
        return a
    return b + 1
    
# Loop through all possible prices from the target price to the target price + the maximum coin value
# Return first (lowest) price that can be achieved with the fewest coins
def solve_recursively(goal, coins):
    #print(goal, coins)
    for i in range(goal, goal + max(coins)):
        val = recursion(i, len(coins) - 1)
        if val < MAX_VALUE:
            return f"{i} {val}"
        
    
t = int(input())

for _ in range(t):
    goal = int(input())
    n = int(input())

    coins = [int(input()) for _ in range(n)]

    #print(coins)

    print(solve_recursively(goal, coins))
    # important: clear the solution cache after each test case
    recursion.cache_clear()