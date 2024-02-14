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
"""

# TODO: Fix så den også finder den laveste sum det er muligt at få

def solve(x, coins): 
    """
    Recursively find the minimum number of coins needed to reach the minimum sum obtained by using the available coins.
    Iterate over each coin and compare the minimum number of coins needed using or not using the current coin.

    Args:
        x (int): Sum we are currently aiming for
        coins (int list): List of available coins
    """

    # Base case: Check if sum is negative 
    if x < 0:
        return float('inf')
    
    # Base case: Check if sum is 0
    if x == 0:
        return 0
    
    # Check if solve(x) has been calculated before
    if ready[x]:
        return value[x]
    
    # Iterate over each coin and find the minimum number of coins needed using or not using the current coin
    best = float('inf')
    for c in coins:
        # Update best to the minimum of its current value and solve(x-c) + 1 (earlier calculated + using one coin c)
        best = min(best, solve(x-c, coins) + 1)
    
    # Update ready and value for memoization
    ready[x] = True
    value[x] = best
        
    return best


# Handle test cases
t = int(input())
for _ in range(t):
    
    # For memoization: 
    ready = [False] * 10001           # True solution has been calculated before
    value = [float('inf')] * 10001    # Current minimum number of coins for target sums
    
    p = int(input())
    n = int(input())
    coins = []
    for _ in range(n):
        v = int(input())
        coins.append(v)
            
    # Find the smallest sum that is above price p 
    minSum = 0
    for i in range(p, len(value)):
        if value[i+p] < float('inf'):
            minSum = i
            break
    
    # Find the minimum amount paid and the total number of coins and bills used
    print(f"{minSum} {solve(10000, coins)}")
    