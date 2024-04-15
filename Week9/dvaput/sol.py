"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/zwdnut/problems/dvaput
Author: Hannah Camilla Andersen (hcan)
Date:   14/04

Description:
- Find the length of the longest substring that appeared at least twice in a given string.

Input:
- L: Length of the string (1 ≤ L ≤ 200.000)
- String of L characters a-z
Output:
- Output the length of the longest string that appears twice on a single line. 
- If there is no such string, output zero.

Solution description:
- 
"""
import random
import sys

# Prime number p used for the modulo operation in hash computation
p = 2**63 - 1
# Randomly select a base for the rolling hash function
a = random.randint(1, p - 1)  

def repeated_string(x, a, m): # x is the string, a is the base, m is the length of the substring
    # Set to store hash values of substrings we've encountered
    found = set()
    # Initialize the hash value
    h = 0
    # Compute a^m
    multiplier = 1

    # Compute the hash of x[0] .... x[m-1]
    for i in range(m):
        h = (h * a + ord(x[i])) % p
        multiplier = (multiplier * a) % p

    # Add the initial hash to the set of found hashes
    found.add(h)

    # Rolling hash over remaining string
    for i in range(1, n - m + 1):
        # Remove first coefficent a^{m - 1}x[i - 1] from h
        h = (a * h - ord(x[i-1]) * multiplier) % p
        # Add the new character to the hash
        h = (h + ord(x[i + m - 1])) % p

        # If the new hash is already in the set, we've found a repeated substring
        if h in found:
            return True
        found.add(h)
    # If no repeated substring is found, return False
    return False


n = int(input())  # Number of characters in input string
line = input()    # Input string

low = 0           # Lower bound of binary search
high = n - 1      # Upper bound of binary search

# Binary search to find the maximum length m of a substring that appears at least twice
while low < high:
    mid = (low + high + 1) // 2  # Middle point, leaning towards high
    # If a repeated substring of length mid exists, adjust low to search the upper half
    if repeated_string(line, a, mid):
        low = mid
    # Otherwise, search the lower half
    else:
        high = mid - 1

# Output the length of the longest repeated substring found
print(low)

    

