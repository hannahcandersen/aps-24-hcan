def solve(order_price):
    global menu, num_of_valid_orders, valid_order
    
    # Precompute all possible order prices
    possible_order_prices = set()
    for menu_price in menu:
        for price in num_of_valid_orders:
            new_price = price + menu_price
            if new_price <= order_price:
                possible_order_prices.add(new_price)

    # Iterate over all menu items and precomputed order prices
    for menuIndex, menuPrice in enumerate(menu):
        for price in possible_order_prices:
            new_order_price = price + menuPrice
            new_order = valid_order[price] + [menuIndex + 1]
            
            # New price exceeds the target order price, so skip it
            if new_order_price > order_price:
                continue
                
            if new_order_price not in num_of_valid_orders: 
                num_of_valid_orders[new_order_price] = 1
                valid_order[new_order_price] = new_order
            else:
                if sorted(new_order) != sorted(valid_order[new_order_price]):
                    num_of_valid_orders[new_order_price] = 2
                else:
                    num_of_valid_orders[new_order_price] += 1


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
    
    
    