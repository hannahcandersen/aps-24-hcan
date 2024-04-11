import random
import sys

p = 2**63 - 1
a = random.randint(1, p - 1)  

def repeated_string(x, a, m):
    found = set() # all the hash codes we have seen
    h = 0
    # compute a^m
    multiplier = 1

    # compute hash of x[0],..., x[m - 1]
    for i in range(m):
        h = (h * a + ord(x[i])) % p
        multiplier = (multiplier * a) % p

    found.add(h)

    # rolling hash over remaining string
    for i in range(1, n - m + 1):
        # remove first coefficent a^{m - 1}x[i - 1] from h
        h = (a * h - ord(x[i-1]) * multiplier) %p
        h = (h + ord(x[i + m - 1])) %p

        if h in found:
            return True
        found.add(h)
    return False


n = int(input())
line = input()

low = 0
high = n - 1

# binary search for the right answer
while low < high:
    mid = (low + high + 1) // 2
    if repeated_string(line, a, mid):
        low = mid
    else:
        high = mid - 1

print(low)


    

