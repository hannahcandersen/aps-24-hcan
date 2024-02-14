N = int(input())
menu = list(map(int, input().split()))
M = int(input())
orders = list(map(int, input().split()))
maxOrder = max(orders)

# Memoization - reuse for all orders
num_of_valid_orders = [0] * (maxOrder+1)
valid_order = [[] for _ in range(maxOrder+1)]

for order in orders:
    # Initialize a table to track if a certain price can be reached
    dp = [False] * (order+1)
    dp[0] = True  # Base case: 0 cost can be achieved
    
    # Loop through each item on the menu
    for cost in menu:
        # Update dp table from right to left to prevent using the same item multiple times
        for i in range(order, cost-1, -1):
            if dp[i - cost]:
                dp[i] = True
    
    if dp[order]:
        # If there is one unique order giving the specified total cost
        if dp.count(True) == 1:
            # Reconstruct the order
            current_order = []
            remaining_cost = order
            for i in range(N-1, -1, -1):
                while remaining_cost >= menu[i] and dp[remaining_cost - menu[i]]:
                    current_order.append(i + 1)
                    remaining_cost -= menu[i]
            valid_order[order] = sorted(current_order)
        else:
            print("Ambiguous")
            continue
    else:
        print("Impossible")
        continue
    
    print(" ".join(str(x) for x in valid_order[order]))