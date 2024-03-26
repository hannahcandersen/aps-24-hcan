"""
Assignment: https://itu.kattis.com/courses/BAPS/APS24/assignments/f8j34o/problems/fenwick
Author: Hannah Camilla Andersen (hcan)
Date:   26/03

Description:
Build a fenwick tree for updates and prefix sum queries.
Operations: 
- Increment an element at index i
- Query the prefix sum of an element

Input: 
- First line with N Q
    - N = number of elements in the array (1 ≤ N ≤ 5.000.000)
    - Q = number of operations (0 ≤ Q ≤ 5.000.000)
- Q lines with operations of two types: 
    - + i p = a[i] += p 
    - ? a = Sum of all elements from a[0] to a[a-1]
Output:
- For each query of type ? print the sum of the elements from a[0] to a[a-1]

Complexity:  
- Update: O(log n)
- Query: O(log n)

Description:
- 1 indexed array
- Each element at index i is responsible for storing the sum of a certain range of elements in the original array. 
- This range is determined by the least significant bit (LSB) of the index in binary form

FenwickTree class inspired by https://github.itu.dk/algorithms/aps-24/blob/main/080-arrays/supercomputer/sol.py
"""
import sys

class FenwickTree():

    def __init__(self, size):
        # Initializes the Fenwick Tree with zeros. 1-indexed.
        self.Tree = [0] * (size + 1)
        
    def increment(self, i, val):
        # Increments the element at index i with val
        # This involves updating all relevant elements in the tree to ensure that prefix sums are maintained correctly.
        i = i + 1 # 1-indexed
        while i < len(self.Tree): # Loop until we reach the end of the tree
            self.Tree[i] += val
            i += i & -i # Parent increment by least significant bit
        
    def prefix_sum(self, i):
        # Calculates the prefix sum of the array up to index i.
        # This involves traversing the tree from the element corresponding to i, moving towards the root, and summing the values of the visited nodes.
        sum = 0
        while i > 0: # Loop until we reach the root
            sum += self.Tree[i]
            i -= i & -i # Left neighbor decrement by least significant bit
        return sum

# Main 
input = sys.stdin.readline  # Override input with faster reader. THIS IS WHY I DONT GET TIME LIMIT EXCEEDED
n, q = map(int, input().split())
fenwick = FenwickTree(n)
output = []  # Use a list to gather output - faster than printing directly

for _ in range(q):
    line = input().split()
    
    # Increment element at index i with p
    if line[0] == '+':
        i, p = map(int, line[1:])
        fenwick.increment(i, p)
        
    # Query the prefix sum of a[0] to a[a-1]
    elif line[0] == '?':
        a = int(line[1])
        output.append(str(fenwick.prefix_sum(a)))

print('\n'.join(output))
