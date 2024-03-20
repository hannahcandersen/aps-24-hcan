"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/cqrk6f/problems/orders
Author: Hannah Camilla Andersen (hcan)
Date:  14/02 2024

Description:
Find out what was ordered given the total cost of the order and the cost of each item on the menu.
- Input:
    - N: Number of items on the menu (1 <= N <= 100)
    - List of N * c: Cost of each item (0 <= c <= 1000)
    - M: Number of orders (1 <= M <= 1000)
    - List of M * s: Total cost of each order (1 <= s <= 30000) 
- Output:
    - For each order in the input output one line as follows. 
      If there is one unique order giving the specified total cost, 
      output a space-separated list of the numbers of the items on that order in ascending order.
      If the order contains more than one of the same item, print the corresponding number the appropriate number of times. 
      The first item on the menu has number 1, the second 2, and so on.
      If there doesn’t exist an order that gives the specified sum, output Impossible. 
      If there are more than one order that gives the specified sum, output Ambiguous.
"""
import sys
sys.setrecursionlimit(10**6)


def find_order(originalPrice, p, currentOrder, index, num_of_valid_orders, valid_order):
    """
    Args:
        originalPrice (int): Original price we are trying to find order for
        p (int): Current price we are trying to find order for
        currentOrder (list): Current order being constructed
        index (int): Index of the current item we are considering from menu
        num_of_valid_orders (list): List to store the number of valid orders for each price
        valid_order (list): List to store the valid orders for each price
    """
    global N, menu
    
    # Base case: Price is negative
    if p < 0:
        return 
    
    # Base case: We have found a valid order
    if p == 0:
        num_of_valid_orders[originalPrice] += 1
        valid_order[originalPrice] = currentOrder
        return 
    
    # Base case: We have considered all items
    elif index == N:
        return 
    
    # Memoization: Check if we have already calculated the number of valid orders for the current price
    if num_of_valid_orders[p] != 0:
        return 
    
    # Recursive case: We can either use the current item or not
    ## Dont use it, check next item on menu
    find_order(originalPrice, p, currentOrder, index + 1, num_of_valid_orders, valid_order)
    ## Use it, add to current order and check same item on menu again 
    find_order(originalPrice, p - menu[index], currentOrder + [index + 1], index, num_of_valid_orders, valid_order)
    
    return 


N = int(input())
menu = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))
maxOrder = max(orders)

# Memoization - reuse for all orders
num_of_valid_orders = [0] * (maxOrder+1)      
valid_order = [[] for _ in range(maxOrder+1)] 

# Process orders
for order in orders:
    find_order(order, order, [], 0, num_of_valid_orders, valid_order) 
   
    if num_of_valid_orders[order] > 1:
        print("Ambiguous")
    elif num_of_valid_orders[order] == 0:
        print("Impossible")
    else:
        print(" ".join(str(x) for x in valid_order[order]))