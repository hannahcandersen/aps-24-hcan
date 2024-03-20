"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/cqrk6f/problems/exactchange2
Author: Hannah Camilla Andersen (hcan)
Date:  17/02 2024

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

t = int(input())

def solve(target, coins):
    solutions = {0: 0}

    for coin in coins:
        # Loop through all the prices we have calculated so far
        for price, coins_needed in list(solutions.items()):
            # If we make use of the current coin, we get a different solution
            new_price = price + coin
            new_amount = coins_needed + 1
            # This solution would not be interesting because it exceeds the maximum output size (very important as otherwise the dictionary becomes too big.)
            if new_price > target + max(coins):
                continue
            # Store solution if (a) we have not seen this price before, or (b) it's better than the currently best known solution.
            if new_price not in solutions or solutions[new_price] > new_amount:
                solutions[new_price] = new_amount

    # Search for the first entry that is at least target price in the solution
    for i in range(target, max(solutions) + 1):
        if i in solutions:
            return f"{i} {solutions[i]}"

for _ in range(t):
    price = int(input())
    n = int(input())

    coins = [int(input()) for _ in range(n)]

    print(solve(price, coins))