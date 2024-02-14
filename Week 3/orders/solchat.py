def find_order_iterative(order):
    global N, menu
    
    prev = [0] * (maxOrder+1)

    for i in range(N):
        for j in range(menu[i], maxOrder+1):
            if num_of_valid_orders[j-menu[i]] or j == menu[i]:
                if num_of_valid_orders[j] == 0:
                    num_of_valid_orders[j] = 1
                    valid_order[j] = valid_order[j-menu[i]] + [i+1]
                    prev[j] = j - menu[i]
                elif prev[j-menu[i]] != prev[j]:
                    num_of_valid_orders[j] = 2

    return {"num_of_valid_orders": num_of_valid_orders, "valid_order": valid_order}

N = int(input()) # Number of items on the menu
menu = list(map(int, input().split()))
M = int(input()) # Number of orders
orders = list(map(int, input().split()))
maxOrder = max(orders) 

# Memoization - reuse for all orders
num_of_valid_orders = [0] * (maxOrder+1)      # List to store the number of valid orders for each price 
valid_order = [[] for _ in range(maxOrder+1)] # List of lists to store the valid orders for each price

for order in orders:    
    # Update all the valid orders that can be achieved with this menu
    
    for item_index in range(N): # For each item on the menu
        for price in range(menu[item_index], maxOrder+1): # For each price from the price of the current item to the maximum order
            # Price is the price of the current item
            if price == menu[item_index]:
                num_of_valid_orders[price] += 1
                valid_order[price] = [item_index + 1]
            # Add the current price to the previous price without item (price - menu[item_index])
            
            
            elif price > menu[item_index]:
                num_of_valid_orders
            
            
            
            price_without_item = price - menu[item_index]
            # Base case: If price is equal to the price of the current item
            # Or if we have already calculated the number of valid orders for (price - item_price)
            if price == menu[item_index] or num_of_valid_orders[price_without_item]:
                num_of_valid_orders[price] = 1
                valid_order[price] = valid_order[price_without_item] + [item_index + 1] # Concat the added item to the previous valid order
            elif num_of_valid_orders[price_without_item] 
            
            
            
    

    for i in range(N): # For each item on the menu
        for j in range(menu[i], maxOrder+1): # For each price from the price of the current item to the maximum order
            if num_of_valid_orders[j-menu[i]] or j == menu[i]: # If we have already calculated the number of valid orders for price - item_price or the price is equal to the price of the current item
                if num_of_valid_orders[j] == 0: # If we haven't already calculated the number of valid orders for the current price
                    num_of_valid_orders[j] = 1 # Set the number of valid orders for the current price to 1
                    valid_order[j] = valid_order[j-menu[i]] + [i+1] # Set the valid order for the current price to the valid order for price - item_price plus the current item
                    prev[j] = j - menu[i] # Set the previous price to the price without the current item
                elif prev[j-menu[i]] != prev[j]: # If the previous price for price - item_price is not the same as the previous price for the current price
                    num_of_valid_orders[j] = 2 # Set the number of valid orders for the current price to 2
    
    if results["num_of_valid_orders"][order] > 1:
        print("Ambiguous")
    elif results["num_of_valid_orders"][order] == 0:
        print("Impossible")
    else:
        print(" ".join(str(x) for x in results["valid_order"][order]))
