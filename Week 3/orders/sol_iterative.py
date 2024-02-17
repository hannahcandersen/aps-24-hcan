"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/cqrk6f/problems/orders
Author: Hannah Camilla Andersen (hcan)
Date:  17/02 2024

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

def solve(order_price):
    global menu, num_of_valid_orders, valid_order
    
    for menuIndex, menuPrice in enumerate(menu):
        
        # Loop through all the prices we have calculated so far
        for price, solutions in list(num_of_valid_orders.items()):
            new_order_price = price
            new_order = valid_order[price].copy()
            
            # Try adding this menu item x number of times until the new order price exceeds the order price
            while new_order_price <= order_price:
                new_order_price += menuPrice
                new_order.append(menuIndex + 1)
            
                # New price exceeds the price of the current order, and is not relevant (to avoid that the dictionary gets too big.)
                if new_order_price > order_price:
                    break
            
                ## The new price has not been seen before ##
                # Store the new order for the new price
                if new_order_price not in num_of_valid_orders: 
                    num_of_valid_orders[new_order_price] = 1
                    valid_order[new_order_price] = new_order.copy()

                ## The new price has been seen before ##
                # If the order is not the same as the current one, it is a new valid order. Needs to update number of valid orders
                if sorted(new_order) != sorted(valid_order[new_order_price]):
                    num_of_valid_orders[new_order_price] = 2
                    # Now there is at least two valid orders, so no need to store/update them

n = int(input())  # Number of items on the menu
menu = list(map(int, input().split())) 
m = int(input())  # Number of orders
orders = list(map(int, input().split()))
maxOrderPrice = max(orders) # Maximum price of an order

# Memoization - Reuse for all orders 
num_of_valid_orders = {}   # price -> number of valid orders
valid_order = {}           # price -> one valid order (list). Only contains one valid order, as we only need to know the order if there is only one valid order 

# Base case
num_of_valid_orders.update({0: 1})
valid_order.update({0: []})

# Handle each order
for i in range(m):
    price = orders[i]
    
    solve(price)
    
    if price not in num_of_valid_orders:
        print("Impossible")
    elif num_of_valid_orders[price] == 2:
        print("Ambiguous")
    else:
        print(" ".join(str(x) for x in sorted(valid_order[price])))
    
    
    