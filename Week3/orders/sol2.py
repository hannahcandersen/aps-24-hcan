def find_order(menu, total_cost):
    memo = {}

    def dp(index, remaining_cost):
        if remaining_cost == 0:
            return []
        if index == len(menu):
            return None
        if (index, remaining_cost) in memo:
            return memo[(index, remaining_cost)]

        # Try including the current item
        if menu[index] <= remaining_cost:
            included = dp(index, remaining_cost - menu[index])
            if included is not None:
                memo[(index, remaining_cost)] = [index + 1] + included
                return memo[(index, remaining_cost)]

        # Try excluding the current item
        excluded = dp(index + 1, remaining_cost)
        memo[(index, remaining_cost)] = excluded
        return excluded

    order = dp(0, total_cost)
    if order is None:
        return "Impossible"
    elif len(order) > 1:
        return "Ambiguous"
    else:
        return " ".join(map(str, order))


def main():
    num_items = int(input())
    menu = list(map(int, input().split()))
    num_orders = int(input())
    orders = list(map(int, input().split()))

    for order in orders:
        print(find_order(menu, order))


if __name__ == "__main__":
    main()