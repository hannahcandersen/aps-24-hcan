def solve(menu, order_total):
    # Number of ways to reach each total, with initialization for total 0
    ways = {0: []}
    ways[0].append([])  # Base case: one way to reach 0, with no items
    
    # Iterate through each item and its index in the menu
    for index, price in enumerate(menu, start=1):
        # Update combinations for reaching new totals
        for previous_total in list(ways.keys()):
            new_total = previous_total + price
            if new_total <= order_total:
                for way in ways[previous_total]:
                    new_way = way + [index]
                    if new_total not in ways:
                        ways[new_total] = []
                    ways[new_total].append(new_way)

    # Determine the result for the given order total
    if order_total not in ways:
        return "Impossible"
    elif len(ways[order_total]) > 1:
        return "Ambiguous"
    else:
        # If there's exactly one way, sort the indices and return them
        return " ".join(map(str, sorted(ways[order_total][0])))

# Read input
n = int(input())  # Number of items on the menu
menu = list(map(int, input().split()))
m = int(input())  # Number of orders
order_totals = [int(input()) for _ in range(m)]

# Solve for each order total
for order_total in order_totals:
    print(solve(menu, order_total))
