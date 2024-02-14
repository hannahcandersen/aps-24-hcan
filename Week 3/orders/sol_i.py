N = int(input())
menu = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))
maxOrder = max(orders)

# Memoization - reuse for all orders
num_of_valid_orders = [0] * (maxOrder+1)      
valid_order = [[] for _ in range(maxOrder+1)] 

# Base case
num_of_valid_orders[0] = 1
valid_order[0] = [[]]

# Process orders
for totalPrice in orders:
    for price in range(1, totalPrice + 1): # For each price from 1 to totalPrice
        for menu_index, item_price in enumerate(menu): # For each item in the menu
            pre_price = price - item_price # Calculate the price without the current item
            if pre_price < 0: 
                continue # Try next item
            if pre_price == 0: # If we have found a valid order
                valid_order[price].append([menu_index + 1])
                num_of_valid_orders[price] += 1
                break # Try next price
            if num_of_valid_orders[pre_price] > 0: # If we have already calculated the number of valid orders for price - item_price
                for order in valid_order[pre_price]: # For each valid order for price - item_price
                    if menu_index + 1 not in order: # If we haven't already included the current item
                        valid_order[price].append(order + [menu_index + 1]) # Add the current item to the order
                        num_of_valid_orders[price] += 1 # Increment the number of valid orders for price
                break
            
            
            
    
   
    if num_of_valid_orders[totalPrice] == 0:
        print("Impossible")
    elif num_of_valid_orders[totalPrice] > 1:
        print("Ambiguous")
    else:
        print(" ".join(str(x) for x in valid_order[totalPrice]))